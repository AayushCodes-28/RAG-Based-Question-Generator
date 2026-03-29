from app.utils.difficulty_rubric import RUBRIC
from app.services.safe_gemini import safe_gemini_call

MODEL = "gemini-1.5-pro"

def generate_question(domains, difficulty, context):
    system_prompt = f"""
You are a technical interview question generator.

RULES:
1. Generate only ONE question.
2. The question must NOT contain numbers like 1. or Q1.
3. The question must NOT contain a question mark (?).
4. The question MUST end with a period (.).
5. Difficulty MUST be an integer from 0 to 4.
6. Domains MUST be valid shorthand codes: {domains}

{RUBRIC}

Context from RAG:
{context}
"""

    user_prompt = f"""
Generate JSON exactly:
{{
  "question": "...",
  "difficulty": {difficulty},
  "domains": {domains}
}}
"""

    response = safe_gemini_call(
        model=MODEL,
        parts=[system_prompt, user_prompt]
    )

    return response.text
