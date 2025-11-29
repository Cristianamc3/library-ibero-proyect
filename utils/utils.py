BACKGROUND_COLOR = "#F2F2F7"   # Soft gray/white background
BUTTON_COLOR = "#4A90E2"       # Soft blue
BUTTON_TEXT_COLOR = "white"
FONT_TITLE = ("Arial", 16, "bold")
FONT_NORMAL = ("Arial", 12)
FONT_SMALL = ("Arial", 10)
PADDING = 10


def validate_empty(fields: dict) -> tuple:
	"""
	Validate that the provided dictionary of fields are not empty.

	:param fields: dict mapping field display name -> value
	:return: (is_valid: bool, message: str)
	"""
	missing = [name for name, value in fields.items() if not str(value).strip()]
	if missing:
		if len(missing) == 1:
			return False, f"El campo '{missing[0]}' es obligatorio."
		else:
			return False, "Los siguientes campos son obligatorios: " + ", ".join(missing)
	return True, ""