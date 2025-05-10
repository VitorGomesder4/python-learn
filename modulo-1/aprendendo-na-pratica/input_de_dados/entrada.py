while True:
    try:
        idade = int(input("Digite sua idade "))
        break
    except ValueError:
        print("Sua idade deve ser um numero inteiro..")
        continue

if idade < 18:
    print("Menor")
else:
    print("Maior")