#1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
##print("Ola mundo")
#2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
##numero =input("DIGITE UM NUMERO")

##print("o numero digita foi "+numero)
#3. Faça um Programa que peça dois números e imprima a soma.
primeiro_numero= float(input("digite um numero"))
segundo_numero= float(input("digite o segundo numero"))
soma= primeiro_numero+segundo_numero
print("o seu resultado é ",soma)
#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))
nota3 = float(input("Digite a nota do terceiro bimestre: "))
nota4 = float(input("Digite a nota do quarto bimestre: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média das notas bimestrais é: {media}")

#5. Faça um Programa que converta metros para centímetros.
metros = float(input("Digite a quantidade em metros: "))
centimetros = metros * 100

print(f"{metros} metros é igual a {centimetros} centímetros")

#6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio**2

print(f"A área do círculo é: {area}")

#7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
]lado = float(input("Digite o comprimento do lado do quadrado: "))
area = lado ** 2
dobro_da_area = 2 * area

print(f"A área do quadrado é: {area}")
print(f"O dobro da área do quadrado é: {dobro_da_area}")

#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas_no_mes = float(input("Digite o número de horas trabalhadas no mês: "))

salario_total = valor_por_hora * horas_trabalhadas_no_mes

print(f"O total do seu salário no mês é: {salario_total}")

#9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    #C = 5 * ((F-32) / 9).
#10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.# Solicita a temperatura em Celsius
temp_celsius = float(input("Digite a temperatura em graus Celsius: "))

# Faz a conversão para Fahrenheit usando a fórmula F = (C * 9/5) + 32
temp_fahrenheit = (temp_celsius * 9/5) + 32

# Exibe o resultado
print(f"A temperatura em graus Fahrenheit é: {temp_fahrenheit:.2f}°F")

#11. Faça um Programa que peça dois números e imprima o maior deles.
# Solicita os dois números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verifica qual é o maior número
if numero1 > numero2:
    print(f"O maior número é: {numero1}")
elif numero2 > numero1:
    print(f"O maior número é: {numero2}")
else:
    print("Os números são iguais.")

#12. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.# Solicita um valor ao usuário
  valor = float(input("Digite um valor: "))

  # Verifica se o valor é positivo, negativo ou zero
  if valor > 0:
      print("O valor é positivo.")
  elif valor < 0:
      print("O valor é negativo.")
  else:
      print("O valor é zero.")

#13. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
    # Solicita a letra correspondente ao sexo
    sexo = input("Digite a letra correspondente ao sexo (F/M): ")

    # Verifica o sexo e imprime a mensagem correspondente
    if sexo.upper() == 'F':
        print("Feminino")
    elif sexo.upper() == 'M':
        print("Masculino")
    else:
        print("Sexo Inválido")

#14. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.# Solicita uma letra ao usuário
      letra = input("Digite uma letra: ")

      # Verifica se a letra é vogal ou consoante
      if letra.lower() in 'aeiou':
          print("A letra é uma vogal.")
      else:
          print("A letra é uma consoante.")

#15. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
    #A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    #A mensagem "Reprovado", se a média for menor do que sete;
    #A mensagem "Aprovado com Distinção", se a média for igual a dez.
        # Solicita as notas ao usuário
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))

        # Calcula a média
        media = (nota1 + nota2) / 2

        # Apresenta a situação do aluno
        if media == 10:
            print("Aprovado com Distinção")
        elif media >= 7:
            print("Aprovado")
        else:
            print("Reprovado")

#16. Faça um Programa que leia três números e mostre o maior deles.
          # Solicita os três números ao usuário
          num1 = float(input("Digite o primeiro número: "))
          num2 = float(input("Digite o segundo número: "))
          num3 = float(input("Digite o terceiro número: "))

          # Encontra o maior número
          maior_numero = max(num1, num2, num3)

          # Exibe o resultado
          print(f"O maior número é: {maior_numero}")

#17. Faça um Programa que leia três números e mostre o maior e o menor deles.# Solicita os três números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Encontra o maior e o menor número
maior_numero = max(num1, num2, num3)
menor_numero = min(num1, num2, num3)

# Exibe os resultados
print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")

#18. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.# Solicita o preço dos três produtos ao usuário
preco_produto1 = float(input("Digite o preço do primeiro produto: "))
preco_produto2 = float(input("Digite o preço do segundo produto: "))
preco_produto3 = float(input("Digite o preço do terceiro produto: "))

# Encontra o produto mais barato
produto_mais_barato = min(preco_produto1, preco_produto2, preco_produto3)

# Exibe o resultado
print(f"Você deve comprar o produto com preço: {produto_mais_barato}")

#19. Faça um Programa que leia três números e mostre-os em ordem decrescente.# Solicita os três números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Cria uma lista com os números e ordena em ordem decrescente
numeros = [num1, num2, num3]
numeros.sort(reverse=True)

# Exibe os números em ordem decrescente
print(f"Números em ordem decrescente: {numeros}")

#20. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.# Solicita o turno ao usuário
turno = input("Em que turno você estuda? Digite M para Matutino, V para Vespertino ou N para Noturno: ")

# Determina a saudação com base no turno
if turno.upper() == 'M':
    print("Bom Dia!")
elif turno.upper() == 'V':
    print("Boa Tarde!")
elif turno.upper() == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")

#21. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.# Solicita o turno ao usuário
  turno = input("Em que turno você estuda? Digite M para Matutino, V para Vespertino ou N para Noturno: ")

  # Determina a saudação com base no turno
  if turno.upper() == 'M':
      print("Bom Dia!")
  elif turno.upper() == 'V':
      print("Boa Tarde!")
  elif turno.upper() == 'N':
      print("Boa Noite!")
  else:
      print("Valor Inválido!")

#22. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.while True:
      # Solicita nome de usuário e senha ao usuário
      usuario = input("Digite o nome de usuário: ")
      senha = input("Digite a senha: ")

      # Verifica se a senha é igual ao nome de usuário
      if senha != usuario:
          print("Cadastro efetuado com sucesso!")
          break  # Sai do loop se a senha for diferente do usuário
      else:
          print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")

#23. Faça um programa que leia e valide as seguintes informações:
   #Nome: maior que 3 caracteres;
   # Idade: entre 0 e 150;
    #Salário: maior que zero;
    #Sexo: 'f' ou 'm';
    #Estado Civil: 's', 'c', 'v', 'd';
        while True:
          # Solicita informações ao usuário
          nome = input("Digite seu nome: ")
          idade = int(input("Digite sua idade: "))
          salario = float(input("Digite seu salário: "))
          sexo = input("Digite seu sexo (f/m): ")
          estado_civil = input("Digite seu estado civil (s/c/v/d): ")

          # Valida as informações
          if len(nome) > 3 and 0 <= idade <= 150 and salario > 0 and sexo.lower() in ['f', 'm'] and estado_civil.lower() in ['s', 'c', 'v', 'd']:
              print("Informações válidas!")
              break  # Sai do loop se todas as informações são válidas
          else:
              print("Erro: Alguma informação é inválida. Por favor, corrija os dados.")

#24. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.populacao_A = 80000
            taxa_crescimento_A = 0.03

            populacao_B = 200000
            taxa_crescimento_B = 0.015

            anos = 0

            while populacao_A < populacao_B:
                populacao_A += populacao_A * taxa_crescimento_A
                populacao_B += populacao_B * taxa_crescimento_B
                anos += 1

            print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")

#25. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
#26. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
#27. Faça um programa que leia 5 números e informe o maior número.
#28. Faça um programa que leia 5 números e informe a soma e a média dos números.
#29. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
#30. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
