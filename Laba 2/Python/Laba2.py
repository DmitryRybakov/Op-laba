import math

print("Введіть змінні a, b, c, d\n")
a, b, c, d = map(float, input().split())        # введення змінних
c = math.pi * c / 180       # переведення градусної міри у радіани
if d<=0:        # перевірка значення в логарифмі
    print("Не визначене значення логарифму")
else:
   e = float()      # оголошення змінної для знаменника
   e = math.fabs(b * b - a * a) * math.sin(c)
   if e == 0:       # перевірка знаменника
       print("Ділення на 0")        
   else:
       f = float()      # оголошення змінної для функції
       f = math.log1p(d) / e        # обчислення функції
       print("Значення функції дорівнює " + str(f))         # виведення функції


