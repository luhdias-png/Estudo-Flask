from estudo import app, database
from flask import render_template, url_for, request
from estudo.models import Contato

# A função url_for tem como objetivo gerar URLs dinamicamente com base no nome da função da rota define uma rota para a URL principal ('/')
@app.route('/')
def homepage():
    usuario = "mandary master ronaldo"
    idade = 31

    context = {
        'usuario': usuario,'idade':idade,
    }
    return render_template('index.html', context=context)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/contatos', methods = ['GET','POST'])
def contatos():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        print('GET:',pesquisa)
        context.update({'pesquisa': pesquisa})
    if request.method =='POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        msg = request.form['msg']

        contato = Contato(
        nome = nome,
        email = email,
        assunto = assunto,
        msg = msg
        )
        database.session.add(contato)
        database.session.commit()
    return render_template('contatos.html', context=context)