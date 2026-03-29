#!/usr/bin/env node

import readline from "node:readline";

const SERVER_NAME = "codex-bridge";
const SERVER_VERSION = "0.1.0";
const SUPPORTED_PROTOCOL_VERSION = "2025-11-25";
const DEFAULT_MODEL = process.env.OPENAI_MODEL || "gpt-5.2-codex";
const DEFAULT_BASE_URL = process.env.OPENAI_BASE_URL || "https://api.openai.com/v1";

const TOOL_DEFINITIONS = [
  {
    name: "delegate_task",
    title: "Delegate Task To Codex",
    description:
      "Send a bounded coding, review, debugging, or analysis task to an OpenAI coding model and return the result.",
    inputSchema: {
      type: "object",
      properties: {
        prompt: {
          type: "string",
          description: "The task to delegate.",
        },
        task_type: {
          type: "string",
          enum: ["coding", "review", "debug", "analysis", "general"],
          description: "What kind of work the delegate should prioritize.",
        },
        cwd: {
          type: "string",
          description: "Optional working directory to mention in the prompt.",
        },
        files: {
          type: "array",
          items: { type: "string" },
          description: "Optional relevant file paths to include in the task brief.",
        },
        instructions: {
          type: "string",
          description: "Optional extra constraints, style guidance, or acceptance criteria.",
        },
        model: {
          type: "string",
          description: `Override model name. Defaults to ${DEFAULT_MODEL}.`,
        },
        reasoning_effort: {
          type: "string",
          enum: ["low", "medium", "high", "xhigh"],
          description: "Optional reasoning effort for supported OpenAI reasoning models.",
        },
      },
      required: ["prompt"],
    },
    outputSchema: {
      type: "object",
      properties: {
        model: { type: "string" },
        response_id: { type: "string" },
        output_text: { type: "string" },
        usage: { type: "object" },
      },
      required: ["model", "output_text"],
    },
  },
  {
    name: "bridge_status",
    title: "Codex Bridge Status",
    description:
      "Report the Codex bridge configuration so Claude can verify the plugin is wired correctly.",
    inputSchema: {
      type: "object",
      properties: {},
    },
    outputSchema: {
      type: "object",
      properties: {
        openai_api_key_present: { type: "boolean" },
        default_model: { type: "string" },
        base_url: { type: "string" },
      },
      required: ["openai_api_key_present", "default_model", "base_url"],
    },
  },
];

function log(level, message, extra = undefined) {
  const stamp = new Date().toISOString();
  const suffix = extra === undefined ? "" : ` ${JSON.stringify(extra)}`;
  process.stderr.write(`[${stamp}] ${level.toUpperCase()} ${message}${suffix}\n`);
}

function send(message) {
  process.stdout.write(`${JSON.stringify(message)}\n`);
}

function sendResult(id, result) {
  send({ jsonrpc: "2.0", id, result });
}

function sendError(id, code, message, data = undefined) {
  send({
    jsonrpc: "2.0",
    id,
    error: {
      code,
      message,
      ...(data === undefined ? {} : { data }),
    },
  });
}

function toolResult(text, structuredContent = undefined, isError = false) {
  return {
    content: [{ type: "text", text }],
    ...(structuredContent ? { structuredContent } : {}),
    ...(isError ? { isError: true } : {}),
  };
}

function buildSystemPrompt(taskType) {
  const base =
    "You are Codex, a pragmatic senior software engineer. Give direct, technically rigorous answers. Optimize for actionable output, concrete tradeoffs, and minimal fluff.";

  const additions = {
    coding:
      " Focus on implementation details, edge cases, and clear patch direction. Prefer concrete code-oriented guidance over general theory.",
    review:
      " Focus on bugs, regressions, missing tests, and risky assumptions before style concerns.",
    debug:
      " Focus on likely root causes, verification steps, and the smallest high-confidence fixes first.",
    analysis:
      " Focus on architecture, tradeoffs, and the most decision-relevant details.",
    general:
      " Stay concise and practical.",
  };

  return `${base}${additions[taskType] || additions.general}`;
}

function buildDelegationInput(args) {
  const sections = [];
  const taskType = args.task_type || "coding";

  sections.push(`Task type: ${taskType}`);

  if (args.cwd) {
    sections.push(`Working directory:\n${args.cwd}`);
  }

  if (Array.isArray(args.files) && args.files.length > 0) {
    sections.push(`Relevant files:\n${args.files.map((file) => `- ${file}`).join("\n")}`);
  }

  if (args.instructions) {
    sections.push(`Constraints and additional instructions:\n${args.instructions}`);
  }

  sections.push(`Task:\n${args.prompt}`);

  return sections.join("\n\n");
}

function extractTextFromOutput(output) {
  if (!Array.isArray(output)) {
    return "";
  }

  const parts = [];
  for (const item of output) {
    if (!Array.isArray(item?.content)) {
      continue;
    }

    for (const block of item.content) {
      if (typeof block?.text === "string" && block.text.trim()) {
        parts.push(block.text);
      }
    }
  }

  return parts.join("\n\n").trim();
}

