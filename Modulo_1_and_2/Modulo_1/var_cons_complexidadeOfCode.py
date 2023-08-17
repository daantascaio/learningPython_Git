"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
        <- Contagem de complexidade (ruim)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 102 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

velocidade_carro_maior_radar = velocidade > RADAR_1
local_carro_dentro_da_area_radar1 = local_carro >= LOCAL_1 - RADAR_RANGE 
local_carro_dentro_da_area_radar2 = local_carro <= LOCAL_1 + RADAR_RANGE
local_carro_dentro_da_area_radar_sempre = local_carro_dentro_da_area_radar1 and local_carro_dentro_da_area_radar2
carro_multado = velocidade_carro_maior_radar and local_carro_dentro_da_area_radar_sempre

#
# if velocidade > RADAR_1:
#     print(f'O carro ultrapassou a velocidade permitida na via!')
#     if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE):        #if local_carro <= 101 and local_carro >= 99:
#         print('E tomou multa!')
#     else:
#         print('Mas, não tomou multa!')
# else:
#     print('O carro não ultrapassou a velocidade permitida na via!')

if velocidade_carro_maior_radar:
    print('O carro ultrapassou a velocidade da via!')

    if carro_multado:
        print('O carro foi multado!')
    else:
        print('O carro não foi multado!')

else:
    print('O carro não ultrapassou a velocidade da via!')