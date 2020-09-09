time_point = input()
if int(time_point) > 0 and 10.3 + int(time_point) >= 24:
    print("Wednesday")
elif int(time_point) < 0 and 10.3 + int(time_point) <= 0:
    print("Monday")
else:
    print("Tuesday")
