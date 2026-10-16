# 🎙️ Bravo Voice Assistant
> **A Next-Generation Voice AI Assistant with Real-Time Audio Streaming, 3D Holographic HUD, Stark Protocols, and Comprehensive OS Control.**

---

## ✨ Overview

**Bravo** is a full-featured, low-latency desktop voice assistant inspired by Tony Stark's J.A.R.V.I.S. Built with PyQt6 and powered by Google's Gemini Live WebSocket API, Bravo combines real-time bidirectional voice interaction with 3D facial animation, proactive briefings, and deep operating system automation.

Say *"play the new Dune trailer"* and the video streams directly within the central HUD. Request *"execute Protocol Clean Slate"* or *"activate Focus Mode"*, and Bravo orchestrates multi-step desktop workflows, controls system hardware, launches applications, and manages files across your machine.

---

## 🚀 Key Capabilities

### 🧠 Core Features & Architecture
| Feature | Description |
|---|---|
| 🧑‍🎤 Holographic Avatar | Real-time animated 3D human mesh rendered in software (no heavy GPU requirements) |
| 👄 Real-time Lip-Sync | Viseme generation (~50 mouth shapes/sec) driven directly by incoming audio formants and live transcripts |
| 🎙️ Low-Latency Live Voice | Ultra-low latency bidirectional audio streaming via Gemini Live WebSocket API |
| ⚡ Stark Protocols | One-phrase multi-task macros ("Protocol Clean Slate", "Focus Mode", "System Audit") |
| 🎙️ Local Wake Word | Offline local **"Hey Bravo"** wake-word detection with automatic sleep/wake states |
| 🎚️ Push-to-Talk | Global keyboard shortcut (**Ctrl+Space**) for instant push-to-talk |
| 🪜 Multi-Tier Model Ladder | 9-model automated fallback ladder with cooldowns to guarantee 100% uptime |
| 🖥️ Deep OS & Hardware Control | Volume, display brightness, WiFi, power states, app launcher, process monitoring |
| 📂 Full File System Access | Read, organize, write, search, and manage files and directories across all drives |
| 🧠 Persistent Memory | Long-term memory engine with localized fast search and zero token bloat |
| ↩️ Action Reversal (Undo) | Voice-activated undo system that safely reverses file and system modifications |
| ⚠️ Human Confirmation Gate | Hardware-level UI confirmation dialog for critical power and network commands |
| 📊 Real-Time Hardware Telemetry | CPU, RAM, GPU, and thermals monitored continuously with proactive audio warnings |
| 👁️ Vision & Screen Analysis | Multi-source vision piping screen capture and webcam frames into Gemini |
| 📱 Remote Web Dashboard | LAN control panel with QR code pairing for remote mobile interaction |
| 🎨 Dynamic HUD Theming | Interactive theme color selector that dynamically re-tints the HUD and avatar |

---

## ⚡ Core Architecture

### 1. 🪜 Multi-Tier Model Fallback Ladder
All one-shot LLM requests route through an automated fallback ladder ordered by measured latency:
- `gemini-3.5-flash-lite` (Fastest, ~0.56s)
- `gemini-2.5-flash` (~0.67s)
- `gemini-3.1-flash-lite` (~0.60s)
- `gemini-2.5-flash-lite` (~0.74s)
- `gemini-3.5-flash` (~1.13s)

If any model encounters rate limits (429) or service outages (503/504), Bravo transparently routes the request to the next available tier with automatic cooldown management.

### 2. ⚡ Stark Protocols (One-Phrase Multi-Action Macros)
Custom macro engine allowing complex operations to execute from a single spoken phrase:
- **Clean Slate**: Closes non-essential background applications, cleans temporary caches, minimizes windows.
- **Deep Focus**: Silences notifications, dims accent lighting, sets system volume, and launches chosen development IDEs.
- **System Audit**: Runs real-time hardware diagnostics and reports health telemetry vocally.

