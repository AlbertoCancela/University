#Conexión Python-Arduino
import serial, time
PUERTO = "COM11"
serialArduino = serial.Serial(PUERTO, 9600)

#Declaración de variables
diaSemana = 0;
#Desarrollo
cadena = "12:40:00"
time.sleep(2)
serialArduino.write(cadena.encode())
#Recibir datos (prueba)
String = serialArduino.readline()
print(String)

cadena2 = "08:00:00"
time.sleep(2)
serialArduino.write(cadena2.encode('ascii'))
#Recibir datos (prueba)
String = serialArduino.readline()
print(String)
serialArduino.close()

    #mi_lista = []
    #mi_lista.append("Juan")
    #mi_lista.append("Juan2")
    #mi_lista.append("JuanDXdxDX")
    #print(mi_lista[0]) # Muestra Juan (la primera posición es la 0)
    #print(mi_lista[2]) # Muestra Juan (la primera posición es la 0)