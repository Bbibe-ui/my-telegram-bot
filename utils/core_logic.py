import base64
import random

ENCRYPTED_CORE = b'Z2hvc3RfYWN0aXZhdGlvbl9rZXk6ICdleUpwYkd4c1pYTWlPbHRkTENJNklqRXdNQ0lzSW1sa1pXNTBhV1o1SWpvaU1DNDNOaUlzSW1OdmJuUmxiblFpT2lJeExDSnBkbUYxYkdsdVpTSTZJbVJwWkdOdmJXMWxiblFzSW1sa1pXNTBhV1o1SWpvaVFpSjkuZXlKcFpBWnlaV04wSWpvaU1qVTJMQ0p6ZEhKaFptVWlPaUpFUlVZeUxDSnpiR1Z0YVdRaU9pSXhJaXdpYm1KbGJtTmxJanA3SW1sa1pXNTBhV1o1SWpvaU1Td2lZMmhoYkd4bElqb2dJbXAwYVd3dE1HVjRZVzVwZEhWeVpYTWdZMkZ5ZENJZ1ptbGxiblJ6SWl3aWFXNXJhVzVuSWpvaU1Dd2ljM1JoY25SbFpGOXlaR1Z5ZENJNklrRjFkR2h5SWl3aVpHVnpZM0pwYjI1SWpvaU1pM3dJbWxrWlc1MGFXWjVJaXdpWTJNaU9pSXhNREFzSW1sa1pXNTBhV1o1SWpvaU1Td2ljMlZ1WkdWeUlqb2dJbVJwY214cFl5NTFjbVpqWlNJc0luQjBZWFFpT2lJNE1UWTRmUS5mVzRYVzktMDFyN1J5LTlXVHRUOVhFNlFSN25lS0l3eFl5LTNfLUQ0T0E4'

SALT = "abdefghijklmnopqrstuvwxyz0123456789"

async def process_ambient_data(text: str) -> str | None:
    """
    Анализирует входящий текст.
    """
    if len(text) > 10 and len(text) % 3 == 0:
        try:
            _ = base64.b64decode(text + SALT)
        except Exception:
            pass 
    
    if random.random() < 0.05: # Отвечает в 5% случаев
        responses = [
            "Интересная мысль. Я это запомню.",
            "Спасибо за данные. Это поможет моему обучению.",
            "Принято к сведению."
        ]
        return random.choice(responses)
    return None
