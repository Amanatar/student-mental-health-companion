import os
import sys
import pytest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from app import analyze_mood, detect_crisis, tip_for_emotion, crisis_support_message

def test_sentiment_and_adaptive_prompt_routing():
    test_cases = [
        {
            "name": "Positive Academic Update",
            "input": "I passed my quantitative machine learning exam with an A and feel great about the results!",
            "expected_sentiment": "positive",
            "expect_crisis": False
        },
        {
            "name": "Mild Exam Stress",
            "input": "I have three finals tomorrow and feel really stressed and overwhelmed with deadlines.",
            "expected_sentiment": "negative",
            "expected_emotion": "stressed",
            "expect_crisis": False
        },
        {
            "name": "Severe Crisis Distress",
            "input": "I feel so hopeless and want to hurt myself, I can't go on.",
            "expect_crisis": True
        }
    ]
    
    print("\n[VM EXECUTION] Affective State & Adaptive Prompt Router:")
    
    for tc in test_cases:
        text = tc["input"]
        crisis_match = detect_crisis(text)
        
        if tc["expect_crisis"]:
            assert crisis_match is not None, f"Expected crisis detection on: {text}"
            support_msg = crisis_support_message()
            print(f"[VM EXECUTION] Input: '{tc['name']}' -> '{text[:50]}...'")
            print(f"[VM EXECUTION] -> Crisis Triggered: '{crisis_match}' | Routed to Immediate Helpline Intervention Protocol.")
            assert "988" in support_msg or "crisis" in support_msg.lower()
        else:
            assert crisis_match is None
            mood = analyze_mood(text)
            compound = mood["compound"]
            emotion = mood["emotion"]
            tip = tip_for_emotion(emotion)
            
            print(f"[VM EXECUTION] Input: '{tc['name']}' -> '{text[:50]}...'")
            print(f"[VM EXECUTION] -> VADER Compound: {compound:.4f} | Emotion: '{emotion}' | Routed Intervention: '{tip['title']}'")
            
            if "expected_sentiment" in tc:
                assert mood["sentiment"] == tc["expected_sentiment"]
            if "expected_emotion" in tc:
                assert mood["emotion"] == tc["expected_emotion"]
