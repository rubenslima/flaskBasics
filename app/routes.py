from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    opcao ='Teste de parametro'
    dados = {'linha01':'Primeira linha','linha02':'Segunda linha'}
    return render_template('index.html', opcao=opcao, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')
