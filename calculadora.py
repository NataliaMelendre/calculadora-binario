import os

#Esse programa transforma um número decimal digitado pelo usuário em um número binário, octal e hexadecimal

os.system('cls' if os.name == 'nt' else 'clear')

while True:

    opcao = input("Convertendo de: \n [1] Decimal para Binário \n [2] Decimal para Octal \n [3] Decimal para HexaDecimal \n [4] Informações do projeto \n [5] Sair \nEscolha uma opção: ")

    if opcao == "5":
        break

    elif opcao == "1":
        numero= int(input("Digite um número decimal:"))
        binario = ""
        while numero!=0:
                resto = numero%2
                binario = str(resto) + binario
                numero = numero//2

        print (f"O número digitado é igual a {binario} na base 2")

    elif opcao == "2":
         numero= int(input("Digite um número decimal:"))
         octal = ""
         while numero!=0:
                resto = numero%8
                octal = str(resto) + octal
                numero = numero//8 

         print (f"O número digitado é igual a {octal} na base 8")

    elif opcao == "3":
        
        numero= int(input("Digite um número decimal:"))
        hexadecimal = ""
        espaco = " "
        while numero!=0:
                resto = numero%16
                hexadecimal = str(resto) + espaco + hexadecimal
                numero = numero//16
                
                hexadecimal= hexadecimal.replace ("10", "A")
                hexadecimal= hexadecimal.replace ("11", "B")
                hexadecimal= hexadecimal.replace ("12", "C")
                hexadecimal= hexadecimal.replace ("13", "D")
                hexadecimal= hexadecimal.replace ("14", "E")
                hexadecimal= hexadecimal.replace ("15", "F")
                hexadecimal= hexadecimal.replace (" ", "")

                
        print (f"O número digitado é igual a {hexadecimal} na base 16")
    
    elif opcao == "4":
        print("\n------------------------------------------------------------------------------\nSistema que converte da base decimal para Binário, Octal e HexaDecimal. \n------------------------------------------------------------------------------")
        
    else:
        print("Opção inválida.")    
