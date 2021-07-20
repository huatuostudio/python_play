import calendar
from datetime import date

#today = date.today()
#print("Today's date:", today.weekday())
dateWeek=calendar.day_name[date.today().weekday()]
print("Today's date?")
print(dateWeek)
print("Breakfast calories?")
bCal=int(input())
print(bCal)
print("Lunch calories?")
lCal=int(input())
print(lCal)
print("Dinner calories?")
dCal=int(input())
print(dCal)
print("Snack calories?")
sCal=int(input())
print(sCal)
sumCal=bCal+lCal+dCal+sCal
print("Calorie content for " + dateWeek + " :" + str(sumCal))