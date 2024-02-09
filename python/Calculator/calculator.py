def suma(num1, num2):
  resultado=num1+num2
  return resultado

def resta(num1, num2):
  resultado=num1-num2
  return resultado

def multiplicacion(num1, num2):
  resultado=num1*num2
  return resultado

while True:

  print("Que quieres hacer? ")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicacion")
  print("4. Salir")
  
  opc1 = int(input("Opcion: "))
  
  if opc1 == 1:
    num1 = int(input("Dame un numero: "))
    num2 = int(input("Dame otro numero: "))
    resultado=suma(num1, num2)
    print(f"Tu resultado es: {resultado}\n")
  
  elif opc1 == 2:
    num1 = int(input("Dame un numero: "))
    num2 = int(input("Dame otro numero: "))
    resultado=resta(num1, num2)
    print(f"Tu resultado es: {resultado}\n")
  
  elif opc1 == 3:
    num1 = int(input("Dame un numero: "))
    num2 = int(input("Dame otro numero: "))
    resultado=multiplicacion(num1, num2)
    print(f"Tu resultado es: {resultado}\n")

  elif opc1 == 4:
    break
  else:
    print("No existe esa opcion... \n")