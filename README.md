# Заочна практична робота №1: Захищений REST API «Електронний деканат»

**Виконав:** Кудін Валентин Валентинович  
**Курс / група:** 3 курс, 233
**Дисципліна:** Безпека інформаційних систем  

---

## 1. Опис проєкту
REST API системи «Електронний деканат» із реалізацією багаторівневої концепції глибокоешелонованого захисту (**Defense in Depth**):
- Ізольоване контейнерне середовище Docker Compose з персистентною базою даних SQLite та міграціями Alembic.
- Модель контролю доступу **RBAC** (Користувач → Роль → Дозвіл) за принципом найменших привілеїв (PoLP).
- Безпечне збереження паролів алгоритмом **bcrypt** (cost factor 12) із захистом від Username Enumeration.
- Токенна аутентифікація та авторизація на базі **JWT (HS256)** з розділенням access (30 хв) та refresh (7 днів) токенів.
- Захист веб-рівня: HTTP Security Headers (CSP, HSTS, X-Frame-Options, nosniff), обмеження CORS, Rate Limiting (slowapi) та санітизація вхідних даних (bleach) проти Stored XSS.

---

## 2. Швидкий запуск

1. Склонувати репозиторій:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/information-security-practice.git](https://github.com/YOUR_USERNAME/information-security-practice.git)
   cd information-security-practice