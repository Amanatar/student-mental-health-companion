# Student Mental Health Companion

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
