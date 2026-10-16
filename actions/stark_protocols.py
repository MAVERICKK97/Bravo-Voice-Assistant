# stark_protocols.py
"""
Named "Stark Protocols" (One-Phrase Multi-Task Macros) for BRAVO.

Inspired by Tony Stark's J.A.R.V.I.S. protocols from Iron Man:
Orchestrates complex multi-action routines across audio, display,
hardware power schemes, background process termination, and application
workspaces in a single unified command.
"""
from __future__ import annotations

import json
import os
import platform
import subprocess
import sys
import time
from pathlib import Path

try:
    import psutil
    _PSUTIL = True
except ImportError:
    _PSUTIL = False

try:
    import pyautogui
    _PYAUTOGUI = True
except ImportError:
    _PYAUTOGUI = False

try:
    import pyperclip
    _PYPERCLIP = True
except ImportError:
    _PYPERCLIP = False

_OS = platform.system()

if _OS == "Windows":
    _WIN_HIDE: dict = {"creationflags": subprocess.CREATE_NO_WINDOW}
else:
    _WIN_HIDE: dict = {}


def _base_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).resolve().parent.parent


_PROTOCOLS_FILE = _base_dir() / "config" / "protocols.json"


def _play_protocol_chime():
    """Crisp futuristic audio chime (rising tone) when a protocol is engaged."""
    if _OS == "Windows":
        try:
            import winsound
            winsound.Beep(587, 60)   # D5 note (quick blip)
            winsound.Beep(880, 90)   # A5 note (rising confirmation)
        except Exception:
            pass


