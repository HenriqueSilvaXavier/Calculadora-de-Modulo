print("Calculadora de módulo:")
multiplos=[0]
c=0
x=int(input("Digite um número: "))
y=int(input("Digite outro número: "))
for k in range(0, x, y):
	c=c+y
	multiplos.append(c)
if x not in multiplos:
	z=x-multiplos[len(multiplos)-2]
if x in multiplos:
	z=0
print(f"{x}%{y}={z}")