from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date

app = FastAPI()

userDB = {}

class Usuario(BaseModel):
    cpf: int
    nome: str
    data_nascimento: date



@app.get('/')
def home():
    if len(userDB) > 0:
        return userDB
    else:
        return HTTPException(status_code=404, detail="Usuário não encontrado!")


@app.post('/add_user/')
def add_user(usuario: Usuario, cpf: int, nome: str, data_nascimento: date):
    if cpf in userDB:
        return HTTPException(status_code=400, detail='Usuário já existe')
    
    usuario.cpf = cpf
    usuario.nome = nome
    usuario.data_nascimento = data_nascimento

    userDB[cpf] = usuario.model_dump()

    return {'mensagem': 'Usuário cadastrado com sucesso!', 'informações': usuario.model_dump()}