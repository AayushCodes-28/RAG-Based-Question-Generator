import json
from app.models.domain_map import VALID_CODES

def validate_output(raw):
    try:
        data = json.loads(raw)
    except:
        return None

    if "question" not in data:
        return None

    if not data["question"].endswith("."):
        return None

    if "?" in data["question"]:
        return None

    if data.get("difficulty") not in [0,1,2,3,4]:
        return None

    if "domains" not in data:
        return None

    if any(d not in VALID_CODES for d in data["domains"]):
        return None

    return data
