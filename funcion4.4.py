def mostrar_encabezado():
     print("===========================================")
     print("|| Sistema de admision escolar ||")
     print("===========================================")

def solicitar_datos():
        try:   
            estudiantes= {}
            estudiantes["rut"] = int(input("ingrese su rut\n"))
            estudiantes["nombre"] = input("ingrese su nombre\n")
            estudiantes["carrera"] = input("que carrera estudia?\n")
            estudiantes["semestre"] = input("en que semestre va?\n")
        except ValueError:
            print("en rut debe ingresar numeros y en lo demas solo letras")


print("en semstre debe ser: primero, segundo, tercero o cuarto")
def mostrar_datos(alumnos):
     print(f"nombre del estudiante: {alumnos["nombre"]}")
     print(f"rut del estudiante: {alumnos["rut"]}")
     print(f"carrera del estudiante: {alumnos["carrera"]}")
     print(f"semestre del estudiante: {alumnos["semestre"]}")

datos = solicitar_datos()
mostrar_encabezado()
mostrar_datos(datos)


























