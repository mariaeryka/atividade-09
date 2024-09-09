# Um motorista deseja calcular o consumo médio de combustível do seu carro. Crie um programa que receba a quantidade de quilômetros percorridos e a quantidade de litros de combustível consumidos, e calcule o consumo médio (km por litro).

Combustível = float(input("seu gasto de combustível aqui"))
Litros = float(input("Seus KM percorridos aqui"))

Média = float(Combustível/Litros)

print(F"Sua média de consumo é {Média}")