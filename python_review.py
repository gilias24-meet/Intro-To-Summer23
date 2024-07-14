import random
temperatures=[]
for i in range(7):
	temperatures.append(random.randint(26,40))
print(temperatures)
days_of_the_week=["Sunday","Monday","tuesday" "wednesday" "thursday" "friday" "saturday"]
num=0
for i in temperatures:
	if i % 2==0:
    num=1+num
print(num)





