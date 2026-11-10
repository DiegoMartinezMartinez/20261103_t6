"""
lista(pongo los nombres de la clase
while len(lista) >0
escojo un alumno aleatorio y lo meto en un grupo
hace el grupo
"""
import random
#Ponemos el listado de los alumnos
alumnos = [
    "Uriel",
    "Isabella",
    "Nerea",
    "Sara",
    "Nora",
    "Marcos",
    "DiegoA",
    "Javier",
    "German",
    "Alejandro",
    "DiegoR",
    "DiegoM",
    "Ricardo",
]

#Ponemos los alumnos en los grupos de manera aleatoria
random.shuffle(alumnos)
grupo1 = alumnos[0:4]  # grupo de 4 personas
grupo2 = alumnos[4:7]  # grupo de 3 personas
grupo3 = alumnos[7:10]  # grupo de 3 personas
grupo4 = alumnos[10:13]  # grupo de 3 personas


print("Grupo 1 (4 personas):", grupo1)
print("Grupo 2 (3 personas):", grupo2)
print("Grupo 3 (3 personas):", grupo3)
print("Grupo 4 (3 personas):", grupo4)