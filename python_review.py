import random
temperatures=[]
for i in range(7):
	temperatures.append(random.randint(26,40))
print(temperatures)

days_of_the_week=["Sunday","Monday","tuesday" "wednesday" "thursday" "friday" "saturday"]
good_days=0
for i in temperatures:
	if i % 2==0:
		good_days=1+good_days
print(good_days)

high_temp=max(temperatures)
low_temp=min(temperatures)
high_temp_day = days_of_the_week[temperatures.index(high_temp)]
low_temp_day = days_of_the_week[temperatures.index(low_temp)]


 avg_temp = sum(temp) / len(temp)
 above_avg = [temperatures for temperatures if temperatures > avg_temp]













# high = 0
# low=0
# for i in range(7):
# 	if temperatures[i] > temperatures[high]:
# 		high=i

# 	elif temperatures[i] < temperatures[low]:
# 		low=i

# # low_1=temperatures.index(low)
# # print(low_1)

# print("low:", low, days_of_the_week[low_1])

# print("high:", high, days_of_the_week[high])











