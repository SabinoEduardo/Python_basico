import math
a = 2
b = 3
c =  4
if b**2 > a**2 + c**2 :
    angle_interno1 = math.degrees((a**2 + b**2 - c**2) / (2*a * b))
    angle_interno2 = math.degrees((c**2 + b**2 - a**2) / (2*c * b))
    
elif a**2 > c**2 + b**2 :
    angle_interno1 = math.degrees((c**2 + a**2 - b**2) / (2*c * a))
    angle_interno2 = math.degrees((a**2 + b**2 - c**2) / (2*c * b))

elif c**2 > a**2 + b**2:
    angle_interno1 = math.degrees((c**2 + b**2 - a**2) / (2*c * b))
    angle_interno2 = math.degrees((a**2 + c**2 - b**2) / (2*c * a))

angle_interno3 = 180 - angle_interno2 - angle_interno1

print(angle_interno1, angle_interno2, angle_interno3)
print(angle_interno1 + angle_interno2 + angle_interno3)

