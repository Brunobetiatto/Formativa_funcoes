from sympy import var
from sympy import sympify
from sympy.utilities.lambdify import lambdify

def calcular_funcao_AoB(funcaoA_expr, funcaoB_expr, x, valor_de_x):
    funcao_AoB_expr = funcaoA_expr.subs(x, funcaoB_expr)
    funcao_AoB =  lambdify(x, funcao_AoB_expr)

    return funcao_AoB(valor_de_x)

x = var('x')  
x_input = int(input("digite um valor: "))
funcaoF_input = input("digite a função F: ") 
funcaoG_input = input("digite a função G: ") 
funcaoF_expr = sympify(funcaoF_input)
funcaoG_expr = sympify(funcaoG_input)

print(f"FoF(x) = {calcular_funcao_AoB(funcaoF_expr, funcaoF_expr, x, x_input)}")   
print(f"FoG(x) = {calcular_funcao_AoB(funcaoF_expr, funcaoG_expr, x, x_input)}")   
print(f"GoG(x) = {calcular_funcao_AoB(funcaoG_expr, funcaoG_expr, x, x_input)}")   
print(f"GoF(x) = {calcular_funcao_AoB(funcaoG_expr, funcaoF_expr, x, x_input)}")  