### 3. 🧠 Hybrid Persistent Memory Architecture
Bravo divides memory into:
1. **Core Prompt Memory**: Compact identity and recently updated context (~900 characters).
2. **On-Demand Searchable Memory**: Full local JSON knowledge store queried in sub-milliseconds without inflating prompt tokens.
3. **Interactive Memory Panel**: GUI editor allowing you to inspect, modify, or delete stored facts at any time.

---

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/MAVERICKK97/Bravo-Voice-Assistant.git
cd Bravo-Voice-Assistant
```

### 2. Set Up API Keys
Copy the example configuration file:
```bash
cp config/api_keys.example.json config/api_keys.json
```
Edit `config/api_keys.json` and insert your Gemini API Key:
```json
{
  "gemini_api_key": "YOUR_GEMINI_API_KEY_HERE"
}
```

### 3. Install Dependencies & Run
```bash
pip install -r requirements.txt
python main.py
```

---

## 📋 System Requirements

| Requirement | Details |
| --- | --- |
| **Operating System** | Windows 10/11, macOS, or Linux |
| **Python** | Python 3.11, 3.12, or 3.13 |
| **Audio I/O** | Microphone and speakers/headphones |
| **API Key** | Google Gemini API Key |
| **Hardware** | Standard CPU (No dedicated GPU required for 3D HUD rendering) |

---

## 🗂️ Project Structure

```
Bravo-Voice-Assistant/
├── main.py                   # Core orchestrator — Gemini Live audio loop, tool dispatch, viseme pipeline
├── ui.py                     # PyQt6 HUD — 3D holographic avatar canvas, audio waveform, settings drawer
├── requirements.txt          # Python project dependencies
├── .gitignore                # Protects local credentials, certs, and long-term memory
├── actions/                  # Modular skill system (Tool definitions + handlers)
│   ├── computer_settings.py  # System volume, brightness, power state, WiFi toggles
│   ├── computer_control.py   # Window management, keyboard automation, mouse actions
│   ├── file_controller.py    # Multi-drive file operations (C: and D: drive management)
│   ├── file_processor.py     # Document reading, analysis, and summarization
│   ├── stark_protocols.py    # Custom multi-step automated workflows
│   ├── system_monitor.py     # Hardware telemetry (CPU, RAM, GPU, temperature)
│   ├── screen_processor.py   # Screen capture and webcam vision input
│   ├── web_search.py         # Multi-mode web search and grounded intelligence
│   ├── open_app.py           # Native application launcher
│   ├── browser_control.py    # Voice-driven web browser automation
│   ├── reminder.py           # Native scheduled notifications
│   ├── proactive.py          # Context-aware morning briefings and time-based check-ins
│   ├── video_player.py       # Embedded HUD video player
│   └── weather_report.py     # Live meteorological data
├── core/                     # Foundational subsystems
│   ├── gemini.py             # Model fallback ladder, timeouts, error isolation
│   ├── wake_word.py          # Local offline "Hey Bravo" wake-word listener
│   ├── avatar.py             # 3D software avatar rendering & lighting engine
│   ├── avatar_mesh.py        # Facial mesh geometry and rigging calculation
│   ├── viseme.py             # Phoneme/viseme synchronization for facial movement
│   ├── echo.py               # Self-echo cancellation guard
│   ├── undo.py               # Universal action undo manager
│   ├── confirm.py            # Safety gate for irreversible system operations
│   └── audio_devices.py      # Audio endpoint discovery, testing, and selection
├── config/
│   ├── api_keys.example.json # Safe configuration template
│   └── api_keys.json         # Local credentials (git-ignored)
└── memory/
    ├── memory_manager.py     # Persistent memory coordinator
    └── long_term.json        # Local factual memory store (git-ignored)
```

---

## 🔒 Security & Privacy

- **Local Execution**: All action execution, memory storage, and hardware controls run entirely on your local machine.
- **Zero Third-Party Telemetry**: There are no external tracking servers, metrics collectors, or third-party cloud services.
- **Credential Protection**: All API keys, TLS certificates, and personal memories are excluded from version control via `.gitignore`.
- **Confirmation Gateways**: Dangerous commands (such as OS power down or WiFi toggles) require physical user confirmation on the UI.
