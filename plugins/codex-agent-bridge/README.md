# Codex Agent Bridge

This is a local Claude Code plugin that gives Claude a spinnable `codex-worker` agent backed by an OpenAI coding model over the Responses API.

## What it provides

- `agents/codex-worker.md`: a Claude subagent intended for bounded delegation to a Codex-style worker
- `.mcp.json`: a bundled MCP server definition
- `servers/codex-bridge.mjs`: a zero-dependency Node MCP server
- `scripts/start-claude-with-plugin.ps1`: a launcher that starts your installed Claude binary with this plugin loaded

## Important scope note

This plugin does **not** remote-control the running Codex desktop app or this current Codex session.

Instead, it delegates to OpenAI through the official Responses API using your `OPENAI_API_KEY`. By default it uses `gpt-5.2-codex`, and you can override that with `OPENAI_MODEL`.

## Requirements

- Node 22 or newer
- An OpenAI API key available as `OPENAI_API_KEY`
- A Claude Code executable on disk

## Environment variables

- `OPENAI_API_KEY`: required
- `OPENAI_MODEL`: optional, defaults to `gpt-5.2-codex`
- `OPENAI_BASE_URL`: optional, defaults to `https://api.openai.com/v1`

## Launching Claude with the plugin

From this repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\plugins\codex-agent-bridge\scripts\start-claude-with-plugin.ps1
```

If Claude is not auto-discovered, pass it explicitly:

```powershell
powershell -ExecutionPolicy Bypass -File .\plugins\codex-agent-bridge\scripts\start-claude-with-plugin.ps1 `
  -ClaudeExecutable "C:\Users\Contrite42\.vscode\extensions\anthropic.claude-code-2.1.85-win32-x64\resources\native-binary\claude.exe"
```

## How to use it in Claude

Once Claude is started with this plugin, ask for the bundled agent directly:

- "Use the `codex-worker` agent to review this patch."
- "Spin up `codex-worker` and have it propose a fix for this parser bug."
- "Ask `codex-worker` for a second opinion on this refactor plan."

You can also verify the plugin is wired correctly by having Claude call the `bridge_status` MCP tool.

## Delegate tool behavior

The MCP server exposes two tools:

- `delegate_task`: sends a bounded task to the OpenAI Responses API
- `bridge_status`: reports whether the key and model configuration are present

`delegate_task` accepts:

- `prompt`
- `task_type`
- `cwd`
- `files`
- `instructions`
- `model`
- `reasoning_effort`

## Notes

- Keep delegation bounded. This plugin is best for second opinions, scoped implementation plans, review passes, and targeted debugging.
- The `codex-worker` agent should pass file paths and constraints explicitly because the OpenAI delegate does not inherit Claude's local filesystem access.
- If you want a different model, set `OPENAI_MODEL` before launching Claude.
