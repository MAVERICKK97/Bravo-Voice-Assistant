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
3. [Comprehensive Capabilities List](#-comprehensive-capabilities-list)
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
15. [Author & Lead Developer](#-author--lead-developer)

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

## 🚀 Comprehensive Capabilities List

Bravo Voice Assistant features an extensive suite of over 50 built-in capabilities spanning real-time audio, software 3D rendering, deep operating system automation, and multimodal intelligence:

### 🎙️ 1. Audio, 3D Holographic Avatar & HUD Presence
| Capability | Description |
|---|---|
| 🧑‍🎤 Holographic 3D Avatar | Real-time animated 3D human head rendered entirely in software via `QPainter` (no GPU or 3D engine required) |
| 👄 Real-Time Lip-Sync | Viseme synthesis (~50 shapes/second) derived from audio formants and live speech transcripts |
| 🌍 Language-Free Articulation | Universal Unicode mouth mapping covering Latin, Cyrillic, and Greek phonemes |
| 🙂 Natural Facial Acting | Phrase-tracking brows, gaze saccades, natural blinking, and subtle nod gestures on stressed syllables |
| 😐 Face as Status Indicator | Looks away while thinking, meets user gaze when listening, lids lower in sleep mode, glances down at loaded files |
| 🎚️ Global Push-to-Talk | Hold **Ctrl+Space** anywhere across the operating system to immediately open the microphone |
| 🔇 Self-Echo Cancellation Guard | Distinguishes user speech from the assistant's own audio output, preventing feedback loops |
| 🎙️ Offline Wake Word | Fully local **"Hey Bravo"** wake-word detection engine; runs offline on an isolated thread |
| 💤 Intelligent Sleep Mode | Automatically enters power-saving sleep after 2 minutes of silence; never streams audio while asleep |
| ⚡ Instant Acknowledgment | Speaks an immediate, context-aware acknowledgement while longer background tasks execute |
| 🚀 Gemini Live WebSocket | Sub-second full-duplex conversational audio streaming directly with Gemini Live |
| 🎙️ Dynamic Voice Switcher | Switch between 5 native Gemini voices on the fly from the HUD without restarting |
| 〰️ Reactive Audio Waveform | Dynamic waveform visualization pulsing to real-time audio amplitudes for both user and assistant |
| 🎧 Audio Endpoint Resolver | Scans, deduplicates, and validates system microphones and speakers across MME, DirectSound, and WASAPI |
| 🔗 Session Continuity | Retains conversation context and history across temporary network drops and device re-plugs |

### 🖥️ 2. Operating System, Desktop & Hardware Automation
| Capability | Description |
|---|---|
| ⚡ Stark Protocols | One-phrase multi-task macro engine ("Stealth", "Focus", "Overclock", "Clean Slate", "Night", "Audit") |
| 📂 Full Multi-Drive File Control | Deep read, write, create, copy, move, and delete permissions across all drives (`C:` and `D:`) |
| 🧹 Desktop Auto-Organizer | Categorizes desktop clutter into clean directories (Documents, Images, Code, Archives) |
| ↩️ Universal Undo Engine | Safely reverses file operations, folder creations, and system settings modifications on voice command |
| ⚠️ Human Confirmation Gate | Hardware-level UI confirmation dialog for critical actions (shutdown, restart, WiFi disable) |
| 🖥️ Hardware Mixers | Voice control over master volume, mute states, display brightness, and dark mode toggles |
| 🔌 Power State Management | Workstation locking, screen sleeping, system reboots, and scheduled shutdowns |
| 🚀 Native Application Launcher | Launches, focuses, minimizes, and terminates desktop applications via flexible name matching |
| 🌐 Voice Browser Automation | Opens URLs, navigates tabs, conducts search queries, and controls web sessions |
| 📊 Real-Time Hardware Telemetry | Continuous background monitoring of CPU, RAM, GPU, and thermal statistics with proactive alerts |
| ⌨️ Hybrid Voice & Keyboard Input | Seamlessly switch between voice dialogue and keyboard typing in the HUD command input |
| 📋 Clipboard Intelligence | Instant clipboard clearing, copying, translation, and text transformation |
| ⏰ Scheduled Notifications | System-native reminders using Windows Task Scheduler and OS notification hubs |
| 📨 Direct Messaging Integration | Voice-driven message composition and dispatch via WhatsApp and web endpoints |
| ⚡ Auto-Start on System Boot | Registers with OS startup management (Windows Registry / macOS LaunchAgents) |

### 👁️ 3. Multimodal Vision, Media & Web Intelligence
| Capability | Description |
|---|---|
| 👁️ Live Screen Analysis | Real-time multi-monitor screen capture analyzed directly by Gemini for debugging, reading, and assistance |
| 📹 Live Webcam Vision | Webcam video stream ingestion for real-world object recognition, spatial awareness, and visual Q&A |
| 📄 Document Intelligence | Deep reading, semantic analysis, and summarization of local PDFs, text files, and code repositories |
| 📺 Embedded HUD Video Player | Plays YouTube streams, direct media URLs, or local MP4 files directly within the central HUD avatar space |
| 🔇 Smart Media Ducking | Automatically ducks playback volume and mutes the microphone while video audio plays |
| 🔍 Multi-Mode Web Search | Grounded live web search supporting modes: `news`, `research`, `price`, `compare`, and `search` |
| 🌤️ Live Weather Reports | Real-time meteorological data and weather forecasts for your city |
| 🗺️ Dynamic Content Panel | Scrollable display layer beneath the HUD rendering structured web results, tables, and search data |

### 🧠 4. Memory Engine, Resilience & Customization
| Capability | Description |
|---|---|
| 🪜 9-Model Fallback Ladder | Automated failover hierarchy with cooldowns ensuring 100% uptime through rate limits or API outages |
| 🧠 Hybrid Persistent Memory | Zero-token bloat architecture combining lightweight prompt context with local vectorless search |
| 👁️ GUI Memory Panel | Dedicated HUD drawer allowing inspection, editing, and deletion of stored facts |
| 🌅 Morning Briefing Engine | Greets on boot, recaps previous conversations, announces time, and summarizes live morning news |
| 🔔 Proactive Check-ins | Context-aware reminders and check-ins based on time of day, active projects, and past topics |
| 📱 Mobile LAN Remote Dashboard | QR-code paired local HTTPS web dashboard for mobile control, text input, and telemetry |
| 🎨 Dynamic HUD Theming | Real-time hue wheel and hex color picker that dynamically recolors the entire HUD and 3D avatar |
| 🧩 Modular Plugin System | Drop-in `.py` plugins auto-discovered at runtime with crash isolation and zero configuration |
| 🪪 Runtime Self-Knowledge | Automatically introspects its own active plugins, system hardware, OS type, and installed tools |

---

### 🏛️ Core Architectural Highlights

- **3D Software Vector Projection**: Uses 3D geometry from a 468-vertex facial mesh rendered cleanly via Qt's 2D vector graphics pipeline (`QPainter`). Zero GPU requirement.
- **Universal Action Reversal (Undo Engine)**: Say *"undo"* in plain language to restore modified file contents, reverse file moves, or revert setting changes.
- **Human-in-the-Loop Confirmation Gate**: Irreversible operations (system shutdowns, restarts, network toggles) trigger an unforgeable physical confirmation dialog on the HUD.
- **Local Wake Word & Push-to-Talk**: Combines an offline "Hey Bravo" local listener with a global **Ctrl+Space** keyboard shortcut.

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

## 👨‍💻 Author & Lead Developer

- **Shrijay Talap** ([@MAVERICKK97](https://github.com/MAVERICKK97))
  - **GitHub:** [https://github.com/MAVERICKK97](https://github.com/MAVERICKK97)
  - **Project Repository:** [Bravo-Voice-Assistant](https://github.com/MAVERICKK97/Bravo-Voice-Assistant)
  - **Role:** Lead Architect & Developer (System Architecture, Gemini Live Integration, 3D Holographic HUD & OS Automation)

## Frontend Development

- **Samiksha Ramesh Ghure**
  - **Role:** Frontend Developer
  - **Responsibilities:** PyQt6 Desktop User Interface, Holographic HUD Interface Design, Dashboard Components & Layout, Activity Logs and UI Overlays, Frontend Integration with Core Modules

---

## 📄 License
This project is open-source and distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.
