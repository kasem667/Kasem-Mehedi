A= float(input())

if A<0 or A>100:print("Fora de intervalo")

elif A<=25:print("Intervalo [0,25]")

elif A<=50:print("Intervalo (25,50]")

elif A<=75:print("Intervalo (25,50]")

else:print("Intervalo (75,100]")