"""
CONSTANTE = "Variáveis" que não vão mudar (Colocado em letras maiúsculas)
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 62 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_pass_radar_1

if velocidade_carro_pass_radar_1:
    print("Velocidade superior a 60km")

elif carro_passou_radar_1:
    print("Carro passou radar 1")

elif carro_multado_radar_1:
    print("Carro multado em radar 1") 