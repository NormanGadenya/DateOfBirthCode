# DateOfBirthCode
import calendar
from datetime import datetime
now=datetime.now()

ne=now.date()

yea=list(str(ne))

year=int(yea[0]+yea[1]+yea[2]+yea[3])

age=input('Enter your age: ')

yr=int(year)-int(age)

mt=input('Enter the month: ')

dy=input('Enter the date of the month: ')

cal=calendar.weekday(int(yr),int(mt),int(dy))

day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']#list of the days

month=['january','february','march','april','may','june','july','august','september','october','november','december'] #list of the months

print('You where born on ',day[cal],dy, month[int(mt)-1], yr)


# Wolimbwa Gadenya Norman Reg 16/u/12408/ps
