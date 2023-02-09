from os import system
system("cls")

b_cien = 5
b_cincue = 5
b_veinte = 5
b_diez = 5
caja_fuerte = [ b_cien * 100,
                b_cincue * 50,  
                b_veinte * 20,
                b_diez * 10
                ]

def darbilletes(valor_solicitado,valorDelBillete):
    contador = 0
    while valor_solicitado >= valorDelBillete:
        contador += 1
        valorDelBillete -= 1
        valor_solicitado -= valorDelBillete
        if valorDelBillete == 0:
            break
    return valor_solicitado, contador



while caja_fuerte > 0:
    valor_solicitado = int(input("Ingrese el dinero a retirar: "))
    if valor_solicitado % 10 == 0:
        if valor_solicitado > caja_fuerte:
            print("Dinero insuficiente en el cajero, por favor utilice otro.")
            break
        else:
            valor_a_restar_en_caja = valor_solicitado
            valor_solicitado , b_cien   = darbilletes(valor_solicitado,b_cien*100)
            valor_solicitado , b_cincue = darbilletes(valor_solicitado,b_cincue*50)
            valor_solicitado , b_veinte = darbilletes(valor_solicitado,b_veinte*20)
            valor_solicitado , b_diez   = darbilletes(valor_solicitado,b_diez*10)
            caja_fuerte - valor_a_restar_en_caja
            DineroRestante = b_cien * 100 + b_cincue * 50 + b_veinte *20 + b_diez * 10
            decision = int(input("¿Desea continuar? 1: Si. 2: No."))
            if decision == 1:
                print("---------------------------------------------------------------")
                print("Valor entregado: ", valor_a_restar_en_caja)
                print("Billetes de 100: ", b_cien)
                print("Billetes de 50 : ", b_cincue)
                print("Billetes de 20 : ", b_veinte)
                print("Billetes de 10 : ", b_diez)
                print("---------------------------------------------------------------") 

            elif decision == 2:
                print("Transacción cancelada, dinero no entregado.")  
                print("Cancelando ejecución")
                break         
    else: 
        print("Valor no admitido, denominaciones disponibles: 100, 50, 20, 10 ")
        
print("Gracias por utilizar nuestros servicios.")