datospersonales = {"nombre": "samuel", "rut": 226221824, "telefono": "+56 9 3204 3953", "carrera": "Ing. Informatica"}

datospersonales["apellido"] = "quiroz"
datospersonales["nombre"] =  "samuel ignacio"

datospersonales["notas"] = {6.3, 5.3, 6.9}


for clave, valor in datospersonales.items():
    print (f"{clave}  {valor}")

data = input("que desea buscar")

print (datospersonales.get(data, "dato no existe"))


promedio = datospersonales(len["notas"])
print (promedio)