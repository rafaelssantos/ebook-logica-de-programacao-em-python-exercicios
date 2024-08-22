palavra1 = input("Informe a primeira palavra: ")
palavra2 = input("Informe a segunda palavra: ")
palavra3 = input("Informe a terceira palavra: ")

if palavra1 < palavra2 < palavra3:
    print(palavra1, palavra2, palavra3)
elif palavra1 < palavra3 < palavra2:
    print(palavra1, palavra3, palavra2)
elif palavra2 < palavra1 < palavra3:
    print(palavra2, palavra1, palavra3)
elif palavra2 < palavra3 < palavra1:
    print(palavra2, palavra3, palavra1)
elif palavra3 < palavra1 < palavra2:
    print(palavra3, palavra1, palavra2)
else:
    print(palavra3, palavra2, palavra1)