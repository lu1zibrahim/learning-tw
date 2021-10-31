# # Variables - PEP8 All lower case and snake case.
# variable_name = "Aprendizado"
# print(type(variable_name))
# variable_float = 5.5
# variable_boolean = True
#
#
# variable_name = 5
# print(type(variable_name))
#
# # Constant - PEP8 All upper case and snake case.
# CONSTANT_NAME = 10
#
#
# # Aritmetic Operators - Can do with the variables, but not with different types, str + int.
# #But Booleans can
# # Sum
# 5 + 5
#
# # Substraction
# 5 - 5
#
# # Multiplication
# 5 * 5
#
# # Division
# 5 / 5
#
# #With Booleans
# print(variable_name + variable_boolean)
#
# # Logic and comparison Operatiors
# 10 > 10 or 10 >= 10
# 10 < 5 and 10 <= 25
# print(not(10 == 10 and 10 == "10"))
# 10 != 10
#
# # I will test commit with command line
# # git add review.py
# # git commit -m "Commit Message", exit vm if forgot something is :wq
# # git push
#
# # Conditions structures
#
# idade = 20
# if idade < 18:
#     print("Você não é adulto")
# elif 18 <= idade <= 60:
#     print("Você é um adulto")
# else:
#     print("Você está na melhor idade")
#
# # Repetition structures
# # For loop
# for i in range(0,11,2):
#     print(i)
# else:
#     print("The list has finished")
# # While loop
# teste = 0
# while teste <=5:
#     print("codigo sendo executado")
#     teste += 1
# else:
#     print("While loop has ended")

#Functions

def calcular_idade(idade):
    if idade < 18:
        return "Você não é adulto"
    elif 18 <= idade <= 60:
        return "Você é um adulto"
    else:
        return "Você está na melhor idade"


print(calcular_idade(20))
print(calcular_idade(72))