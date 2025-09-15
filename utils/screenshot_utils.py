# utils/screenshot_utils.py
import os
from datetime import datetime
from pathlib import Path

def capture_screenshot(browser, test_name, status="passed"):
    """Capture screenshot and save to evidence folder"""
    evidence_dir = Path("evidence") / datetime.now().strftime("%Y-%m-%d")
    evidence_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%H-%M-%S")
    filename = f"{status}_{test_name}_{timestamp}.png"
    filepath = evidence_dir / filename
    
    browser.save_screenshot(str(filepath))
    return filepath