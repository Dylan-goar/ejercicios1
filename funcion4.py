def conversion_notas(puntaje, puntaje_total):
    nota = (puntaje * 6 /puntaje_total) + 1
    return nota
while True:

        try:
           p = int(input("ingrese la nota del estudiante\n"))
           if p <= 0:
                print("debe ser una nota positiva")
           else:
                break     
        except ValueError:
            print("ingrese solo numeros")
   
pt = int(input("ingrese la nota total de la evaluacion\n"))

calif = conversion_notas(p, pt)
print(f"la nota chile es\n {calif}")










