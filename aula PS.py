def Igualdade_Primeiro_Ultimo(lista:'list') -> 'bool':
    if lista[0] == lista[-1]:
        return True
    else:
        return False


def Verificar_Palindromo(numero:'float')-> 'bool':
    numero = str(numero).replace('.','')
    numero_inverso = numero[::-1]

    if numero == numero_inverso:
        return True
    else:
        return False


def Listar_Divisores_Primos(numero:'int') -> 'int':

    listagem = [i for i in range(numero + 1) if i!=1 and i !=0]

    for i in listagem:
        for ii in listagem:
            if i!=ii and ii%i == 0:
                listagem.remove(ii) 

    return listagem


print(Igualdade_Primeiro_Ultimo([1,2,3,4,1]))
    
numero = int(input('Digite um numero para saber o maior divisor primo: '))
print(list(filter(lambda x: numero%x==0,Listar_Divisores_Primos(numero)))[-1])

print(Verificar_Palindromo(1000.01))

print(sum(Listar_Divisores_Primos(1000)))

