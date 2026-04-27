import os 
os.system("cls")
import time


flag = True
acumulador_compra = 0
acumulador_compra = 0
acumulador_baya_precio = 0 
acumulador_pocion_precio = 0 
acumulador_poke_precio = 0
acumulador_revivir_precio = 0 
contador_poke = 0
contador_pocion = 0 
contador_revivir = 0 
contador_baya = 0 
cantidad_revivir = 0 
dscto_revivir = 0 
dscto_por_cantidad = 0
dscto_compra = 0

while flag:
    
    print("1. Pokebola $1000")
    print("2. Pocion $1500")
    print("3. Revivir $3000")
    print("4. Baya $500")
    print("5. Finalizar compra")

    try:

        opcion = int(input("Ingrese opcion \n"))
        if opcion == 1:
            cantidad_poke = int(input("Ingrese cantida que desea comprar \n"))
            acumulador_poke_precio = acumulador_poke_precio + cantidad_poke * 1000
            contador_poke = contador_poke + cantidad_poke
            print("pokebola agregada con exito")

        elif opcion == 2:
            cantidad_pocion = int(input("Ingrese cantidad deseada: \n"))
            acumulador_pocion_precio = acumulador_pocion_precio + cantidad_pocion * 1500
            contador_pocion = contador_pocion + cantidad_pocion
            print("Poción agregada con exito")
        
        elif opcion == 3:
            cantidad_revivir = int(input("Ingrese la cantidad deseada: \n"))
            acumulador_revivir_precio = acumulador_revivir_precio + cantidad_revivir * 3000
            contador_revivir = contador_revivir + cantidad_revivir
            print("Revivir agregado con exito")

        elif opcion == 4:
            cantidad_baya = int(input("Ingrese cantidad deseada: \n"))
            acumulador_baya_precio = acumulador_baya_precio + cantidad_baya * 500
            contador_baya = contador_baya + cantidad_baya
            print("Baya agregaa con exito")
        
        elif opcion == 5:
            flag = False

        else:
            print("Opción ingresada no existe, intente nuevamente")

    except:
        print("iNGRESE VALOR NÚMERICO")

acumulador_bruto = acumulador_poke_precio + acumulador_pocion_precio + acumulador_revivir_precio + acumulador_baya_precio

if cantidad_revivir > 3:
    dscto_revivir = acumulador_revivir_precio * 0.15
    precio_revivir_con_dscto = acumulador_revivir_precio + dscto_revivir
    acumulador_compra = acumulador_poke_precio + acumulador_baya_precio + acumulador_pocion_precio + precio_revivir_con_dscto

else:
    acumulador_compra = acumulador_poke_precio + acumulador_baya_precio + acumulador_pocion_precio + acumulador_revivir_precio
contador_compra = contador_poke + contador_baya + contador_pocion + contador_revivir


if acumulador_compra > 5000:
    dscto_compra = acumulador_compra * 0.10
    acumulador_compra = acumulador_compra - dscto_por_cantidad


if acumulador_compra > 0:

    print(f"total a pagar por pokebolas: ${acumulador_poke_precio} ({contador_poke})")
    print(f"total a pagar por Pociones: ${acumulador_pocion_precio} ({contador_pocion})")
    print(f"total a pagar por Revivir: ${acumulador_revivir_precio} ({contador_revivir})")
    print(f"total a pagar por Bayas: ${acumulador_baya_precio} ({contador_baya})")
    print(f"Cantidad de productos listados: {contador_compra}")
    print("---------------------------------")
    print(f"Total bruto: ${acumulador_bruto}")
    print("---------------------------------")
    print(f"Descuento por Revivir: ${dscto_revivir}")
    print(f"Descuento por Precio (sobre 5000): ${dscto_compra}")
    print(f"descuento por cantidad (sobre 10 unidades): ${dscto_por_cantidad}")
    print("---------------------------------")
    print(f"Total a pagar: ${acumulador_compra}")

else:
    print("No tienes productos seleccionados")

