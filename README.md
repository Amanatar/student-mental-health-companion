# Student Mental Health Companion

<div align="center">

[![CI Verified](https://github.com/Amanatar/student-mental-health-companion/actions/workflows/ci-verify.yml/badge.svg)](https://github.com/Amanatar/student-mental-health-companion/actions)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Gemini API](https://img.shields.io/badge/Gemini_API-8E75C2?logo=google-gemini&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

Context-aware affective computing and supportive dialogue assistant designed for university students navigating academic stress, anxiety, and burnout.

## System Architecture

- **Affective State Classification:** Real-time sentiment scoring using VADER combined with a domain-specific lexicon covering 8 emotional states (anxiety, stress, sadness, loneliness, anger, frustration, fatigue, guilt).
- **Dual-Mode Response Generation:**
  - *LLM Tier:* Structured empathetic grounding via Google Gemini API with safety guardrails.
  - *Offline Deterministic Tier:* Context-specific psychoeducation, breathing exercises, cognitive reframing prompts, and crisis hotline signposting if offline or unauthenticated.
- **Privacy First:** Ephemeral session state with zero external telemetry storage by default.

## Interface

Built with Streamlit for clean, responsive interaction across desktop and mobile devices.

## Setup & Running

```bash
git clone https://github.com/Amanatar/student-mental-health-companion.git
cd student-mental-health-companion
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
