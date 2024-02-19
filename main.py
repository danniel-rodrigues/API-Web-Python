from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

userDB = {}

class Usuario(BaseModel):
    cpf: int
    nome: str
    data_nascimento: str



@app.get('/')
def home():
    if len(userDB) > 0:
        return userDB
    else:
        return HTTPException(status_code=404, detail="Nenhum usuário encontrado!")


@app.post('/add_user/')
def add_user(usuario: Usuario, cpf: int, nome: str, data_nascimento: str):
    if cpf in userDB:
        return HTTPException(status_code=400, detail='Usuário já existe')
    
    usuario.cpf = cpf
    usuario.nome = nome
    usuario.data_nascimento = (datetime.strptime(data_nascimento, '%d/%m/%Y')).strftime('%d/%m/%Y')

    userDB[cpf] = usuario.model_dump()

    return {'mensagem': 'Usuário cadastrado com sucesso!', 'informações': usuario.model_dump()}