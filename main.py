num1 =float(input("введите первое число:"))
num2 =float(input("введите второе число :"))
result ="числа равны" if num1==num2 else(f"наименьшее число : {num1}"if num1< num2 else f"наименьшее число : {num2}")
print (result)