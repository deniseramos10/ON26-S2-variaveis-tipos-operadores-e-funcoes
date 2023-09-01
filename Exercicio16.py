import math

# Solicita o tamanho da área em metros quadrados a ser pintada
area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

# Calcula a quantidade de latas de 18 litros necessárias
litros_necessarios = area_a_ser_pintada / 3
latas_necessarias = math.ceil(litros_necessarios / 18)

# Calcula o preço total
preco_total = latas_necessarias * 80.00

print(f"Você precisa de {latas_necessarias} latas de 18 litros de tinta.")
print(f"O preço total é R$ {preco_total:.2f}")

import math

# Solicita o tamanho da área em metros quadrados a ser pintada
area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

# Calcula a quantidade de litros necessários
litros_necessarios = area_a_ser_pintada / 6

# Calcula a quantidade de latas de 18 litros e galões de 3,6 litros necessários
latas_necessarias = math.ceil(litros_necessarios / 18)
galoes_necessarios = math.ceil(litros_necessarios / 3.6)

# Calcula os preços totais
preco_total_latas = latas_necessarias * 80.00
preco_total_galoes = galoes_necessarios * 25.00

print(f"Para comprar apenas latas de 18 litros, você precisa de {latas_necessarias} latas.")
print(f"O preço total é R$ {preco_total_latas:.2f}")

print(f"Para comprar apenas galões de 3,6 litros, você precisa de {galoes_necessarios} galões.")
print(f"O preço total é R$ {preco_total_galoes:.2f}")