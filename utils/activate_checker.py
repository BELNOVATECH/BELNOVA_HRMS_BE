def is_active_name(name: str) -> bool:
    """
    Used for job positions.
    Returns True if the job title contains valid keywords.
    """
    name = name.lower().strip()
    valid_keywords = ["developer", "engineer", "hr", "it", "manager", "admin"]
    return any(word in name for word in valid_keywords)


def is_valid_name(name: str) -> bool:
    """
    Used for department names.
    Automatically sets department active or not.
    """
    name = name.lower().strip()
    valid_dept_keywords = ["finance", "sales", "marketing", "hr", "it", "support"]
    return any(word in name for word in valid_dept_keywords)
