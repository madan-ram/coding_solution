def is_leap_year(y):
	# if centure year the see if divisible by 400 if not then it is not leap year
	if y%100 == 0:
		return (y%400==0)
	else:
		return (y%4==0)

# number of days from jan 1 to every months 13
days_in_month_till_13 = [13, 44, 72, 103, 133, 164, 194, 225, 256, 286, 317, 347]

j = 0
day = [0]*7
N = input() + 1900
for y in xrange(1900, N):
	for i in xrange(0, 12):
		day_index = (days_in_month_till_13[i]+(j*365))%7
		day[day_index] += 1
		if i == 1 and is_leap_year(y):
			days_in_month_till_13 = [x+1 for x in days_in_month_till_13]
	j += 1

print day

# for y in xrange(1900, N):
# 	if is_leap_year(y):
# 		number_of_days += 1
# 	day_index = (number_of_days + i * 365)%7
# 	day[day_index] += 1
# 	i += 1

# print day