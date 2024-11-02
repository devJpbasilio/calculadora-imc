class Pessoa:
    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def calculoDoImc(self):
        # Fórmula para calcular o Índice de Massa Corporal (IMC)
        return self.peso / (self.altura ** 2)

    def classificacaoDoImc(self):
        # Classificação do IMC de acordo com a OMS.
        imc = self.calculoDoImc()

        if imc < 18.5:
            return 'Abaixo do peso!'
        elif imc >= 18.5 and 24.9:
            return 'Peso adequado!'
        elif imc >= 25 and 29.9:
            return 'Sobrepeso!'
        elif imc >= 30 and 34.9:
            return 'Obesidade grau 1!'
        elif imc >= 35 and 39.9:
            return 'Obesidade grau 2!'
        else:
            return 'Obesidade grau 3!'

print('**** CALCULADORA IMC ****')
print('')
nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura(em metros): '))
peso = float(input('Digite seu peso: '))

pessoa = Pessoa(nome, altura, peso)
imc = pessoa.calculoDoImc()
classificacao = pessoa.classificacaoDoImc()
print(f"{pessoa.nome} tem um IMC de {imc:.2f}, que é classificado como: {classificacao}")