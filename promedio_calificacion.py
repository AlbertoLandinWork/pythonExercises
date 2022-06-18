resp = "Si"
def run():
    resp = "Si"
    

    while (resp != "No"):
        print("Ingresa el nombre del alumno: ")
        nom = input()
        print("Cuantas calificaciones vas a promediar?: ")
        nCal=input()
        nCal=int(nCal)
        suma=0
        for i in range(1,nCal+1):
            print("Ingresa la ", i,"a. Calificacion: ")
            cal=input()
            cal=float(cal)
            suma = suma + cal
        promedio = suma / nCal
        #Comprobando si el promedio es aprobatorio oreprobatorio
        if (promedio >=7):
            print("El alumno ", nom, " tiene de promedio ", promedio, " y es Aprobatorio")
        else:    
            print("El alumno ", nom, " tiene de promedio ", promedio, " y es Reprobatorio")
        #Preguntar al usuario si desea capturar otro alumno
        print("Deseas capturar a otro alumno (Si/No)?")
        resp = input()


if __name__ == '__main__':
    run()