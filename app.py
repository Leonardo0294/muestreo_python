import json
import random

poblacion=json.load(open("edades.json"))

# print("poblacion", poblacion)

edades=[]
muestra=[]

for individuo in poblacion:
    edades.append(individuo["age"])
print("promedio de edades", sum(edades)/len(edades))

edades_auxiliar=edades.copy()

for _ in range(0, 21):
    indice_random=random.randint(0, len(edades_auxiliar)-1)
    valor=edades_auxiliar.pop(indice_random)
    muestra.append(valor)
print("valores eleminados", muestra)
print("promedio de muestra", sum(muestra)/len(muestra))

acc=0
cant_muestra=20

k=round(len(edades)/ cant_muestra)
i=random.randint(1, k)

muestra_sistematica=[]
muestra_sistematica.append(edades[i])

for j in range(1, 21):
    acc=i+(j*k)

    if acc <= len(edades)-1:
        muestra_sistematica.append(edades[acc])
    else:
        muestra_sistematica.append(edades[acc - len(edades)])

print("muesta sistematica", muestra_sistematica)
print ("promedio de la muesta sistematica", sum(muestra_sistematica)/len(muestra_sistematica))