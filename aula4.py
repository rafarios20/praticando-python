nota = int(input('Digite uma nota: '))
while nota > 10:
     nota = int(input('Você digitou a nota errada, digite novamente: '))
print('Nota correta: {}' .format(nota))




# a = int(input('Entre com um número: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)