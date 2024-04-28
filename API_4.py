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


class Task(BaseModel):
    title: str
    description: str
    status: str


usuarios_registrados = []
tareas_usuario = {}


#4. Listar Tareas por Usuario:
@app.get("/api/v1/tasks/{user_id}")
async def get_tasks_by_user(user_id: int):
    if user_id < 0 or user_id >= len(usuarios_registrados):
        raise HTTPException(status_code=404, detail="No se encontró al usuario")

    if user_id not in tareas_usuario or len(tareas_usuario[user_id]) == 0:
        raise HTTPException(status_code=404, detail="No se encontraron tareas para este usuario")

    return tareas_usuario[user_id]