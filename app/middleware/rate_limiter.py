from slowapi import Limiter
from slowapi.util import get_remote_address

# Обмеження рахуються за IP-адресою клієнта
limiter = Limiter(key_func=get_remote_address)