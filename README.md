# Aula_Nautilus_GIT
* Entregável da aula de git. Criar repositório remoto e executar clone no repositório local.

&nbsp;

&nbsp;

# Aula_Nautilus_Python

* ## Entregável da aula de python.
    1. ### "Faça um programa que diga se o primeiro e o último ítens de uma lista são iguais"

        Utilizei a função **Igualdade_Primeiro_Ultimo** para verificar a igualdade entre os itens de índice 0 e -1, ou seja, o primeiro e o último item da lista independente da quantidade de itens e do tipo utilizado retornando “True” quando forem iguais e “False” para caso contrário.
    
    2. ### "Faça um programa que diga o maior divisor primo de um número dado como input"

        Utilizei a função **Listar_Divisores_Primos** que captura os números primos no range do número especificado e utilizei a função **filter** em conjunto com a função **lambda** para retirar aqueles que não são divisores do número especificado. Com a lista de primos divisores em mãos basta pegar o último item da lista e será o maior primo divisor.

        OBS: A função **Listar_Divisores_Primos** foi desenvolvida com alguns loops, por este motivo eu não recomendaria utilizar em números de grande escala.

    3. ### "Diga se um número qualquer é um palíndromo."

        Um número palíndromo é aquele que escrito de trás para a frente mantém-se com o mesmo valor. Com esta definição em mente utilizei a função **Verificar_Palindromo** para coletar qualquer número (mesmo que decimais) e transformá-lo em uma string utilizando o recurso de Fatiamento do python para escrever o número ao contrário, verificando assim se ele possui o mesmo valor.

    4. ### "Dê a soma de todos os números primos menores que 1000."

        Utilizando uma função já citada **Listar_Divisores_Primos** executei a função soma (sum()) para somar todos os números primos encontrados, já que como retorno esta função me dá uma lista com todos os números primos encontrados.   

&nbsp;

&nbsp;

# Aula_Nautilus_Python_POO
    
* ## Entregável da aula de Orientação a Objeto.

    1. ### "Implemente um modelo que descreva os AUVs da UFRJ Nautilus"

        Para descrever os AUVs e suas possíveis funções e relações entre si, o modelo criado em **Aula_python_POO.py** segue a seguinte estrutura:
        
        * ### Objeto **VeiculoAutonomo**

            Um Objeto **VeiculoAutonomo** é criado com as propriedades descritas nos requerimentos, ou seja, contém nome, quantidade de thrusters lista de sensores, as dimensões do veículo, ano de construção e classificação nos testes (parâmetro acrescentado por mim, pensando em prováveis avaliações quantitativas que um veículo poderia passar para fins de análise e desempenho)

            Este objeto criado está conectado, através de uma hierarquia, ao objeto **AUVs** que é responsável por estabelecer as relações entre todos os objetos **VeiculoAutonomo** criados.

            Esta relação é possível, pois **AUVs** guarda **VeiculoAutonomo** dentro do vetor/atributo **veiculos_registrados** podendo ser acessado quando for necessário.

        Obs: Optei por desenvolver de forma hierárquica, porque se os métodos fossem criados em um único objeto, necessariamente deveria criar-se um novo **VeiculoAutonomo** passando todos os parâmetros novamente, mesmo caso fossem vazios. Com isto em mente uma instância **AUVs** pode facilmente analisar e exercer uma visualização geral de forma mais prática.

        * ### Objeto **AUVs**

            Um Objeto **AUVs** pode ser criado em qualquer etapa do código e tem como principal função analisar e visualizar os **VeiculoAutonomo**s criados, logo não possui parâmetros de inicialização.

            Métodos:

                AUVs.Exibir_Todos(veiculos:'list[object]' = veiculos_registrados) -> 'str'
                '''Exibe todos os AUVs em formato tabela'''

            Percorre a lista de veículos passada como parâmetro montando-os em formato tabela-string. No primeiro momento o método busca as chaves encontradas no primeiro objeto da lista e as coloca em posição de cabeçalho da tabela, após esta etapa ele busca os valores de cada objeto formatando diretamente como texto ou aplicando o método **.join** para formatar uma lista.

                AUVs.Detalhar_AUV( nome:'str' ) -> 'dict | str'
                '''Exibe os robôs individualmente'''

            Cria uma lista com os nomes de cada veículo registrado e busca o objeto pelo mesmo índice do nome encontrado.

                AUVs.Filtrar_Ano() -> 'str'
                '''Rankeia os robôs do mais novo para o mais antigo'''
            
            Filtra os **veiculos_registrados** por valor de **ano_construcao** e utiliza o método **Exibir_Todos** para retornar uma tabela com o filtro escolhido.

                AUVs.Filtrar_Desenpenho() -> 'str'
                '''Rankeia os robôs pelo desempenho nos testes''
            
            Filtra os **veiculos_registrados** por valor de **classificacao_testes** e utiliza o método **Exibir_Todos** para retornar uma tabela com o filtro escolhido.

                AUVs.Atualizar_AUVs(veiculo:'object')
                '''Atualiza a lista de veículos registrados'''
            
            Acrescenta um novo objeto **VeiculoAutonomo** na lista **veiculos_registrados**.

&nbsp;

&nbsp;

# Aula_Nautilus_ROS_Basico

* ## Entregável da aula de ROS básico.

    1. ### "Implemente um modelo que descreva os AUVs da UFRJ Nautilus"
        * ### Arquivo **velocidade.py**
            Dentro deste modulo possui um Objeto chamado **Velocidade**, ele é o responsavel por publicar no topico "velocidade" os valores referentes a velocidade do AUV.
            * Utilizando **Twist** foi possivel definir tanto a velocidade angular como linear com um unico objeto.
            * Utilizei o modulo **random** para gerar  numeros aleatórios dentro do range especificado.

        * ### Arquivo **mod_velocidade**
            Dentro deste modulo possui um Objeto chamado **ModularVelocidade** responsavel pela coleta de valores publicados no topico "velocidade"  e também por executar o calculo correspondente ao modulo de um vetor:
            $$
                f(x,y,z) =  \sqrt(x²+y²+z²)
            $$
            * Utilizei a biblioteca math para efetuar a operação.
            * O código publica o valor em formato Float64 em dois tópicos diferentes, a saber "modulo_angular" e "modulo_linear".

&nbsp;

&nbsp;

# Aula_Nautilus_ROS_Avançado

* ## Entregável da aula de ROS Avançado.

    1. ### "Implemente um modelo de sistema solar simples usando TF."
        * ### Arquivo **solar_system.yaml**
            Responsável por determinar os corpos existentes, os quais possuem as seguintes propriedades:

            1.  id: (Nome do corpo)
            2.  raio: (distância entre o corpo e a origem)
            3.  referência: (id do corpo no qual está orbitando)
            4.  velocidade: (velocidade relativa ao ano terrestre)

        * ### Arquivo **TimeSpace.py**

            Responsável por coletar os parâmetros de cada corpo e movimentá-los em órbita respeitando os atributos de cada um. Caso um corpo não possua referência, este permanecerá em sua inércia.
        
        * ### Arquivo **system.launch**

            Responsável por inicializar os processos de servidor de parâmetros e nós.