function readErrorMessage(payload, fallback) {
  if (payload && typeof payload === "object") {
    if (typeof payload.error?.message === "string" && payload.error.message.trim()) {
      return payload.error.message;
    }
    if (typeof payload.message === "string" && payload.message.trim()) {
      return payload.message;
    }
  }

  return fallback;
}

async function callOpenAIResponses(args) {
  const apiKey = process.env.OPENAI_API_KEY;
  if (!apiKey) {
    throw new Error("OPENAI_API_KEY is not set.");
  }

  const model = args.model || DEFAULT_MODEL;
  const taskType = args.task_type || "coding";
  const payload = {
    model,
    instructions: buildSystemPrompt(taskType),
    input: buildDelegationInput(args),
    store: false,
  };

  if (args.reasoning_effort) {
    payload.reasoning = { effort: args.reasoning_effort };
  }

  const response = await fetch(`${DEFAULT_BASE_URL.replace(/\/$/, "")}/responses`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const body = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(readErrorMessage(body, `OpenAI request failed with status ${response.status}.`));
  }

  const outputText =
    (typeof body.output_text === "string" && body.output_text.trim()) ||
    extractTextFromOutput(body.output) ||
    "[No text output returned by the model.]";

  return {
    model: body.model || model,
    response_id: body.id || "",
    output_text: outputText,
    usage: body.usage || {},
  };
}

async function handleToolCall(params) {
  const name = params?.name;
  const args = params?.arguments || {};

  if (name === "bridge_status") {
    const result = {
      openai_api_key_present: Boolean(process.env.OPENAI_API_KEY),
      default_model: DEFAULT_MODEL,
      base_url: DEFAULT_BASE_URL,
    };

    return toolResult(
      [
        `OpenAI API key present: ${result.openai_api_key_present}`,
        `Default model: ${result.default_model}`,
        `Base URL: ${result.base_url}`,
      ].join("\n"),
      result,
    );
  }

  if (name === "delegate_task") {
    if (typeof args.prompt !== "string" || !args.prompt.trim()) {
      return toolResult("delegate_task requires a non-empty `prompt`.", undefined, true);
    }

    try {
      const result = await callOpenAIResponses(args);
      const summaryLines = [
        `Model: ${result.model}`,
        result.response_id ? `Response ID: ${result.response_id}` : null,
        "",
        result.output_text,
      ].filter(Boolean);

      return toolResult(summaryLines.join("\n"), result);
    } catch (error) {
      return toolResult(
        `Codex bridge failed: ${error instanceof Error ? error.message : String(error)}`,
        undefined,
        true,
      );
    }
  }

  return toolResult(`Unknown tool: ${name}`, undefined, true);
}

async function handleRequest(message) {
  switch (message.method) {
    case "initialize": {
      const requestedVersion = message.params?.protocolVersion;
      if (
        typeof requestedVersion === "string" &&
        requestedVersion !== SUPPORTED_PROTOCOL_VERSION
      ) {
        sendError(message.id, -32602, "Unsupported protocol version", {
          supported: [SUPPORTED_PROTOCOL_VERSION],
          requested: requestedVersion,
        });
        return;
      }

      sendResult(message.id, {
        protocolVersion: SUPPORTED_PROTOCOL_VERSION,
        capabilities: {
          tools: {
            listChanged: false,
          },
        },
        serverInfo: {
          name: SERVER_NAME,
          version: SERVER_VERSION,
        },
        instructions:
          "Use delegate_task for bounded work you want sent to the OpenAI coding model. Use bridge_status to verify configuration.",
      });
      return;
    }
    case "tools/list":
      sendResult(message.id, { tools: TOOL_DEFINITIONS });
      return;
    case "tools/call": {
      const result = await handleToolCall(message.params);
      sendResult(message.id, result);
      return;
    }
    case "logging/setLevel":
      sendResult(message.id, {});
      return;
    case "ping":
      sendResult(message.id, {});
      return;
    default:
      sendError(message.id, -32601, `Method not found: ${message.method}`);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  crlfDelay: Infinity,
});

rl.on("line", async (line) => {
  const trimmed = line.trim();
  if (!trimmed) {
    return;
  }

  let message;
  try {
    message = JSON.parse(trimmed);
  } catch (error) {
    log("error", "Failed to parse JSON input", { error: String(error) });
    return;
  }

  if (!message || message.jsonrpc !== "2.0") {
    if (message?.id !== undefined) {
      sendError(message.id, -32600, "Invalid Request");
    }
    return;
  }

  if (message.id === undefined) {
    if (message.method && message.method !== "notifications/initialized") {
      log("info", "Ignoring notification", { method: message.method });
    }
    return;
  }

  try {
    await handleRequest(message);
  } catch (error) {
    log("error", "Unhandled request failure", {
      method: message.method,
      error: error instanceof Error ? error.message : String(error),
    });
    sendError(
      message.id,
      -32603,
      error instanceof Error ? error.message : "Internal error",
    );
  }
});

rl.on("close", () => {
  log("info", "stdin closed");
});

log("info", "Codex bridge server started", {
  defaultModel: DEFAULT_MODEL,
  baseUrl: DEFAULT_BASE_URL,
});
