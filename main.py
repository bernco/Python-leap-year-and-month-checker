'''
program checks if the year is a leap year then returns the number of days in the selected month

'''

#leap year function definition
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

#function definition that returns the days of the month according to the calender year
def days_in_month(input_year, input_month):
  
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  for _ in range (len(month_days)):
    index_set = input_month-1
    if is_leap(input_year):
      month_days[1] = 29
    days_out = month_days[index_set]
    
    return days_out
    
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)













