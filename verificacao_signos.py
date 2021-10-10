mes = int(input("Escolha a opção que representa seu mês: \n 1: Janeiro \n 2: Fevereiro \n 3: Março \n 4: Abril \n 5: Maio \n 6: Junho \n 7: Julho \n 8: Agosto \n 9: Setembro \n 10: Outubro \n 11: Novembro \n 12: Dezembro \n Digite o número referente ao mês: "))
dia = int(input('Digite o dia: '))

if dia >= 20 and dia <= 31 and mes == 3 or dia >= 1 and dia <= 20 and mes == 4:
    print("É do signo de Áries ")
elif dia >= 21 and dia <= 30 and mes == 4 or dia >=1 and dia <= 20 and mes == 5:
    print("É do signo de Touro")
elif dia >= 21 and dia <= 31 and mes == 5 or dia >= 1 and dia <= 20 and mes == 6:
    print("É do signo de Gêmeos")
elif dia >= 21 and dia <= 30 and mes == 6 or dia >= 1 and dia <= 21 and mes == 7:
    print("É do signo de Cancer")
elif dia >= 22 and dia <= 31 and mes == 7 or dia >= 1 and dia <= 22 and mes == 8:
    print("É do signo de Leão")
elif dia >= 22 and dia <= 31 and mes == 8 or dia >= 1 and dia <= 22 and mes == 9:
    print("É do signo de Virgem")
elif dia >= 22 and dia <= 30 and mes == 9 or dia >= 1 and dia <= 22 and mes == 10:
    print("É do signo de Libra")
elif dia >= 23 and dia <= 31 and mes == 10 or dia >= 1 and dia <= 21 and mes == 11:
    print("É do signo de Escorpião")
elif dia >= 22 and dia <= 30 and mes == 11 or dia >= 1 and dia <= 21 and mes == 12:
    print("É do signo de Sagitário")
elif dia >= 22 and dia <= 31 and mes == 12 or dia >= 1 and dia <= 20 and mes == 1:
    print("É do signo de Capricórnio")
elif dia >= 21 and dia <= 31 and mes == 1 or dia >= 1 and dia <= 18 and mes == 2:
    print("É do signo de Aquário")
elif dia >= 19 and dia <= 29 and mes == 2 or dia >= 1 and dia <= 19 and mes == 3:
    print("É do signo de Peixes")
else:
    print("Dia ou mês invalido")
