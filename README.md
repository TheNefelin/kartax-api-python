# Kartax Api Python 3.12.3

### Deploy and run App
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
```sh
.venv\Scripts\activate
source .venv/bin/activate  
python3 run.py
```

### Check Python Version & Installed Packages
```sh
python3 --version
python3 -m pip list
python3 -m venv .venv
.venv\Scripts\activate      # windows
source .venv/bin/activate   # linux
```

### Install Dependencies
```sh
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv pydantic pydantic-settings
pip install pillow python-multipart # Manejo de archivos / uploads
pip install cloudinary # Cloud storage
pip install google-auth google-auth-oauthlib google-auth-httplib2 # Google
pip install python-jose[cryptography] # JWT
pip install pydantic[email] # Extras opcionales de Pydantic
```
```sh
pip freeze > requirements.txt
```

## Structure
```
project
│
├─ src/
│   ├─ api/
│   │   ├─ categories/
│   │   │   ├─ dto.py
│   │   │   ├─ models.py
│   │   │   ├─ repository.py
│   │   │   ├─ routes.py
│   │   │   └─ service.py
│   │   ├─ groups/
│   │   │   ├─ dto.py
│   │   │   ├─ models.py
│   │   │   ├─ repository.py
│   │   │   └─ routes.py
│   │   ├─ mobile/
│   │   │   ├─ dto.py
│   │   │   ├─ repository.py
│   │   │   └─ routes.py
│   │   └─ products/
│   │       ├─ dto.py
│   │       ├─ models.py
│   │       ├─ repository.py
│   │       └─ routes.py
│   │
│   ├─ core/
│   │   ├─ config.py
│   │   └─ database.py
│   │
│   ├─ services/
│   │   └─ cloudinary_service.py
│   │
│   ├─ shared/
│   │   └─ dtos.py
│   │
│   └─ main.py
│
├─ LICENSE.txt
├─ README.md
├─ requirements.txt
└─ run.py
```

