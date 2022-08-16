class AUVs:

    veiculos_registrados = []

    def __init__(self) -> None:
        self.tabela = ''
        
    def Exibir_Todos(self, veiculos:'list[object]' = veiculos_registrados) -> 'str':
        try:
            colunas = list( vars( veiculos[0] ).keys() )
            linha = '| {:<23}' * len( colunas )
            self.tabela = linha.format( *colunas ) + '\n'
        except:
            return 'Objeto sem atributos'
        for veiculo in veiculos:
            propriedades = list( map( lambda atributo: str(atributo) if type(atributo)!=list else ','.join(atributo), vars(veiculo).values()))
            linha = '| {:<23}' * len( propriedades )
            self.tabela += linha.format(*propriedades)  + '\n'
        return self.tabela

    def Detalhar_AUV(self, nome:'str') -> 'dict | str':
        identificadores = [veiculo.nome for veiculo in self.veiculos_registrados]
        try:
            indice_nome = identificadores.index(nome)
        except:
            return 'Nome não encontrado'
        else:
            return vars(self.veiculos_registrados[indice_nome])

    def Filtrar_Ano(self) -> 'str':
        veiculos_filtrados = sorted( self.veiculos_registrados, key = lambda veiculo: vars(veiculo)['ano_construcao'], reverse=True )
        return self.Exibir_Todos( veiculos_filtrados )
    
    def Filtrar_Desenpenho(self) -> 'str':
        veiculos_filtrados =sorted( self.veiculos_registrados, key = lambda veiculo: vars(veiculo)['classificacao_testes'], reverse=True )
        return self.Exibir_Todos( veiculos_filtrados )

    def Atualizar_AUVs(self, veiculo:'object') -> None:
        self.veiculos_registrados.append(veiculo)


class VeiculoAutonomo(AUVs):

    def __init__(self, nome:'str', thursters:'int', sensores:'list', dimensoes:'tuple', ano_construcao:'int', classificacao_testes:'int | float') -> None:
        super().__init__()
        self.nome = nome
        self.thursters = thursters
        self.sensores = sensores
        self.dimensoes = dimensoes
        self.ano_construcao = ano_construcao
        self.classificacao_testes = classificacao_testes
        super().Atualizar_AUVs(self)


Vovozao = VeiculoAutonomo('Vovozao', 2, ['Radio', 'Infravermelho'], (0.4,1,0.5), 2016, 6.7)

BRhue = VeiculoAutonomo('BRhue', 6, ['Laser', 'Magnético'], (1.5,2,1.6), 2018, 8.6)

Lua = VeiculoAutonomo('Lua', 8, ['Imagem'], (1,1.3,0.6), 2022, 7.7)


All_auv = AUVs()

print('==='*50)

print(All_auv.Exibir_Todos())

print('==='*50)

print(All_auv.Detalhar_AUV('Vovozao'))

print('==='*50)

print(All_auv.Detalhar_AUV('BRhue'))

print('==='*50)

print(All_auv.Filtrar_Ano())

print('==='*50)

print(All_auv.Filtrar_Desenpenho())










# Exercicio:

# class Pessoa: 
#     def __init__(self, nome:'str', idade:'int', altura:'float') -> None:
#         self.nome = nome
#         self.idade = idade
#         self.altura = altura

#     def Envelhecer(self):
#         self.idade += 1
#         self.Crescer()
    
#     def Crescer(self):
#         if self.idade < 21:
#             self.altura += 0.05
    
#     def __repr__(self):
#         r = '{} tem {} anos de idade e {}m de altura'.format(self.nome,self.idade,self.altura)
#         return r

# class Cliente(Pessoa):
#     def __init__(self, nome: 'str', idade: 'int', altura: 'float') -> None:
#         super().__init__(nome, idade, altura)


# juca = Pessoa('Juca',18,1.40)

# print(juca.idade, juca.altura)
# print(juca)
# print('------')

# juca.Envelhecer()

# print(juca.idade, juca.altura)
# print(juca)
# print('------')

# juca.Envelhecer()

# print(juca.idade, juca.altura)
# print(juca)
# print('------')

# juca.Envelhecer()

# print(juca.idade, juca.altura)
# print(juca)
# print('------')
