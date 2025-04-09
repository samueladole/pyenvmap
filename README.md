# pyenvmap

A schema-based environment variable loader for Python.  
Type-safe, validated, and plug-and-play.  
Define your config once — get clean, typed access to environment variables with zero boilerplate.

---

**pyenvmap** is a lightweight Python library for loading and validating environment variables using a schema-first approach.

### ✅ Features
- 🧾 Schema-based config via class annotations
- 🔒 Type-safe loading: `int`, `bool`, `list[str]`, etc.
- ⚠️ Validation for required fields
- 🧪 Dotenv support
- 🧼 Clean, zero-boilerplate interface

### 📦 Example

```python
from pyenvmap import EnvConfig

class Settings(EnvConfig):
    DEBUG: bool = False
    PORT: int
    SECRET_KEY: str
    ALLOWED_HOSTS: list[str] = []

settings = Settings.load()

print(settings.PORT)
