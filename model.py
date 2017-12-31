
"""
Este modulo possui as classes referente aos dados utilizados no mini-projeto.

As classes desse modulo sao:
    -- User
    -- Account
    -- History
    -- Agency
"""


class User:
    """
    Classe utilizada para guardar informaçoes pessoais de um usuario.
    Existe principalmente para evitar o acumulo de atividades na classe Account.

    Em um caso real, seria utilizado algum tipo de codificacao  para armazenar estas informacoes
    """
    def __init__(self, name, cpf, password):
        self.fullname = name
        self.cpf = cpf
        self.password = password

    def __str__(self):
        result = ""
        result += "Usuario: " + str(self.fullname) + "\n"
        return result

class Account:
    accountId = 0
    accountQnt = 0

    def __init__(self, user, agency_number, balance = 0.0):
        if user.__class__.__name__ != 'User':
            raise AttributeError
        else:
            self.agency_number = agency_number
            self.account_number = Account.accountId
            self.user = user
            self.balance = balance
            self.history = []
            Account.accountId += 1
            Account.accountQnt += 1

    def __str__(self): pass
