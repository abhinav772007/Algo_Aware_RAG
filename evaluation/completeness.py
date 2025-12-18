from evaluation.schema import REQUIRED_SECTIONS

def check_completeness(answer: str):
    missing = []
    for section in REQUIRED_SECTIONS:
        if section not in answer:
            missing.append(section)
    return {
        "missing_sections": missing,
        "is_complete": len(missing) == 0
    }
