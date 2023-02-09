# El cajero debe pedir el valor a retirar
# Denominaciones de los billetes 10 20 50 y 100
# confirmacion (Seguir o cancelar)

b_cien = 5
b_cincue = 5
b_veinte = 5
b_diez = 5
caja_fuerte = b_cien * 100 + b_cincue * 50 + b_veinte * 20 + b_diez * 10

while caja_fuerte > 0:
    valor_solicitado = int(input("Ingrese el dinero a retirar: "))
    if valor_solicitado % 10 == 0:
        if valor_solicitado > caja_fuerte:
            print("Dinero insuficiente en el cajero, por favor utilice otro.")
            pass
        else:
            valor_a_restar_en_caja = valor_solicitado
            c1 = 0
            c2 = 0
            c3 = 0
            c4 = 0
            while valor_solicitado >= 100:
                if b_cien == 0:
                    break
                else:
                    b_cien = b_cien - 1
                    c1 += 1
                    valor_solicitado -= 100
                    caja_fuerte -= 100
                

            while valor_solicitado >= 50:
                if b_cincue == 0:
                    break
                else: 
                    b_cincue = b_cincue - 1
                    c2 += 1
                    valor_solicitado -= 50
                    caja_fuerte -= 50
                
                
            while valor_solicitado >= 20:
                if b_veinte == 0:
                    break
                else:
                    b_veinte = b_veinte - 1
                    c3 += 1
                    valor_solicitado -= 20
                    caja_fuerte -= 20
                
            while valor_solicitado >= 10:
                if b_diez == 0:
                    break
                else:
                    b_diez = b_diez - 1
                    c4 += 1
                    valor_solicitado -= 10
                    caja_fuerte -= 10
                
            decision = int(input("¿Desea continuar? 1: Si. 2: No."))
            if decision == 1:
                print("---------------------------------------------------------------")
                print("Valor entregado: ", (c1*100 + c2*50 + c3*20 + c4*10))
                print("Billetes de 100: ", c1)
                print("Billetes de 50 : ", c2)
                print("Billetes de 20 : ", c3)
                print("Billetes de 10 : ", c4)
                print("---------------------------------------------------------------")
                print("Total billetes : ", c1+c2+c3+c4 ) 

            elif decision == 2:
                print("Transacción cancelada, dinero no entregado.")  
                print("Cancelando ejecución")
                pass         
    else: 
        print("Valor no admitido, denominaciones disponibles: 100, 50, 20, 10 ")
        pass
        
print("---------------------------------------------------------------")
print("Cajero sin fondos, vuelva más tarde....")