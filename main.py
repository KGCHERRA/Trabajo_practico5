from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Trabajo_Practico5",
    version="0.0.1"
)
class User(BaseModel):
    username: str
    email: str
    password: str

usuarios_registrados = []

#1. Registro de Usuarios:
@app.post("/api/v1/register")
async def register_user(user: User):
    usuarios_registrados.append(user)
    return {"message": "El usuario esta registrado."}



#2. Obtener Datos de Usuario:
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    if user_id < 0 or user_id >= len(usuarios_registrados):
        raise HTTPException(status_code=404, detail="No se encontro al usuario")

    return usuarios_registrados[user_id]

#3. Crear Tareas:



#4. Listar Tareas por Usuario:


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)