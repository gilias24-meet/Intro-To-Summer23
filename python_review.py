import random
temperatures = [23,24,28,18,30,33,25]
days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

good_days = 0 
bad_days = 0

for temp in temperatures:
	if temp % 2==0:
		good_days +=1
print('the amont of good days is:',good_days)

high_temp=max(temperatures)
low_temp=min(temperatures)

print('the highest temp is:',high_temp)
print('the day of the highest temp is:',days[temperatures.index(high_temp)])


print('the lowest temp is:',low_temp)
print('the day of the lowest temp is:',days[temperatures.index(low_temp)])


avg_temp = sum(temperatures)/len(temperatures)
print('the average temp of the week:',avg_temp)


above_avg = [temp for temp in temperatures  if temp > avg_temp]
print('above average days:',above_avg)

print('the weeks temperatures:', temperatures)

