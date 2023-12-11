#Filter
nomes = ['Larissa', 'Rafael', 'Marcus', 'John']

def pessoa_aprovada(pessoa):
    if pessoa == 'Marcus':
        return True
    else:
        return False
    
print(list(filter(pessoa_aprovada, nomes)))
print(list(map(pessoa_aprovada, nomes)))


pinturas = ['pintura classica', 'Azul', 1857], ['pintura medieval', 'vermelha', 1867],['pintura moderna', 'verde', 1897]

def eh_antiguidade(pintura):
    if pintura[2] < 1890:
        return True
    else:
        return False
    
print(list(filter(eh_antiguidade, pinturas)))
print(list(map(eh_antiguidade, pinturas)))

#Desafio1
##Usando a lista abaixo, filtre apenas as vagas com salário acima de R$2500

vagas = ['vaga 1', 1200], ['vaga 2', 2550], ['vaga 3', 5000]

def salario_acima(salario):
    if salario[1] > 2500 :
        return True
    else:
        return False
    
print(list(filter(salario_acima, vagas)))
print(list(map(salario_acima, vagas)))


