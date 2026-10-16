# system_command.py
"""
Executes system shell / PowerShell commands on the user's laptop.
Enables BRAVO to perform administrative tasks, install software (winget),
inspect network/disk/hardware status, and run system utilities.
"""
import os
import sys
import subprocess
import platform
from pathlib import Path

_OS = platform.system()

# Disallow destructive wipe commands
_BLOCKED_PATTERNS = [
    "format c:",
    "del /f /s /q c:\\windows",
    "rmdir /s /q c:\\windows",
    ":(){ :|:& };:",
    "rm -rf / --no-preserve-root",
]


def _is_safe(cmd: str) -> tuple[bool, str]:
    low = cmd.lower()
    for pattern in _BLOCKED_PATTERNS:
        if pattern in low:
            return False, f"Blocked unsafe system command containing '{pattern}'."
    return True, ""


def system_command(
    parameters: dict,
    player=None,
    speak=None,
    response=None,
    session_memory=None,
) -> str:
    """
    Executes a shell or PowerShell command on the host laptop.
    """
    params = parameters or {}
    command = str(params.get("command", "")).strip()

    if not command:
        return "No command provided to execute."

    safe, reason = _is_safe(command)
    if not safe:
        return reason

    working_dir = params.get("working_dir")
    cwd = None
    if working_dir:
        p = Path(working_dir).expanduser().resolve()
        if p.is_dir():
            cwd = str(p)

    timeout = int(params.get("timeout", 45))

    print(f"[SystemCommand] Executing: {command} (timeout={timeout}s, cwd={cwd})")
    if player:
        player.write_log(f"[Terminal] {command[:60]}")

    try:
        if _OS == "Windows":
            # Run in PowerShell
            proc = subprocess.run(
                ["powershell", "-NoProfile", "-NonInteractive", "-Command", command],
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=timeout,
                creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, "CREATE_NO_WINDOW") else 0,
            )
        else:
            proc = subprocess.run(
                command,
                shell=True,
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=timeout,
            )

        stdout = (proc.stdout or "").strip()
        stderr = (proc.stderr or "").strip()
        code = proc.returncode

        # Format output for Gemini
        result_parts = []
        if code != 0:
            result_parts.append(f"Exit code: {code}")
        if stdout:
            # Truncate if extremely long to preserve context window
            trimmed = stdout if len(stdout) <= 2500 else stdout[:2400] + "\n...[truncated]"
            result_parts.append(trimmed)
        if stderr:
            trimmed_err = stderr if len(stderr) <= 1000 else stderr[:900] + "\n...[truncated stderr]"
            result_parts.append(f"Errors:\n{trimmed_err}")

        if not result_parts:
            return f"Command executed successfully (exit code {code}, no output)."

        return "\n".join(result_parts)

    except subprocess.TimeoutExpired:
        return f"Command timed out after {timeout} seconds."
    except Exception as e:
        return f"Failed to execute command: {e}"


# ── Tool declaration (auto-discovered by core/action_loader.py) ──────────────
TOOL = {
    "name": "system_command",
    "description": (
        "Executes a system command or PowerShell script on the user's laptop. "
        "Use this for running terminal commands, installing apps via winget (e.g. 'winget install ...'), "
        "checking network/IP (ipconfig, ping), checking storage space, querying running tasks, or system configuration."
    ),
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "command": {
                "type": "STRING",
                "description": "The exact shell or PowerShell command string to execute."
            },
            "working_dir": {
                "type": "STRING",
                "description": "Optional working directory path to run the command in."
            },
            "timeout": {
                "type": "INTEGER",
                "description": "Execution timeout in seconds (default: 45)."
            }
        },
        "required": [
            "command"
        ]
    },
    "handler": system_command,
}
