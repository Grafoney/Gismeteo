def metric():
    a = int(input("Введите длину в см: "))
    x = a * 10000
    y = a * 10
    b = a * 0.01
    c = a * 0.00001
    print(x,"мкм")
    print(y,"мм")
    print(b,"м")
    print(c,"км")

print (metric())


