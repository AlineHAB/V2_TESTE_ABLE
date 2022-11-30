def viagem_volta():

    percurso_total =  130         #305.779  
    galoes = 15.14                #4 * (3,78544 = 1 galão americano)
    km_sol =  10                  #23.5215            
    km_chuva = 7                #716.465          
    
    volta_no_sol = (km_sol * galoes)       #km_sol * 3,7 = resultado -> resultado * 4 
    volta_na_chuva = (km_chuva * galoes)

    if volta_no_sol:
        if volta_no_sol > percurso_total:
            print('Dias de Sol')
            return True
        else:
            print('Dias de Sol')
            return False

    elif volta_na_chuva:
        if volta_na_chuva > percurso_total:
            print('Dias de Chuva')
            return True
        else:
            print('Dias de Chuva')
            return False

print(viagem_volta())

