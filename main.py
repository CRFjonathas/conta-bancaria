class Conta:
    def __init__(self, numero, nome_titular, cpf, saldo):
        self.numero = numero
        self.nome_titular = nome_titular
        self.cpf = cpf
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            return False
        else:
            self.saldo -= valor
            return True

    def gerar_extrato(self):
        print(f"""N° Conta: {self.numero}
Nome do titular: {self.nome_titular}
CPF: {self.cpf}
Saldo: R$ {self.saldo:,.2f}\n""")

    def transferencia(self, conta_destino, valor):
        if valor > self.saldo:
            print("Saldo Insuficiente.")
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            return ("Transfência realizadas.")

# Main

c1 = Conta(1, "Jonathas", 9707602562, 2300)
c2 = Conta(2, "Maria Cecilia", 7373792359, 25000)
c1.gerar_extrato()
c2.gerar_extrato()
c1.depositar(700)
valor_saque = 1000
resultado_saque = c1.sacar(valor_saque) # Verifica o resultado da função se é VERDADEIRO ou FALSO

if resultado_saque:
    print(f"Saque de R${valor_saque} realizado com sucesso.")
else:
    print(f"Saldo insuficiente.")

c1.gerar_extrato()

c1.transferencia(c2, 1300)

c1.gerar_extrato()
c2.gerar_extrato()