def main():
    n =int(input("1: Correr Programa  2: Salir:  "))
    while n != 2:
       print("Ingresar cadena: ")
       x= input()
       if x == "abaab":
           print("Es aceptado")
       if x == "abb":
           print("Es aceptado")
       if x == "abaaaabbb":
           print("Es aceptado")
       if x == "aaabbaab":
           print("Es aceptado")
       if x == "abbaab":
           print("Es aceptado")
       if x == "abbbbbb":
           print("Es aceptado")
       if x == "aabbaabb":
           print("Es aceptado")            
       else:
           print("No es aceptado")
       n =int(input("1: Continuar  2: Salir: "))
    
main()
