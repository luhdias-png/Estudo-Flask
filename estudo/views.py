from estudo import app, database
from flask import render_template, url_for, request, redirect
from estudo.models import Contato
from estudo.forms import ContatoForm

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
#---------------------------------------------------------------------------------------------------------------------------------------------
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))





    return render_template('contato.html', context=context, form=form)

#---------------------------------------------------------------------------------------------------------------------------------------------
@app.route('/contatos_old', methods = ['GET','POST'])
def contatos_old():
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
    return render_template('contatos_old.html', context=context)