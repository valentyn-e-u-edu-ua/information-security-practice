import bleach


def sanitize_text(text: str) -> str:
    """Видаляє всі HTML-теги і екранує спецсимволи."""
    return bleach.clean(text, tags=[], attributes={}, strip=True).strip()