import re

def cpf_invalido(cpf):
    #Retorna a função caso a quantidade de caractéres de 'cpf' seja diferente de 11.
    return len(cpf) != 11

def nome_invalido(nome):
    #Retorna a função caso o nome não seja inteiro com letras.
    return not nome.isalpha()

def celular_invalido(celular):
    """
    modelo = Variavel que nos apresenta um modelo de como deve ser um celular valido, em colchetes de qaunto a quantos numeros podem ser 
    usados ex: 0-9 e entre chaves quantas vezes vai ser escolhido esses numeros.
    resposta = Variavel que vai comparar o modelo criado anteriormente com o celular passado.
    return = Retorna a resposta não seja correta.
    """
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    print(resposta)
    return not resposta