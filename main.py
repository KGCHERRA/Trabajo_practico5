from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import uuid

app = FastAPI(
    title="Trabajo_práctico5",
    version="0.0.1"
)

users = {
    "Hola1234": {
        "username": "person1",
        "name": "gabriela"
    },
    "Hola5678": {
        "username": "person2",
        "name": "sophia"
    },
}

# 1. Registro de Usuarios:

@app.post("/api/v1/register")
async def register_user(username: str, email: str, password: str):
    user_id = str(uuid.uuid4())
    users[user_id] = {
        "username": username,
        "email": email,
        "password": password,
        "Status_code": 201
    }

# 2. Obtener Datos de Usuario:

@app.get("/user/{user_id}")
async def get_user(user_id: str):
    user = users.get(user_id)
    if user:
        return JSONResponse(
            content=user,
            status_code=status.HTTP_200_OK
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Este usuario no existe."
        )


# 3. Crear Tareas:


# 4. Listar Tareas por Usuario:

