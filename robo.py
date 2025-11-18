nb=int(input("Digite o nivel de bateria :"))
t=int(input("Digite a temperatura:"))
us=int(input("Digite a umidade do solo:"))
mododeoperacao=input("Digite o modo de operação:"). upper()
if nb<20:
    print("Bateria muito baixa!Retorne imediatamente para a base!")
if nb >=20:
    if nb<50:
        print("Atenção: Bateria em nível moderado:")
if nb>=50:
    print("Bateria suficiente para operação:")
if t>40:
    print("Temperatura critica! Operação suspensa!")
if t<5:
    print("FRio extremo! Modo de economia ativado")
if us<30:
    print("Solo muito seco. Recomendado iniciar irrigação")
    if us>80:
        print("Solo encharcado! Suspender irrigação imediatamente") 
if mododeoperacao=="plantio":
    print("Iniciando modo de PLANTIO")
if mododeoperacao=="colheita":
    print("Iniciando modo de COLHEITA")
if mododeoperacao=="irrigação":
    print("Iniciando modo de IRRIGAÇÃO")
if nb>=50:
    if t>=10:
        if t<36:
            if us >=30:
                if us<81:
                    print("Robô autorizado a realizar a operação")
                else:
                    print("Operação negada! Verifique as condições do ambiente")
            else:
                print("Operação negada! Verifique as condições do ambiente")
        else:
            print("Operação negada! Verifique as condições do ambiente")
    else:
        print("Operação negada! Verifique as condições do ambiente")
else:
    print("Operação negada! Verifique as condições do ambiente")