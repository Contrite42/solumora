[CmdletBinding()]
param(
  [string]$ClaudeExecutable,
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]]$ClaudeArgs
)

$ErrorActionPreference = "Stop"

$PluginRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

function Resolve-ClaudeExecutable {
  param([string]$ExplicitPath)

  if ($ExplicitPath) {
    $resolved = Resolve-Path -LiteralPath $ExplicitPath -ErrorAction Stop
    return $resolved.Path
  }

  $commandCandidates = @("claude", "claude.exe", "cc", "cc.cmd")
  foreach ($candidate in $commandCandidates) {
    $command = Get-Command $candidate -ErrorAction SilentlyContinue
    if ($command) {
      return $command.Source
    }
  }

  $appDataCmd = Join-Path $env:APPDATA "npm\claude.cmd"
  if (Test-Path -LiteralPath $appDataCmd) {
    return $appDataCmd
  }

  $extensionRoots = Join-Path $env:USERPROFILE ".vscode\extensions"
  if (Test-Path -LiteralPath $extensionRoots) {
    $matches = Get-ChildItem -Path $extensionRoots -Directory -Filter "anthropic.claude-code-*" |
      Sort-Object Name -Descending

    foreach ($match in $matches) {
      $candidate = Join-Path $match.FullName "resources\native-binary\claude.exe"
      if (Test-Path -LiteralPath $candidate) {
        return $candidate
      }
    }
  }

  throw "Could not find a Claude executable. Pass -ClaudeExecutable explicitly."
}

$ResolvedClaude = Resolve-ClaudeExecutable -ExplicitPath $ClaudeExecutable

if (-not $env:OPENAI_API_KEY) {
  Write-Warning "OPENAI_API_KEY is not set in this shell. The codex bridge will load, but delegate_task will fail until that variable is present."
}

$LaunchArgs = @("--plugin-dir", $PluginRoot)
if ($ClaudeArgs) {
  $LaunchArgs += $ClaudeArgs
}

Write-Host "Launching Claude with plugin:" $PluginRoot
Write-Host "Executable:" $ResolvedClaude

if ($ResolvedClaude.ToLowerInvariant().EndsWith(".cmd")) {
  & cmd.exe /c $ResolvedClaude @LaunchArgs
  exit $LASTEXITCODE
}

& $ResolvedClaude @LaunchArgs
exit $LASTEXITCODE
