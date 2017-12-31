
"""
Este modulo possui as classes referente aos dados utilizados no mini-projeto.

As operaçoes realzadas por estas classes fazem alteracoes no banco de dados por meio do
modulo

As classes desse modulo sao:
    -- User
    -- Account
    -- History
    -- Money
    -- Agency
"""

from decimal import Decimal

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
            self.balance = Money(balance)
            self.history = []
            Account.accountId += 1
            Account.accountQnt += 1

    def __str__(self): pass


    def delete(self):
        # TODO deletar a conta no banco de dados
        if self.balance.value == 0.0:
            # Deletar conta
            return True
        else:
            # Caso saldo seja positivo, sacar ou transferir. Caso negativo, exigir deposito.
            return False


class Money:

    """
    Adapta um valor decimal para o sistema bancario/monetario. Com fins de formatacao e
    gerenciamento de cedulas.
    """

    # TODO decidir como organizar as celulas no dicionario
    banknotes = {}

    def __init__(self, value):
        self.value = value

    def __str__(self):
        sign = '-' if self.value < 0.0 else ''
        pos = abs(self.value)
        whole = Money.commas(int(pos))
        fract = ("{0:.2f}".format(pos))[-2:]
        result = "{0}{1}.{2}".format(sign, whole, fract)
        return result

    def commas(self):
        digits = str(self.value)
        assert (digits.isdigit())
        result = ''
        while digits:
            digits, last = digits[:-3], digits[-3:]
            result += (last + ',' + result) if result else last
        return result

    commas = staticmethod(commas)

    def getOptions(self): pass
