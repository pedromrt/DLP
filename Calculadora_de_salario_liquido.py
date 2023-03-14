#Este programa sirve para poder calcular el salario liquido (libre de impuestos) de un trabajador.

# Primero establecemos todas nuestas entradas:

nombresT = input("\n Ingrese sus nombres a continuacion: ")
apellidosT = input("\n Ingrese sus apellidos a continuacion: ")
edadT = int(input("\n Ingrese su edad: "))
salarioM = float(input("\n Ingrese su salario mensual: $"))

# Despues de eso establecemos nuestros datos adicionales:

CUOTA = 25
RENTA = 0.10
AFP = 0.0625

# Procedemos a redactar las expreciones algebraicas:

renta = salarioM * RENTA
afp = salarioM * AFP
descuento = renta + afp + CUOTA
salarioL = salarioM - descuento

# Por ultimo selecionaremos la informacion que aparecera por pantalla:

print("\n Su nombre completo es: ",nombresT, apellidosT, "\n\n Su salario liquido libre de impuestos es de: $", salarioL,)
print("\n El descuento a su salario es de: $", descuento,"\n")
