# nome_completo = "ronaldo   -- Erro
# nazario"

nome_completo = "ronaldo " \
"nazario"

nome_completo1 = """ronaldo 
nazario"""

#formatação
print("(1FORMA)Nome completo:", nome_completo) #esse metodo automaticamente bota um espaço antes da variavel
print("(2FORMA)Nome completo: "+ nome_completo)
print(f"(3FORMA)Nome completo: {nome_completo}")
print("(4FORMA)Nome completo: {}".format(nome_completo))
print("(5FORMA)Nome completo: %s %s" % (nome_completo, nome_completo))