print("Bienvenido a la calculadora de comisiones.")
print("------------------------------------------")

nombre = input("Dime tu nombre: ")
ventas = int(input("Dime el valor de tus ventas en $ de este mes: "))

valor_comision = round(ventas * (13 / 100), 2)

valor_total = ventas + valor_comision

print(f"Hola {nombre}. Con el valor de ventas de {ventas}$ te corresponde, con una comisión del 13%, una comision de {valor_comision}$ y un ingreso total de {valor_total}$")

input("Pulsa ENTER para finalizar el programa.")