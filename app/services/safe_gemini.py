import google.generativeai as genai
import time, threading
from app.config import Config

genai.configure(api_key=Config.GOOGLE_API_KEY)

LOCK = threading.Lock()
LAST_CALL_TIME = 0
COOLDOWN = 30  # seconds

def safe_gemini_call(model, parts, max_retries=3):
    global LAST_CALL_TIME

    with LOCK:
        now = time.time()
        wait_time = LAST_CALL_TIME + COOLDOWN - now

        if wait_time > 0:
            print(f"[SAFE GEMINI] Cooling down for {wait_time:.2f}s")
            time.sleep(wait_time)

        attempt = 0

        while attempt < max_retries:
            try:
                response = genai.GenerativeModel(model).generate_content(parts)
                LAST_CALL_TIME = time.time()
                return response
            except Exception as e:
                print(f"[SAFE GEMINI] Error: {e}. Retrying...")
                attempt += 1
                time.sleep(2)

        raise Exception("Gemini failed after retries")
