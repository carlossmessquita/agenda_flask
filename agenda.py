from flask import Flask, render_template, request, redirect, url_for, session
from classes import Atividade, Usuario

# Instância de App Flask:
app = Flask(__name__)
app.secret_key = '2508'

lista = []


# Rotas da Aplicação - Sessão de Atividades:
@app.route('/')
def index():
    """ Página principal da aplicação, mostra as atividades cadastradas. """
    if session['usuario_logado'] == None:
        return redirect(url_for('login'))
    else:
        return render_template('index.html', titulo='Agenda', atividades=lista)


@app.route('/nova_atividade')
def nova_atividade():
    """ Rota para registro de nova atividade. """
    return render_template('atividade.html', titulo='Nova Atividade')


@app.route('/registrar', methods=['POST', ])
def registrar():
    """ Rota para formulário de registro de atividade. """
    atividade = request.form['atividade']
    data = request.form['data']
    hora = request.form['hora']
    descricao = request.form['descricao']
    registro = Atividade(atividade, data, hora, descricao)
    lista.append(registro)
    return redirect(url_for('index'))


# Rotas da Aplicação - Login e Usuário:
usuario = Usuario('Carlos', '', 'cvsm')

usuarios = {
    usuario.nome: usuario,
}


@app.route('/login')
def login():
    """ Rota para formulário de login. """
    return render_template('login.html')


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    """ Rota com a lógica de autenticação para login de usuário. """
    if request.form['nome'] in usuarios:
        user = usuarios[request.form['nome']]
        if request.form['senha'] == user.senha:
            session['usuario_logado'] = user.nome
            return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    """ Rota com a lógica pra logout de usuário. """
    session['usuario_logado'] = None
    return redirect(url_for('login'))


# Rodando aplicação:
app.run(debug=True)
