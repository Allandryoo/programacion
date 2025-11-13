alumnos={"nombre": "alan","nota" : 10,"nombre":"ionut","nota":3,"nombre":"boy","nota":6,"nombre":"carlos","nota":4,"nombre":"patricio","nota":7}
alumnos_aprobados={}
for value in alumnos.items():
    if value["nota"] >= 5:
        alumnos_aprobados.update()