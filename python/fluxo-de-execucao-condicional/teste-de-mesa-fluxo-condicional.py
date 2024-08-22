# Cenário 1

a = 10
b = 5
c = 8

if a > b:                   # True 10 > 5
    if b > c:               # False 5 > 8
        print("Bloco 1")
    else:
        print("Bloco 2")    # Aqui
else:
    if c > a:
        print("Bloco 3")
    else:
        print("Bloco 4")



# Cenário 2

a = 3
b = 7
c = 9

if a > b:                   # False 3 > 7
    if b > c:
        print("Bloco 1")
    else:
        print("Bloco 2")
else:
    if c > a:               # True 9 > 3
        print("Bloco 3")    # Aqui
    else:
        print("Bloco 4")



# Cenário 3

a = 6
b = 6 
c = 4

if a > b:                   # False 6 > 6
    if b > c:
        print("Bloco 1")
    else:
        print("Bloco 2")
else:
    if c > a:               # False 4 > 6
        print("Bloco 3")
    else:
        print("Bloco 4")    # Aqui