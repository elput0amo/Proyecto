while True:
  try:
    version = input(f"¿Quieres la version facil o complicada?")
    if version=="Facil" or version=="Complicada":
      
      break;
    else:
      print(f"{version} no es un comando, aprende a usar mayusculas, porfavor escribe (Izquierda) o (Derecha)")      
  except:
    continue
#final