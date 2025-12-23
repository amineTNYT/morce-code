
# Morse Code Translator with Sound 🔊

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A feature-rich Python Morse code translator with text-to-sound conversion, interactive learning mode, and comprehensive translation capabilities.

![Demo GIF](docs/demo.gif) <!-- Add a demo gif later -->

## ✨ Features

### 🎯 Core Features
- **Text ↔ Morse Translation** - Bidirectional conversion with full punctuation support
- **Audio Playback** - Hear Morse code with realistic timing and tones
- **Interactive Learning** - Practice mode with quizzes and statistics
- **File Support** - Save and load translations

### 🔧 Technical Features
- **Cross-platform** - Works on Windows, macOS, and Linux
- **Multiple Sound Backends** - Uses winsound (Windows) or simpleaudio (cross-platform)
- **No GUI Dependencies** - Runs in terminal, easy to integrate
- **Extensible** - Clean architecture for adding new features

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- For sound on non-Windows systems: `simpleaudio`

### Quick Install
```bash
# Clone the repository
git clone https://github.com/amineTNYT/morse-code.git
cd morse-code-translator

# Install dependencies (optional for sound)
pip install -r requirements.txt
