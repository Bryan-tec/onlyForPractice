while True:
  print("Que quieres hacer un cuadrado o un triangulo")
  print("1. Triangulo")
  print("2. Cuadrado")
  print("3. Parar")
  opcion=int(input("Opcion: "))
  if opcion == 1:
    rango=int(input("Tamaño del triangulo: \n"))+1
    ran=rango-1
    for r in range(rango):
      for a in range(rango):
        if a<ran:
          print(" ", end="")
        else:
          print("*", end=" ")
      ran=ran-1
      print(" ")
  
  elif opcion == 2:
    rango=int(input("Tamaño del Cuadrado: \n"))+1
    ran=rango-1
    for r in range(rango):
      for a in range(rango):
        print("*", end=" ")
      print(" ")

  elif opcion == 3:
    print("Adios...")
    break

  else:
    print("No existe esa opcion")