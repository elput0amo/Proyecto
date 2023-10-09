#lo primero que hay que hacer es importar para poder usar elementos como pi y hacer operaciones como seno o coseno
import math 

#para mayor facilidad he usado los simbolos de los valores al crear las funciones
def calcular_derecha(A,w,t,k,x,phi):
    interiord= w*t-k*x+phi
    y_derecha= A* math.sin(interiord)
    return y_derecha

def calcular_izquierda(A,w,t,k,x,phi):
    interiori= w*t+k*x+phi
    y_izquierda= A* math.sin(interiori)
    return y_izquierda
#las operaciones cambian dependiendo de a donde se propage la onda

while True:
  try:
    direccion = input("Direccion de propagación (Izquierda/Derecha): ")
    if direccion=="Izquierda" or direccion=="Derecha":
      
      break;
    else:
      print(f"({direccion}) no es un comando valido, porfavor escribe (Izquierda) o (Derecha): ")      
  except:
    continue
#la direccion hace falta para definir la operacion despues, he tardado demasiado en aprender como hacer que te pida otro valor si no vale el que has escrito

#me he emocionado y he decidido hacer dos versiones, una mas facil y comprensible, y otra mas optima y dificil de usar.
#seria mas facil hacerlo en diferentes codigos en el mismo repositorio pero queria ver si podia hacerlo

while True:
  try:
    version = input(f"¿Quieres la version (Facil) o (Complicada)?: ")
    if version=="Facil" or version=="Complicada":
      
     break;
    else:
      print(f"({version}) no es valido, aprende a usar mayusculas, porfavor escribe (Izquierda) o (Derecha): ")      
  except:
    continue
  
if version == "Facil":

#aqui voy a pedir todos los valores necesarios para poder calcular
    amplitud = float (input(f"Amplitud (m): "))
    velocidad_angular = float (input(f"Velocidad angular (pi*rad/s): "))
    velocidad_angular2 = velocidad_angular*math.pi 
#aqui simplemente he multiplicado los valores de los radianes por pi para que se puedan operar

    tiempo = float (input(f"Instante de oscilacion (s): "))
    k = float (input(f"Numero de ondas (pi*rad/m): "))
    k2 = k* math.pi 
#es lo mismo que antes
    posicion= float (input(f"Posicion inicial (m): "))

    fase0= float (input(f"Fase inicial (pi*rad): "))
    fase1= fase0*math.pi

#otra vez tengo que calcular por pi
#aqui ya es donde tengo los valores y hago una operacion u otra depende de la direccion

    if direccion == "Derecha" :
        y_derecha = calcular_derecha(amplitud,velocidad_angular2,tiempo,k2,posicion,fase1)
        print (f"Tu elongación en el momento {tiempo}s de la posicion {posicion}m es de {y_derecha:.2f} metros")
        print (f"y({posicion},{tiempo})={y_derecha}m")

    if direccion == "Izquierda":
        y_izquierda = calcular_izquierda(amplitud,velocidad_angular2,tiempo,k2,posicion,fase1)
        print (f"Tu elongación en el momento {tiempo}s de la posicion {posicion}m es de {y_izquierda:.2f} metros")
        print (f"y({posicion},{tiempo})={y_izquierda}m")

#esta era la primera version del codigo pero me he emocionado y queria hacerlo mas optimo 

else:
    print (f"Introduce los valores separados por una coma en el orden: ")
    print(f" A (m) , w (pi*rad/s) , t (s) , k (pi*rad/m) , x (m) , phi (pi*rad) ")
    a, w, t, k, x, phi = input ().split(",")
#aqui he conseguido tener todos los valores del tiron (si todo va bien), ahora proceso para convertirlos en float y poner pi
    a = float(a)
    t=float(t)
    x=float(x)
    w= float (w)*math.pi
    k= float(k)*math.pi
    phi =float(phi)*math.pi
    if direccion == "Derecha" :
        y_derecha = calcular_derecha(a,w,t,k,x,phi)
        print (f"Tu elongación en el momento {t}s de la posicion {x}m es de {y_derecha:.2f} metros")
        print (f"y({x},{t})={y_derecha}m")
    
    if direccion == "Izquierda" :
        y_izquierda = calcular_izquierda(a,w,t,k,x,phi)
        print (f"Tu elongación en el momento {t}s de la posicion {x}m es de {y_izquierda:.2f} metros")
        print (f"y({x},{t})={y_izquierda}m")
#esto es para ver si se ha guardado en gihub
#final