def _load_custom_protocols() -> dict:
    if not _PROTOCOLS_FILE.exists():
        return {}
    try:
        return json.loads(_PROTOCOLS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


# ── Built-in Stark Protocols ──────────────────────────────────────────────────

def _protocol_stealth(player=None) -> str:
    """Protocol Stealth: Instant lockdown, silence, and minimized displays."""
    _play_protocol_chime()
    from actions.computer_settings import lock_screen, show_desktop, volume_mute
    steps = []

    # 1. Minimize all windows
    try:
        show_desktop()
        steps.append("Displays cleared to desktop")
    except Exception:
        pass

    # 2. Stop any media playback
    if _PYAUTOGUI:
        try:
            pyautogui.press("stop")
            pyautogui.press("playpause")
            steps.append("Media playback stopped")
        except Exception:
            pass

    # 3. Mute master audio
    try:
        volume_mute()
        steps.append("Audio channels muted")
    except Exception:
        pass

    # 4. Lock computer
    try:
        lock_screen()
        steps.append("Workstation locked")
    except Exception:
        pass

    msg = "Protocol Stealth engaged, sir. All displays minimized, audio silenced, and workstation secured."
    if player:
        player.write_log("SYS: [PROTOCOL // STEALTH] Engaged.")
    return msg


def _protocol_focus(player=None, app: str | None = None) -> str:
    """Protocol Focus: Work environment setup, clears distractions, sets lighting & sound."""
    _play_protocol_chime()
    from actions.computer_settings import brightness_set, kill_app, volume_set
    from actions.open_app import open_app

    steps = []

    # 1. Terminate distracting background apps
    distractions = ["Steam", "Discord", "Netflix", "TikTok", "Instagram"]
    closed = []
    for d in distractions:
        try:
            res = kill_app(d)
            if "Terminated" in res:
                closed.append(d)
        except Exception:
            pass
    if closed:
        steps.append(f"Closed distractions ({', '.join(closed)})")

    # 2. Calibrate sound & display for deep focus
    try:
        volume_set(25)
        steps.append("Audio set to 25%")
    except Exception:
        pass

    try:
        brightness_set(75)
        steps.append("Display brightness set to 75%")
    except Exception:
        pass

    # 3. Launch primary workspace app (e.g. VS Code, or user requested app)
    target_app = app or "vscode"
    try:
        open_app({"app_name": target_app})
        steps.append(f"Launched {target_app}")
    except Exception:
        pass

    msg = f"Protocol Focus engaged, sir. {'; '.join(steps)}. Workspace deployed for optimal productivity."
    if player:
        player.write_log("SYS: [PROTOCOL // FOCUS] Engaged.")
    return msg


def _protocol_overclock(player=None, target_game: str | None = None) -> str:
    """Protocol Overclock: Maximum performance mode, High Performance power scheme, audio boost."""
    _play_protocol_chime()
    from actions.computer_settings import kill_app, volume_set
    from actions.open_app import open_app

    steps = []

    # 1. Switch Windows Power Scheme to High Performance or Ultimate Performance
    if _OS == "Windows":
        try:
            # 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c = High Performance
            # e9a42b02-d5df-448d-aa00-03f14749eb61 = Ultimate Performance
            subprocess.run(["powercfg", "/setactive", "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"],
                           capture_output=True, **_WIN_HIDE)
            steps.append("Windows High-Performance power plan activated")
        except Exception:
            pass

    # 2. Trim heavy non-essential background processes
    heavy_apps = ["Teams", "Slack"]
    trimmed = []
    for app in heavy_apps:
        try:
            res = kill_app(app)
            if "Terminated" in res:
                trimmed.append(app)
        except Exception:
            pass
    if trimmed:
        steps.append(f"Trimmed background processes ({', '.join(trimmed)})")

    # 3. Boost audio volume for immersion
    try:
        volume_set(75)
        steps.append("Master volume set to 75%")
    except Exception:
        pass

    # 4. Optional launch of game or game client
    if target_game:
        try:
            open_app({"app_name": target_game})
            steps.append(f"Booted {target_game}")
        except Exception:
            pass

    msg = f"Protocol Overclock engaged, sir. {'; '.join(steps)}. System resources channeled for maximum throughput."
    if player:
        player.write_log("SYS: [PROTOCOL // OVERCLOCK] Engaged.")
    return msg


def _protocol_clean_slate(player=None) -> str:
    """Protocol Clean Slate: Closes active windows, clears clipboard, returns to desktop."""
    _play_protocol_chime()
    from actions.computer_settings import show_desktop

    # 1. Clear clipboard
    if _PYPERCLIP:
        try:
            pyperclip.copy("")
        except Exception:
            pass

    # 2. Minimize to desktop
    try:
        show_desktop()
    except Exception:
        pass

    msg = "Protocol Clean Slate executed, sir. Clipboard purged and desktop restored to pristine condition."
    if player:
        player.write_log("SYS: [PROTOCOL // CLEAN SLATE] Executed.")
    return msg


def _protocol_night(player=None) -> str:
    """Protocol Sleep / Night: Dims display, mutes audio, turns off screen."""
    _play_protocol_chime()
    from actions.computer_settings import brightness_set, sleep_display, volume_mute

    try:
        volume_mute()
    except Exception:
        pass

    try:
        brightness_set(10)
    except Exception:
        pass

    try:
        sleep_display()
    except Exception:
        pass

    msg = "Protocol Sleep engaged, sir. Audio silenced, display dimmed and deactivated. Systems standing by."
    if player:
        player.write_log("SYS: [PROTOCOL // SLEEP] Engaged.")
    return msg


def _protocol_status_report(player=None) -> str:
    """Status Report: Complete tactical diagnostics briefing across all hardware subsystems."""
    lines = ["TACTICAL STATUS REPORT // MARK LV"]

    # 1. Power / Battery Subsystem
    if _PSUTIL:
        try:
            b = psutil.sensors_battery()
            if b:
                plug_str = "Charging / AC Online" if b.power_plugged else "On Battery Power"
                time_str = ""
                if 0 < b.secsleft < 86400 * 2:  # Valid within 48 hours
                    hrs = b.secsleft // 3600
                    mins = (b.secsleft % 3600) // 60
                    time_str = f" (~{hrs}h {mins}m remaining)"
                lines.append(f"• Power Core: {int(b.percent)}% ({plug_str}{time_str})")
            else:
                lines.append("• Power Core: Desktop AC Supply (Stable)")
        except Exception:
            lines.append("• Power Core: AC Online")

    # 2. CPU & Thermal
    if _PSUTIL:
        try:
            cpu_pct = psutil.cpu_percent(interval=0.2)
            cores = psutil.cpu_count(logical=True)
            lines.append(f"• CPU Load: {cpu_pct:.1f}% ({cores} logical cores)")
        except Exception:
            pass

    # 3. RAM / Memory
    if _PSUTIL:
        try:
            mem = psutil.virtual_memory()
            used_gb = mem.used / (1024 ** 3)
            total_gb = mem.total / (1024 ** 3)
            lines.append(f"• Memory Bus: {mem.percent}% ({used_gb:.1f} GB / {total_gb:.1f} GB utilized)")
        except Exception:
            pass

    # 4. Storage Drives
    if _PSUTIL:
        try:
            drives = []
            for part in psutil.disk_partitions(all=False):
                if os.name == 'nt' and ('cdrom' in part.opts or part.fstype == ''):
                    continue
                try:
                    usage = psutil.disk_usage(part.mountpoint)
                    free_gb = usage.free / (1024 ** 3)
                    drives.append(f"{part.mountpoint} ({free_gb:.0f} GB free)")
                except Exception:
                    pass
            if drives:
                lines.append(f"• Storage Volumes: {', '.join(drives)}")
        except Exception:
            pass

    # 5. Top Memory Consumer
    if _PSUTIL:
        try:
            top_proc = None
            top_mem = 0
            for p in psutil.process_iter(['name', 'memory_info']):
                try:
                    m = p.info['memory_info'].rss
                    if m > top_mem:
                        top_mem = m
                        top_proc = p.info['name']
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            if top_proc:
                mb = top_mem / (1024 * 1024)
                lines.append(f"• Primary Process: {top_proc} ({mb:.0f} MB)")
        except Exception:
            pass

    # 6. Uptime
    if _PSUTIL:
        try:
            up_secs = time.time() - psutil.boot_time()
            h = int(up_secs // 3600)
            m = int((up_secs % 3600) // 60)
            lines.append(f"• Workstation Uptime: {h} hours, {m} minutes")
        except Exception:
            pass

    lines.append("• Overall Status: All subsystems operating within normal parameters, sir.")

    report = "\n".join(lines)
    if player:
        player.write_log("SYS: [DIAGNOSTICS] Status report compiled.")
    return report


def _execute_custom_protocol(proto_name: str, proto_data: dict, player=None) -> str:
    """Executes a user-defined custom protocol from config/protocols.json."""
    _play_protocol_chime()
    from actions.computer_settings import brightness_set, kill_app, show_desktop, volume_set
    from actions.open_app import open_app

    steps = []

    if proto_data.get("minimize_others"):
        show_desktop()
        steps.append("minimized other windows")

    for app in proto_data.get("apps_to_close", []):
        try:
            kill_app(app)
            steps.append(f"closed {app}")
        except Exception:
            pass

    if "volume" in proto_data:
        try:
            vol = int(proto_data["volume"])
            volume_set(vol)
            steps.append(f"volume set to {vol}%")
        except Exception:
            pass

    if "brightness" in proto_data:
        try:
            brt = int(proto_data["brightness"])
            brightness_set(brt)
            steps.append(f"brightness set to {brt}%")
        except Exception:
            pass

    for app in proto_data.get("apps_to_open", []):
        try:
            open_app({"app_name": app})
            steps.append(f"opened {app}")
        except Exception:
            pass

    desc = proto_data.get("description", f"Protocol {proto_name}")
    msg = f"Protocol '{proto_name}' executed, sir ({desc}). Actions taken: {', '.join(steps) if steps else 'none'}."
    if player:
        player.write_log(f"SYS: [PROTOCOL // {proto_name.upper()}] Engaged.")
    return msg


# ── Main Handler ─────────────────────────────────────────────────────────────

def stark_protocols(
    parameters: dict,
    player=None,
    speak=None,
    response=None,
    session_memory=None,
) -> str:
    """
    Dispatcher for named Stark Protocols.
    """
    params = parameters or {}
    raw_name = str(params.get("protocol_name", "")).lower().strip()
    norm = raw_name
    for prefix in ("protocol_", "protocol ", "protocol"):
        if norm.startswith(prefix):
            norm = norm[len(prefix):].strip()
            break
    norm = norm.replace("mode", "").replace("-", "_").strip()

    options = params.get("options") or {}
    app = options.get("app")

    # 1. Stealth / Lockdown
    if norm in ("stealth", "lockdown", "secure", "lock_down"):
        return _protocol_stealth(player=player)

    # 2. Focus / Work
    if norm in ("focus", "work", "study_mode", "coding"):
        return _protocol_focus(player=player, app=app)

    # 3. Overclock / Gaming / Performance
    if norm in ("overclock", "gaming", "game", "performance", "high_performance"):
        return _protocol_overclock(player=player, target_game=app)

    # 4. Clean Slate
    if norm in ("clean_slate", "clean", "reset", "clear_desktop"):
        return _protocol_clean_slate(player=player)

    # 5. Night / Sleep
    if norm in ("sleep", "night", "goodnight", "bedtime"):
        return _protocol_night(player=player)

    # 6. Status Report / Diagnostics
    if norm in ("status_report", "status", "diagnostics", "armor_status", "system_status", "health"):
        return _protocol_status_report(player=player)

    # 7. List Protocols
    customs = _load_custom_protocols()
    if norm in ("list", "list_protocols", "protocols", "help", "available") or raw_name in ("list", "list_protocols", "protocols"):
        built_ins = ["stealth", "focus", "overclock", "clean_slate", "sleep", "status_report"]
        custom_names = list(customs.keys())
        return (
            f"Available Stark Protocols, sir:\n"
            f"• Standard: {', '.join(built_ins)}\n"
            f"• Custom (configured): {', '.join(custom_names) if custom_names else 'none'}\n"
            f"Say 'Protocol [name]' to engage any of them."
        )

    # 8. Check Custom Protocols in config/protocols.json
    if norm in customs:
        return _execute_custom_protocol(norm, customs[norm], player=player)

    # Check without normalization
    if raw_name in customs:
        return _execute_custom_protocol(raw_name, customs[raw_name], player=player)

    # Fallback suggestion
    return (
        f"I couldn't identify protocol '{raw_name}', sir. "
        f"Available protocols are: stealth, focus, overclock, clean_slate, sleep, status_report, "
        f"or custom protocols: {', '.join(customs.keys())}."
    )


# ── Tool declaration (auto-discovered by core/action_loader.py) ──────────────
TOOL = {
    "name": "stark_protocols",
    "description": (
        "Executes high-level multi-action Stark system protocols on the laptop. "
        "Use this whenever the user invokes or asks for a protocol (e.g. 'Protocol Stealth', 'Protocol Focus', "
        "'Protocol Overclock', 'Protocol Clean Slate', 'Protocol Sleep', 'Status Report / Diagnostics') "
        "or asks to enter work/gaming/stealth/night mode. Executes all associated system actions (apps, audio, "
        "brightness, security, power schemes, diagnostics) in a single unified sequence."
    ),
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "protocol_name": {
                "type": "STRING",
                "description": (
                    "The name of the protocol to engage: "
                    "stealth | focus | overclock | clean_slate | sleep | status_report | list_protocols | [custom_name]"
                )
            },
            "options": {
                "type": "OBJECT",
                "description": "Optional parameters such as specific 'app' to launch (e.g. game name or editor).",
                "properties": {
                    "app": {
                        "type": "STRING",
                        "description": "Specific application name to launch for focus or overclock/gaming mode."
                    }
                }
            }
        },
        "required": [
            "protocol_name"
        ]
    },
    "handler": stark_protocols,
}
