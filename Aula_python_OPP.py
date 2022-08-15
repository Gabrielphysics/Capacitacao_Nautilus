"""
class Pessoa: 
    def __init__(self, nome:'str', idade:'int', altura:'float') -> None:
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def Envelhecer(self):
        self.idade += 1
        self.Crescer()
    
    def Crescer(self):
        if self.idade < 21:
            self.altura += 0.05
    
    def __repr__(self):
        r = '{} tem {} anos de idade e {}m de altura'.format(self.nome,self.idade,self.altura)
        return r

class Cliente(Pessoa):
    def __init__(self, nome: 'str', idade: 'int', altura: 'float') -> None:
        super().__init__(nome, idade, altura)


gabriel = Pessoa('Gabriel',18,1.40)

print(gabriel.idade, gabriel.altura)
print(gabriel)
print('------')

gabriel.Envelhecer()

print(gabriel.idade, gabriel.altura)
print(gabriel)
print('------')

gabriel.Envelhecer()

print(gabriel.idade, gabriel.altura)
print(gabriel)
print('------')

gabriel.Envelhecer()

print(gabriel.idade, gabriel.altura)
print(gabriel)
print('------')
"""


class AUVs:
    objetos_filhos = []

    def __init__(self) -> None:
        pass
        
    def Exibir_Todos(self, veiculos = objetos_filhos):
        tabela = []
        
        try:
            indexes = list(vars(veiculos[0]).keys())
            linha = '| {:<20}'*len(indexes)
            tabela = (linha.format(*indexes)) + '\n'
        except:pass

        for i in veiculos:
            propriedades = list(map(lambda x: str(x), vars(i).values()))
            linha = '| {:<20}'*len(propriedades)
            tabela += (linha.format(*propriedades)) + '\n'

        return tabela

    def Detalhar_AUV(self, nome):
        ids = [i.nome for i in self.objetos_filhos]
        indice_nome = ids.index(nome)
        return vars(self.objetos_filhos[indice_nome])

    def Filtrar_Ano(self):
        objetos_filtrados = sorted(self.objetos_filhos,key=lambda x: vars(x)['ano_construcao'],reverse=True)
        return self.Exibir_Todos(objetos_filtrados)
    
    def Filtrar_Desenpenho(self):
        objetos_filtrados =sorted(self.objetos_filhos,key=lambda x: vars(x)['classificacao_testes'],reverse=True)
        return self.Exibir_Todos(objetos_filtrados)

    def Atualizar_AUVs(self, veiculo):
        self.objetos_filhos.append(veiculo)


class Veiculo_Autonomo(AUVs):
    def __init__(self, nome:'str', tipo:'str', sensores:'list', dimensoes:'tuple', ano_construcao:'int', classificacao_testes:'float') -> None:
        super().__init__()
        self.nome = nome
        self.tipo = tipo
        self.sensores = sensores
        self.dimensoes = dimensoes
        self.ano_construcao = ano_construcao
        self.classificacao_testes = classificacao_testes
        
        super().Atualizar_AUVs(self)



Vovozao = Veiculo_Autonomo('Vovozao', 'aquatico', [], (0.4,1,0.5), 2016, 6.7)

BRhue = Veiculo_Autonomo('BRhue', 'aquatico', ['SENSORS PCB'], (1.5,2,1.6), 2018, 8.6)

Lua = Veiculo_Autonomo('Lua', 'aquatico', ['SENSORS PCB'], (1,1.3,0.6), 2022, 8.9)

Drone = Veiculo_Autonomo('Drone', 'aereo', ['Infravermelho'], (0.7, 0.7, 0.5), 2022, 7.4)


All_auv = AUVs()

print('==='*50)

print(All_auv.Exibir_Todos())

print('==='*50)

print(All_auv.Detalhar_AUV('Vovozao'))

print('==='*50)

print(All_auv.Detalhar_AUV('Drone'))

print('==='*50)

print(All_auv.Filtrar_Ano())

print('==='*50)

print(All_auv.Filtrar_Desenpenho())




    