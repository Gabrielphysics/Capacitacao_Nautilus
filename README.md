# Aula_Nautilus_GIT

 * Entregável da aula de git. Criar repositório remoto e executar clone no repositório local.

# Aula_Nautilus_Python

  * Entregável da aula de python.
    1. "Faça um programa que diga se o primeiro e o último ítens de uma lista são iguais"

        Utilizei a função "Igualdade_Primeiro_Ultimo" para verificar a igualdade entre os itens de índice 0 e -1, ou seja, o primeiro e o último item da lista independente da quantidade de itens e do tipo utilizado retornando “True” quando forem iguais e “False” para caso contrário.
    
    2. "Faça um programa que diga o maior divisor primo de um número dado como input"

        Utilizei a função "Listar_Divisores_Primos" que captura os números primos no range do número especificado e utilizei a função "filter" em conjunto com a função "lambda" para retirar aqueles que não são divisores do número especificado. Com a lista de primos divisores em mãos basta pegar o último item da lista e será o maior primo divisor.

        OBS: A função "Listar_Divisores_Primos" foi desenvolvida com alguns loops, por este motivo eu não recomendaria utilizar em números de grande escala.

    3. "Diga se um número qualquer é um palíndromo."

        Um número palíndromo é aquele que escrito de trás para a frente mantém-se com o mesmo valor. Com esta definição em mente utilizei a função "Verificar_Palindromo" para coletar qualquer número (mesmo que decimais) e transformá-lo em uma string utilizando o recurso de Fatiamento do python para escrever o número ao contrário, verificando assim se ele possui o mesmo valor.

    4. "Dê a soma de todos os números primos menores que 1000."

        Utilizando uma função já citada "Listar_Divisores_Primos" executei a função soma (sum()) para somar todos os números primos encontrados, já que como retorno esta função me dá uma lista com todos os números primos encontrados.   
