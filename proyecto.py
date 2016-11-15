import random
def generar():
      L=range(1,42)
      milista=[]
      while len(milista)<6:
            numero=random.choice(L)
            if not (numero) in milista:
                  milista.append(numero)
      return milista
                               
