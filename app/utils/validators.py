# Add any custom validators here.
def validate_color_code(color_code: str) -> bool:
    if not color_code.startswith("#") or len(color_code) not in (4, 7):
        return False
    return True
