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


#3. Crear Tareas:
@app.post("/api/v1/tasks/create")
async def create_task(user_id: int, task: Task):
    if user_id < 0 or user_id >= len(usuarios_registrados):
        raise HTTPException(status_code=404, detail="No se encontró al usuario")
    if user_id not in tareas_usuario:
        tareas_usuario[user_id] = []

    tareas_usuario[user_id].append(task)
    return {"message": "Tarea creada correctamente"}
