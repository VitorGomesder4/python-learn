print("\nExemplo de encapsulamento:")

class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo        
    
conta = ContaBancaria(saldo = 50)
print(f"\nSaldo da conta bancária: {conta.consultar_saldo()}\n")

conta.depositar(valor = 500)
print(f"\nSaldo da conta bancária: {conta.consultar_saldo()}\n")

conta.sacar(valor = 500)
print(f"\nSaldo da conta bancária: {conta.consultar_saldo()}\n")