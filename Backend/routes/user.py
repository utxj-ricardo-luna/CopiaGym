from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from config.db import conn
from models.users import users
from models import tb_users

user = APIRouter()
users = []

#usersModel
class model_user(BaseModel):
    id:str
    usuario:str
    contrasena: str
    created_at:datetime = datetime.now()
    estatus:bool=False

@user.get('/')

def bienvenida():
    return "Bienvenido al sistema de apis"

@user.get('/users', tags=["Usuarios"])

def get_usuarios():
    return users
@user.get('/users_all', tags=["Usuarios"])

def get_usuarios_all():
    return conn.execute(tb_users.select()).fecthall()

@user.get('/users_all', tags=["Usuarios"])

def get_usuarios_all():
    return conn.execute(users.select()).fetchall()

@user.post('/users', tags=["Usuarios"])

def save_usuarios(insert_users:model_user):
    users.append(insert_users)
    print (insert_users)
    return "Datos guardados"

@user.post('/user/{user_id}', tags=["Usuarios"])

def get_usuario(user_id: str):
    for user in users:
        if user.id== user_id:
            return user
    return "No existe el registro"

@user.delete('/user/{user_id}', tags=["Usuarios"])

def delete_usuario(user_id: str):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return "Registro eliminado correctamente"
    return "Registro no encontrado"

@user.put('/user/{user_id}', tags=["Usuarios"])

def update_usuario(user_id: str, updateUser: model_user):
    for user in users:
        if user.id == user_id:
            user.usuario=updateUser.usuario
            user.contrasena=updateUser.contrasena
            user.estatus=updateUser.estatus
            return "Registro actualizado correctamente"
    return "Registro no encontrado"