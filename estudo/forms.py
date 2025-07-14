from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

from estudo import database
from estudo.models import Contato

class ContatoForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])#StringField = Literalmente campo de caracteristicas ou seja precisa de informacoes do usuario para enviar.
    email = StringField("Email", validators=[DataRequired(), Email()])
    assunto = StringField("Assunto", validators=[DataRequired()])
    msg = TextAreaField("Msg", validators=[DataRequired()])
    btn_enviar = SubmitField("Enviar")#SubmitFild = Literalmente campo de ENVIO como um botao para enviar algo.

    def save(self):
        contato = Contato(
            nome = self.nome.data,
            email = self.email.data,
            assunto = self.assunto.data,
            msg = self.msg.data
        )
        database.session.add(contato)
        database.session.commit()