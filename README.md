# VTC – Visual Time-domain Composer

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-green)
![License](https://img.shields.io/badge/license-MIT-orange)

**VTC (Visual Time-domain Composer)** is a feature-rich, interactive signal and waveform generator built with Python, PyQt5, and Matplotlib. It allows users to synthesize, visualize, and analyze various complex waveforms in real-time with customizable dynamic layouts and instant parameter tuning.

---

## 🌟 Key Features

- **Side-by-Side Responsive Layout**:
  - Control Panel (30% width) and Waveform Viewer Canvas (70% width) via an interactive splitter.
  - Full-screen support (Maximize) and dynamic cursor resizing.
- **Comprehensive Waveform Variations**:
  - Sinusoidal
  - Square Wave
  - Sawtooth Wave
  - Triangle Wave
  - Damped Sine
  - Chirp (Frequency Sweep)
  - Gaussian Pulse
  - White Noise
- **Real-Time Interactive Updates**:
  - Automatically updates plots in real-time as parameters (Frequency, Amplitude, Phase, DC Offset, Duty Cycle, Damping, Sample Rate, Duration) are adjusted.
- **Flexible Display Layouts (Split-View Canvas)**:
  - **1 Layout (Overlay)**: Superimpose all generated waveforms for direct comparison.
  - **1 Layout (Single)**: Focus on an individual waveform.
  - **2 Subplot Layout**: Compare two distinct signals vertically.
  - **4 Subplot Layout (2x2 Grid)**: Observe primary waveforms side-by-side.
  - **Multi-Subplot**: Stack all waveform variations independently.
- **Multilingual Support (5 Languages)**:
  - English (Default)
  - Bahasa Indonesia
  - Traditional Chinese (繁體中文)
  - Simplified Chinese (简体中文)
  - Japanese (日本語)
- **Data & Visual Export**:
  - Export figures to high-resolution **PNG** or **JPG/JPEG** (300 DPI).
  - Export raw time-series data to **CSV** format for further analysis in MATLAB, Excel, or Python.

---

## 🛠️ Requirements & Installation

### Prerequisites
Make sure you have **Python 3.8** or higher installed on your system.

### Install Dependencies
Clone the repository and install the required Python packages:

git clone https://github.com/your-username/vtc.git
cd vtc
pip install PyQt5 matplotlib numpy pandas

---

## 🚀 How to Run

Execute the main script from your terminal:

python vtc.py

---

## 🎛️ Parameters Overview

| Parameter | Description |
| :--- | :--- |
| **Frequency** | Sets the oscillation frequency (Hz) |
| **Amplitude** | Sets the peak amplitude level |
| **Phase** | Adjusts signal phase offset in degrees (°) |
| **DC Offset** | Shifts the vertical baseline of the waveform |
| **Duty Cycle** | Adjusts high-state ratio for Square and Triangle waves (1% - 99%) |
| **Damping Factor** | Controls decay rate for Damped Sine waves |
| **Duration** | Defines total observation time window (s) |
| **Sample Rate** | Sets sampling frequency (Hz) for discretization |

---

## 💾 Export Formats

1. **Image Export (`.png`, `.jpg`)**: Saves the active canvas figure suitable for publication or presentation.
2. **CSV Export (`.csv`)**: Contains the discrete `Time_s` vector alongside amplitude data for all active waveforms.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
