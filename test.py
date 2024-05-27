print("Escriba 2 de las siguientes escalas para convertirlas: Celsius, Farenheit, Kelvin")

escalas_validas = ["Celsius","Farenheit","Kelvin"]
respuesta = ["Si","No"]
grado1 = "°C"
grado2 = "°F"

while True: 
    variable1 = input("Introduzca la primera escala: ")
    variable2 = input("Introduzca la segunda escala: ")
    if variable1 in escalas_validas and variable2 in escalas_validas:
        print(f'¿Desea convertir de {variable1} a {variable2}?')
        respuesta = input("Escriba 'Si' para continuar y 'No' para reintentarlo: ")
    if respuesta == "Si":
        break
    elif respuesta == "No":
        continue
    else:
        print("Escala inválida, por favor ingrese una respuesta válida")
else:
    print("Escalas incorrectas, por favor vuelva a intentarlo")

while True:
    try: 
        cantidad1 = float(input(f"Introduzca la cantidad en grados {variable1}: "))
        break
    except ValueError:
        print("Error, ingrese un número correcto")
   

#Celcius a Farenheit
if variable1 == "Celsius" and variable2 == "Farenheit":
    grado1 = "°C"
    grado2 = "°F"
    resultado = round((cantidad1 * 9/5) + 32,2)
    
#Celcius a Kelvin
elif variable1 == "Celsius" and variable2 == "Kelvin":
    grado1 = "°C"
    grado2 = "°K"
    resultado = round(cantidad1 + 273.15,2)
    
#Farenheit a Celcius
elif variable1 == "Farenheit" and variable2 == "Celsius":
    grado1 = "°F"
    grado2 = "°C"
    resultado = round((cantidad1 -32) * 5/9,2)
    
#Farenheit a Kelvin
elif variable1 == "Farenheit" and variable2 == "Kelvin":
    grado1 = "°F"
    grado2 = "°K"
    resultado = round((cantidad1 - 32) * 5/9 + 273.15,2)
    
#Kelvin a Celcius
elif variable1 == "Kelvin" and variable2 == "Celsius":
    grado1 = "°K"
    grado2 = "°C"
    resultado = round(cantidad1 -273.15,2)

#Kelvin a Farenheit
else: 
    variable1 == "Kelvin" and variable2 == "Farenheit"
    grado1 = "°K"
    grado2 = "°F"
    resultado = round((cantidad1 - 273.15) * 9 / 5 + 32,2)

print (f"{cantidad1}{grado1} equivalen a {resultado}{grado2}") 