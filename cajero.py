caja_fuerte = 1000

while caja_fuerte > 0:
    valor_solicitado = int(input("Ingrese el dinero a retirar: "))
    if valor_solicitado % 10 == 0:
        if valor_solicitado > caja_fuerte:
            print("Dinero insuficiente en el cajero, por favor utilice otro.")
            break
        else:
            caja_fuerte - valor_solicitado
            b_cien = 0
            b_cincue = 0
            b_veinte = 0
            b_diez = 0
            
            while valor_solicitado >= 100:
                b_cien = b_cien +1
                valor_solicitado -= 100
                
            while valor_solicitado >= 50:
                b_cincue = b_cincue +1
                valor_solicitado -= 50
                
            while valor_solicitado >= 20:
                b_veinte = b_veinte +1
                valor_solicitado -= 20
                
            while valor_solicitado >= 10:
                b_diez = b_diez +1
                valor_solicitado -= 10
                
            total = b_cien + b_cincue + b_veinte + b_diez
            decision = int(input("¿Desea continuar? 1: Si. 2: No."))
            if decision == 1:
                print("---------------------------------------------------------------")
                print("Valor entregado: ", (b_cien*100 + b_cincue*50 + b_veinte*20 + b_diez*10))
                print("Billetes de 100: ", b_cien)
                print("Billetes de 50 : ", b_cincue)
                print("Billetes de 20 : ", b_veinte)
                print("Billetes de 10 : ", b_diez)
                print("---------------------------------------------------------------")
                print("Total billetes : ", total) 

            elif decision == 2:
                print("Transacción cancelada, dinero no entregado.")  
                print("Cancelando ejecución")
                break         
    else: 
        print("Valor no admitido, denominaciones disponibles: 100, 50, 20, 10 ")

print("Gracias por utilizar nuestros servicios.")