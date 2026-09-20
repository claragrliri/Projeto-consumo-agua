# Pergunta do tipo de imóvel - segurança para respostas erradas
while True:
    imovel = input("Qual é o tipo do seu imóvel? (comercial, casa ou apartamento): ").strip().lower()
    if imovel in ["comercial", "casa", "apartamento"]:
        break
    print("Tipo de imóvel inválido. Por favor, tente novamente.")

# Pergunta do consumo por mês de água - assegurando para respostas não correspondentes
while True:
    try:
        consumo_mensal = float(input("Qual o consumo mensal de água em m³?: "))
        if consumo_mensal < 0:
            print("O consumo mensal deve ser um valor positivo.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")

# Quantas pessoas moram para saber o consumo médio por morador
if imovel in ["casa", "apartamento"]:
    while True:
        try:
            moradores = int(input("Quantas pessoas moram no imóvel?: "))
            if moradores > 0:
                break
            print("O número de moradores deve ser pelo menos 1.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

# Calculo do Resultado e recomendação de consumo
print("-" * 40)
print("-- Resultado do consumo de Água --")
print("-" * 40)

if imovel == "comercial":
    print(" ᵀᵃʳᶦᶠᵃ comercial aplicada - consulte o plano corporativo para mais detalhes.")

elif imovel == "apartamento" and consumo_mensal < 10:
    print("Consumo econômico - excelente controle de água!")

elif imovel == "casa" and consumo_mensal < 10:
    print("Consumo econômico - excelente controle de água!")

elif imovel == "apartamento" or (imovel == "casa" and consumo_mensal <= 25):
    print("Consumo moderado - dentro do padrão residencial.")

else:
    print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")

# Pergunta para quantidade de morador apenas para lugares residenciais ("casa" ou "apartameneto")
if imovel in ["casa", "apartamento"]:
    consumo_por_pessoa = consumo_mensal / moradores
    print(f"Consumo médio por pessoa: {consumo_por_pessoa:.2f} m³")

# Calculo de consumo médio por morador
litros_por_pessoa_dia = consumo_por_pessoa * 1000 / 30  
if litros_por_pessoa_dia <= 110:
        print("Ótimo hábito! O consumo por pessoa está dentro da recomendação da ONU (110L/dia).")
elif litros_por_pessoa_dia <= 160:
        print("Consumo consciente por pessoa, mas com margem para otimização em banhos e limpezas.")
else:
        print("Atenção: Cada morador está gastando acima da média recomendada. Reduza o tempo no chuveiro!")

print("-" * 40)
