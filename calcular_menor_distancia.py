def calcular_menor_distancia(viagens):
    # Dicionário para armazenar a distância total percorrida por cada motorista
    distancia_motoristas = {}

    # Iterar sobre todas as viagens
    for viagem in viagens.values():
        motorista = viagem.get('motorista')
        distancia = viagem.get('distancia_total', '0').replace('Km', '').strip()  # Remover "Km" e espaços extras
        
        # Converter distância para float, assumindo que está em quilômetros
        try:
            distancia = float(distancia)
        except ValueError:
            distancia = 0.0

        # Somar a distância para o motorista correspondente
        if motorista in distancia_motoristas:
            distancia_motoristas[motorista] += distancia
        else:
            distancia_motoristas[motorista] = distancia

    # Encontrar o motorista com a menor distância total percorrida
    motorista_menor_distancia = min(distancia_motoristas, key=distancia_motoristas.get)
    menor_distancia = distancia_motoristas[motorista_menor_distancia]

    return motorista_menor_distancia, menor_distancia
