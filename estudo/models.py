from estudo import database
from datetime import datetime

class Contato(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    data_envio = database.Column(database.DateTime, default=datetime.utcnow())
    nome = database.Column(database.String, nullable=True )
    email = database.Column(database.String, nullable=True)
    assunto = database.Column(database.String, nullable=True)
    msg = database.Column(database.String, nullable=True) 
    check = database.Column(database.Integer, default=0)

#Quando desejar alterar ou adicionar algo no banco de dados no terminal digita: flask db migrate -m "fiz uma alteração"
#salvar no banco de dados (terminal): flask db upgrade