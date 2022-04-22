"""
Arquivo de classes da aplicação:
- Classe Atividade:
    >> Nome da atividade
    >> Data e Hora
    >> Descrição da atividade

- Classe Usuario:
    >> Nome
    >> Email
    >> Senha
"""


class Atividade:
    def __init__(self, atividade, data, hora, descricao):
        self.atividade = atividade
        self.data = data
        self.hora = hora
        self.descricao = descricao


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
