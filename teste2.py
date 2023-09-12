from sympy import var
from sympy import sympify
from sympy.utilities.lambdify import lambdify

x = var('x')  
x_input = int(input("digite um valor: "))
funcaoF_input = input("digite a função F: ") 
funcaoG_input = input("digite a função G: ")
funcaoF_expr = sympify(funcaoF_input)  
funcaoG_expr = sympify(funcaoG_input)   

funcao_FoF_expr = funcaoF_expr.subs(x,funcaoF_expr)
funcao_FoF = lambdify(x, funcao_FoF_expr)  
print(f"FoF(x) = {funcao_FoF(x_input)}")  

funcao_FoG_expr = funcaoF_expr.subs(x,funcaoG_expr)
funcao_FoG = lambdify(x, funcao_FoG_expr)  
print(f"FoG(x) = {funcao_FoG(x_input)}")   

funcao_GoG_expr = funcaoG_expr.subs(x,funcaoG_expr)
funcao_GoG = lambdify(x, funcao_GoG_expr)  
print(f"GoG(x) = {funcao_GoG(x_input)}")   

funcao_GoF_expr = funcaoG_expr.subs(x,funcaoF_expr)
funcao_GoF = lambdify(x, funcao_GoF_expr)  
print(f"GoF(x) = {funcao_GoF(x_input)}")  

