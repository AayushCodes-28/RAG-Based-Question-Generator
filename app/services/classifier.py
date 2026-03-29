from app.models.domain_map import VALID_CODES

def classify_domains_and_difficulty(domains, difficulty):
    valid_domains = [d for d in domains if d in VALID_CODES]
    difficulty = max(0, min(4, difficulty))
    return valid_domains, difficulty
