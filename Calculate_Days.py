Calculates the date of n days ago from today.

Use datetime.date.today() to get the current day.

Use datetime.timedelta to subtract n days from today's date.

Code:

from datetime import timedelta, date

def days_ago(n):

  return date.today() - timedelta(n)

EXAMPLE

days_ago(5) 

Output: 

 date(2020, 10, 23)

