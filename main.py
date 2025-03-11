import math

dados_itaparica =[501,507,596,615,662,672,674,684,687,698,742,742,744,755,815,823,828,833,847,851,853,883,894,896,905,909,910,935,938,979,981,985,986,998,1001,1007,1020,1021,1027,1044,1047,1071,1083,1110,1146,1198,1248,1255,1269,1298,1299,1305,1306,1316,1323,1335,1406,1480,1526,1528,1540,1558,1582,1705,1734,1783,1929,1972,2014,2021,2223,2276,2349,2362,2405,2536,2607,2634,2641,2652,2673,2712,2720,2846,2941,3017,3118,3241,3412,3514,3538,3668,3671,3797,3889,3907,4052,4087,4265,4277,4368,4440,4503,4545,4574,4594,4766,4910,4912,4953,4988,5051,5244,5291,5393,5422,5832,6771,7118,
7242]

dados_sobradinho = [506,506,573,614,644,665,669,680,683,690,727,729,737,747,804,815,831,843,843,851,883,889,890,899,923,928,936,945,973,975,976,976,983,984,995,996,1010,1019,1022,1025,1036,1063,1072,1074,1127,1185,1232,1236,1272,1289,1297,1302,1304,1374,1382,1393,1402,1463,1482,1492,1493,1588,1611,1794,1841,1871,1881,1901,1933,1939,2133,2229,2234,2303,2410,2412,2534,2547,2604,2642,2696,2701,2730,2737,2737,2947,3086,3233,3459,3516,3542,3631,3635,3964,4010,4021,4044,4062,4118,4123,4132,4254,4387,4388,4440,4442,4465,4656,4761,4807,4915,5002,5072,5080,5329,5409,5905,6765,6786,6947,]

# colocar dados em ordem crescente
dados_itaparica.sort()
dados_sobradinho.sort()


# calcular número de classes k = 1 + 3,3 x log(n)
numero_classes_k = 1 + 3.3 * math.log(len(dados_itaparica))

# amplitude
amplitude_itaparica = max(dados_itaparica) - min(dados_itaparica) 
amplitude_sobradinho = max(dados_sobradinho) - min(dados_sobradinho) 

# amplitude h
h_itaparica = amplitude_itaparica / numero_classes_k
h_sobradinho = amplitude_sobradinho / numero_classes_k

print((h_itaparica * 1))


print("TABELA DE FREQUÊNCIA IRAPARICA")
print("Intervalo entre classes     |     Frequência absoluta    |     ")
soma_frequencia = 0  # Variável para somar as frequências

for i in range(int(numero_classes_k)):  # Ajuste o range para o número de classes
    frequencia_classe = 0
    
    for j in range(len(dados_itaparica)):
        if (dados_itaparica[j] >= (min(dados_itaparica) + (h_itaparica * i)) and 
            (dados_itaparica[j] < (min(dados_itaparica) + (h_itaparica * (i + 1))))):
            frequencia_classe += 1
                
    soma_frequencia += frequencia_classe  # Acumule a frequência
    
    print(f"{min(dados_itaparica) + (h_itaparica * i)} -| {min(dados_itaparica) + (h_itaparica * (i + 1))}     |     {frequencia_classe}    |     ")

print(f"Soma das frequências: {soma_frequencia}")

