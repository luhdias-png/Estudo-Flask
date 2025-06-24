from estudo import app

from flask import render_template, url_for

# A função url_for tem como objetivo gerar URLs dinamicamente com base no nome da função da rota define uma rota para a URL principal ('/')
@app.route('/')
def homepage():
    usuario = "mandary master ronaldo"
    idade = 31

    context = {
        'usuario': usuario,'idade':idade,
    }
    return render_template('index.html', context=context)

@app.route('/contatos')
def cadastro():
    return 'É a ambulancia besta!'