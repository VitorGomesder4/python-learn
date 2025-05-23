def saudacao(nome: str):
    v = nome.strip().lower().capitalize()
    return f"Ola {v}."

def quadrado(numero: str):
    try:
        n = float(numero)
        return pow(n, 2)
    
    except Exception as e:
        print(f"ERRO: [{e}]")