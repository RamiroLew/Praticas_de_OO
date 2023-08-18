class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto ... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        bancos = {
            'Banco do Brasil': '001',
            'Caixa Econômica Federal': '104',
            'Bradesco': '237',
            'Itaú Unibanco': '341',
            'Santander': '033',
            'HSBC Bank Brasil': '399',
            'Banco Safra': '422',
            'Banco Rural': '453',
            'Banco Mercantil do Brasil': '389',
            'Banco Cooperativo Sicredi': '748',
            'Bancoob (Banco Cooperativo do Brasil)': '756',
            'Banco Votorantim': '655',
            'Banco Original': '212',
            'Banco Inter': '077',
            'Banco Neon': '735',
            'Banrisul (Banco do Estado do Rio Grande do Sul)': '041',
            'Banco Pan (Banco Panamericano)': '623',
            'Banco Daycoval': '707',
            'BTG Pactual': '208',
            'Banco ABC Brasil': '246'
        }
        return bancos

