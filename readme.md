# 🎙️ Bravo Voice Assistant
> **An Advanced Desktop Voice AI Assistant featuring Real-Time Gemini Live Audio Streaming, 3D Holographic HUD, Stark Protocols, and Comprehensive OS Automation.**

[![Python Version](https://img.shields.io/badge/Python-3.11%20%7C%203.12%20%7C%203.13-blue?logo=python&logoColor=white)](https://www.python.org/)
[![GUI Framework](https://img.shields.io/badge/GUI-PyQt6-green?logo=qt&logoColor=white)](https://riverbankcomputing.com/software/pyqt/)
[![AI Engine](https://img.shields.io/badge/AI%20Engine-Gemini%20Live%20API-orange?logo=google&logoColor=white)](https://ai.google.dev/)
[![OS Support](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?logo=windows&logoColor=white)](#-system-requirements)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 📑 Table of Contents
1. [Overview & Vision](#-overview--vision)
2. [System Architecture](#-system-architecture)
3. [Key Highlights & Capabilities](#-key-highlights--capabilities)
4. [Stark Protocols (Macro Automation)](#-stark-protocols-macro-automation)
5. [Operating System & Hardware Control](#-operating-system--hardware-control)
6. [Resilience & Fallback Ladder](#-resilience--fallback-ladder)
7. [Persistent Memory Architecture](#-persistent-memory-architecture)
8. [Multimodal Vision & Media](#-multimodal-vision--media)
9. [Mobile LAN Remote Dashboard](#-mobile-lan-remote-dashboard)
10. [Voice Commands Cheat Sheet](#-voice-commands-cheat-sheet)
11. [Installation & Setup](#-installation--setup)
12. [Project File Structure](#-project-file-structure)
13. [Security & Privacy](#-security--privacy)
14. [Academic & Team Collaboration](#-academic--team-collaboration)

---

## 🌟 Overview & Vision

**Bravo** is an intelligent, low-latency, full-duplex desktop voice assistant inspired by Tony Stark's J.A.R.V.I.S. Built using **PyQt6** and Google's **Gemini Live WebSocket API**, Bravo breaks away from traditional turn-based "command-and-wait" chatbots to provide a truly responsive, hands-free personal computing companion.

### Why Bravo?
- **Full-Duplex Audio**: Talk and listen simultaneously. Interrupt Bravo mid-sentence without waiting for speech synthesis to finish.
- **3D Software-Rendered Avatar**: An interactive, holographic human mesh rendered entirely in software—delivering 3D facial animation, eye saccades, and realistic viseme lip-sync without requiring heavy 3D game engines or dedicated GPUs.
- **Deep Desktop Automation**: Unlocked access across both `C:` and `D:` drives, system power states, display brightness, volume mixers, application launching, and browser control.
- **Stark Protocols**: One-phrase multi-task macros that orchestrate entire workspace environments in seconds.

---

## 🏛️ System Architecture

```
                  ┌──────────────────────────────────────────────┐
                  │                 USER AUDIO                   │
                  │   (Microphone / Local "Hey Bravo" Listener)  │
                  └──────────────────────┬───────────────────────┘
                                         │ PCM16 Audio Stream (16 kHz)
                                         ▼
                  ┌──────────────────────────────────────────────┐
                  │              ECHO & NOISE GUARD              │
                  │   Distinguishes user voice from system audio │
                  └──────────────────────┬───────────────────────┘
                                         │ Filtered Audio Chunks
                                         ▼
┌────────────────────────────────────────────────────────────────────────────────┐
│                        GEMINI LIVE WEBSOCKET SESSION                           │
│  Bidirectional full-duplex stream · Real-time LLM · Server-side audio synthesis │
└──────────────┬──────────────────────────────────────────────────┬──────────────┘
               │ Incoming PCM Audio (24 kHz)                      │ Tool Call JSON
               ▼                                                  ▼
┌──────────────────────────────────────────────┐ ┌───────────────────────────────┐
│              VISEME & AUDIO PIPELINE         │ │      TOOL DISPATCH ENGINE     │
│  Extracts speech formants & phonemes         │ │  • Stark Protocols            │
│  Synchronizes ~50 mouth visemes per second   │ │  • File Controller (C: & D:)  │
└──────────────────────┬───────────────────────┘ │  • Hardware Settings Mixer    │
                       │                         │  • Screen & Camera Vision     │
                       ▼                         │  • Web Search & Browser Ops   │
┌──────────────────────────────────────────────┐ └───────────────┬───────────────┘
│                 PYQT6 HUD                    │                 │
│  • 3D Holographic Software Avatar Canvas     │                 │ State & Log
│  • Audio-Reactive Waveform Visualizer        │◄────────────────┘ Updates
│  • Slide-Out Setup & Control Drawers         │
│  • Integrated Video & Telemetry Layer        │
└──────────────────────────────────────────────┘
```

---

## 🚀 Key Highlights & Capabilities

### 🧑‍🎤 1. 3D Holographic Avatar & Realistic Lip-Sync
- **Software Vector Projection**: Uses 3D geometry from a 468-vertex facial mesh rendered cleanly via Qt's 2D vector graphics pipeline (`QPainter`).
- **Real-Time Lip-Sync**: Analyzes both incoming audio formants and live text transcripts to compute ~50 viseme mouth shapes per second.
- **Facial Dynamics**: Features natural blinking, subtle head tracking nods on stressed syllables, and saccadic eye movements. The avatar looks down when reading and meets your eyes when actively listening.

### 🎙️ 2. Offline Wake Word & Push-to-Talk
- **Local Wake Word ("Hey Bravo")**: Listens locally on an isolated background thread. Auto-sleeps after periods of inactivity to conserve CPU and bandwidth. Zero audio is sent over the internet while asleep.
- **Global Push-to-Talk**: Hold **Ctrl+Space** anywhere on your desktop to speak instantly without saying the wake word.

### ↩️ 3. Universal Action Reversal (Undo Engine)
- Say *"undo"* in plain language, and Bravo reverses its last modification:
  - **Files**: Moves files back to their original paths, restores edited contents, unlinks newly created empty folders.
  - **Settings**: Restores previous volume levels, brightness settings, or desktop themes.

### ⚠️ 4. Human-in-the-Loop Confirmation Gate
- Destructive commands (system shutdown, restart, disabling network interfaces) trigger a direct UI confirmation dialog on the HUD. The assistant cannot bypass this safety gate on its own.

---

## ⚡ Stark Protocols (Macro Automation)

Stark Protocols allow you to execute sophisticated, multi-step actions across hardware, applications, and operating system states with a single spoken command:

| Protocol Name | Voice Trigger | Actions Executed |
|---|---|---|
| **Protocol Stealth** | *"Engage Protocol Stealth"* | Clears all windows to desktop, stops active media playback, mutes master audio, and locks the workstation. |
| **Protocol Focus** | *"Activate Focus Mode"* | Closes distracting apps (Discord, Steam, Netflix), dims display brightness to 75%, sets volume to 25%, and boots your coding IDE (VS Code). |
| **Protocol Overclock** | *"Initiate Protocol Overclock"* | Activates Windows Ultimate/High-Performance power scheme, trims non-essential background processes, and boosts audio. |
| **Protocol Clean Slate** | *"Execute Clean Slate"* | Purges clipboard history, minimizes all windows, and returns the workspace to a pristine desktop state. |
| **Protocol Night** | *"Initiate Protocol Night"* | Mutes system audio, dims display brightness to 0%, puts displays to sleep, and sets Bravo into low-power standby. |
| **Protocol Audit** | *"Run System Audit"* | Runs comprehensive hardware diagnostics (CPU utilization, RAM load, GPU usage, thermal levels) and reads a voice report. |

> [!TIP]
> **Custom Protocols:** You can define your own automated macros simply by adding custom entries to `config/protocols.json` or extending [`actions/stark_protocols.py`](file:///d:/Academics/Projects/Bravo%20Voice%20Assistant/actions/stark_protocols.py).

---

## 🖥️ Operating System & Hardware Control

Bravo is engineered for true desktop autonomy with safe, full-system access:

### 📂 Multi-Drive File Operations
- **Full Access across C: and D: Drives**: Search, create, move, rename, read, edit, and organize files across your entire file system.
- **Desktop Organizer**: Analyzes cluttered desktop directories and organizes files cleanly into categorized folders (Images, Documents, Code, Archives) with single-command undo support.
- **Document Intelligence**: Summarizes and answers complex questions from local PDFs, text documents, spreadsheets, and source code files.

### ⚙️ Hardware & Device Management
- **Audio Device Resolver**: Probes and enumerates all physical input and output endpoints. Automatically resolves host APIs (MME, DirectSound, WASAPI) to prevent driver dropouts.
- **Display & Audio Mixers**: Adjusts system volume, mutes audio, controls monitor backlight brightness, and toggles dark mode.
- **Power Operations**: Puts displays to sleep, locks the screen, triggers restarts, and handles scheduled shutdowns.

---

## 🪜 Resilience & Fallback Ladder

To ensure Bravo never fails or freezes during network degradation or API rate limits, all one-shot intelligence requests pass through an automated **9-Model Fallback Ladder**:

```
                       ┌────────────────────────────┐
                       │   gemini-3.5-flash-lite    │  (Fastest ~0.56s)
                       └─────────────┬──────────────┘
                                     │ 429 Quota / Timeout
                                     ▼
                       ┌────────────────────────────┐
                       │     gemini-2.5-flash       │  (Reliable ~0.67s)
                       └─────────────┬──────────────┘
                                     │ Error / 503
                                     ▼
                       ┌────────────────────────────┐
                       │   gemini-3.1-flash-lite    │  (~0.60s)
                       └─────────────┬──────────────┘
                                     │ Fallback
                                     ▼
                       ┌────────────────────────────┐
                       │    gemini-2.5-flash-lite   │  (~0.74s)
                       └─────────────┬──────────────┘
                                     │ Fallback
                                     ▼
                       ┌────────────────────────────┐
                       │     gemini-3.5-flash       │  (~1.13s)
                       └────────────────────────────┘
```

- **Dynamic Cooldown Periods**:
  - `429 Quota Exhausted`: Cooled for 5 minutes.
  - `503 / 504 Outage / Timeout`: Cooled for 30 minutes.
  - `404 Key Incompatible`: Cooled for 6 hours.
- **Live Voice Engine Fallback**: The real-time Live WebSocket engine maintains an independent dual-model failover path so conversations are never dropped.

---

## 🧠 Persistent Memory Architecture

Bravo features a hierarchical local memory system that eliminates token bloat while ensuring the assistant remembers personal context across sessions:

1. **Active Context Injection**: Stores user identity, personal preferences, and recent topics in a lightweight prompt block (< 1,000 characters).
2. **On-Demand Local Search**: A built-in local retrieval tool searches the full `memory/long_term.json` knowledge store in sub-milliseconds without making extra API calls.
3. **Interactive Memory Panel**: Open the GUI memory editor (**⚙ → MEMORY**) to view every learned fact, inspect timestamps, and delete entries with a single click.

---

## 👁️ Multimodal Vision & Media

- **Live Screen Analysis**: Takes immediate screenshots of single or dual-monitor setups to analyze errors, explain code, or locate information on your screen.
- **Webcam Integration**: Streams webcam frames into Gemini for real-world object recognition and visual queries.
- **HUD Video Player**: Directly streams YouTube videos, direct media URLs, or local MP4 files directly into the central HUD where the avatar sits. Automatically ducks audio and mutes microphone to prevent self-echo.

---

## 📱 Mobile LAN Remote Dashboard

Control Bravo from your smartphone without installing third-party apps:
1. Open **⚙ → REMOTE** in the desktop interface.
2. Scan the generated QR code with your mobile device on the same local Wi-Fi network.
3. Access a mobile-optimized control dashboard over secure local HTTPS (using locally generated self-signed TLS certificates) to issue text commands, monitor hardware telemetry, and execute Stark Protocols remotely.

---

## 🗣️ Voice Commands Cheat Sheet

| Category | Example Spoken Command |
|---|---|
| **Conversation** | *"Bravo, explain how quantum computing differs from classical bits."* |
| **Stark Protocols** | *"Execute Protocol Focus."* / *"Bravo, engage Protocol Stealth."* |
| **System Settings** | *"Set display brightness to 80 percent and turn the volume down to 30."* |
| **File Automation** | *"Find all PDF files downloaded this week on drive D and summarize them."* |
| **Desktop Ops** | *"Organize my desktop."* / *"Undo the last action."* |
| **Vision** | *"Bravo, look at my screen and tell me why this code isn't compiling."* |
| **Media** | *"Play the official Interstellar soundtrack in the HUD."* |
| **Hardware** | *"What is my current GPU temperature and CPU utilization?"* |

---

## ⚡ Installation & Setup

### 1. Prerequisites
- **Operating System**: Windows 10/11, macOS 12+, or modern Linux.
- **Python**: Version `3.11`, `3.12`, or `3.13`.
- **Hardware**: Working microphone and audio output. (No dedicated GPU required).

### 2. Clone the Repository
```bash
git clone https://github.com/MAVERICKK97/Bravo-Voice-Assistant.git
cd Bravo-Voice-Assistant
```

### 3. Create a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Your API Key
Copy the example configuration file:
```bash
cp config/api_keys.example.json config/api_keys.json
```
Edit `config/api_keys.json` and insert your Gemini API Key:
```json
{
  "gemini_api_key": "YOUR_ACTUAL_GEMINI_API_KEY_HERE"
}
```

### 6. Launch Bravo
```bash
python main.py
```

---

## 🗂️ Project File Structure

```
Bravo-Voice-Assistant/
├── main.py                   # Central orchestrator — Gemini Live loop, tool dispatch, audio I/O
├── ui.py                     # PyQt6 HUD — 3D software avatar, waveform, drawer panels, log view
├── setup.py                  # Platform-aware dependency setup script
├── requirements.txt          # Python dependencies
├── .gitignore                # Protects credentials, certs, and local memory
│
├── actions/                  # Modular skill handlers & tool definitions
│   ├── stark_protocols.py    # Custom multi-step macros (Stealth, Focus, Overclock, etc.)
│   ├── computer_settings.py  # System volume, brightness, power state, and WiFi toggles
│   ├── computer_control.py   # Window switcher, keyboard shortcuts, mouse actions
│   ├── file_controller.py    # Multi-drive file operations (C: and D: drive management)
│   ├── file_processor.py     # Document reading, analysis, and text summarization
│   ├── system_monitor.py     # Real-time CPU, RAM, GPU, and thermal telemetry
│   ├── screen_processor.py   # Screen capture and webcam vision input
│   ├── web_search.py         # Multi-mode grounded web search
│   ├── open_app.py           # Application launcher
│   ├── browser_control.py    # Voice-driven web browser automation
│   ├── reminder.py           # Native scheduled notifications
│   ├── proactive.py          # Time-aware morning briefings and contextual check-ins
│   ├── video_player.py       # Embedded HUD video player
│   └── weather_report.py     # Live meteorological reporting
│
├── core/                     # Core system modules
│   ├── gemini.py             # Model fallback ladder, timeouts, error isolation
│   ├── wake_word.py          # Local offline "Hey Bravo" wake-word listener
│   ├── avatar.py             # 3D software avatar rendering & lighting engine
│   ├── avatar_mesh.py        # Facial mesh geometry and rigging calculation
│   ├── viseme.py             # Phoneme/viseme synchronization for facial movement
│   ├── echo.py               # Self-echo cancellation guard
│   ├── undo.py               # Universal action undo manager
│   ├── confirm.py            # Safety gate for irreversible system operations
│   └── audio_devices.py      # Audio endpoint discovery, testing, and selection
│
├── config/
│   ├── api_keys.example.json # Safe configuration template
│   ├── api_keys.json         # Local credentials (git-ignored)
│   ├── protocols.json        # User-customized Stark Protocol macros
│   └── certs/                # Self-signed TLS pair for LAN dashboard (git-ignored)
│
└── memory/
    ├── memory_manager.py     # Persistent memory coordinator
    └── long_term.json        # Local factual memory store (git-ignored)
```

---

## 🔒 Security & Privacy

- **100% Local Execution**: All action handlers, desktop operations, memory logs, and hardware telemetry run exclusively on your machine.
- **Zero Third-Party Telemetry**: There are no tracking scripts, analytics engines, or external cloud relays.
- **Git Protection**: Your private API key, local network TLS certs, and memory database are strictly ignored via `.gitignore` to prevent accidental commits.
- **Physical Confirmation Gates**: Critical power and network toggles require physical mouse-clicks on the HUD before execution.

---

## 🎓 Academic & Team Collaboration

This project is structured for academic group collaboration and modular development:

### Contribution Workflow
1. **Pull Latest Main**:
   ```bash
   git pull origin main
   ```
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit & Push**:
   ```bash
   git add .
   git commit -m "feat: implement custom telemetry graph"
   git push origin feature/your-feature-name
   ```
4. **Open a Pull Request**: Submit a Pull Request on GitHub for peer review before merging into `main`.

---

## 📄 License
This project is open-source and distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.
