Converts a date to its ISO-8601 represenation.

Use datetime.datetime.isoformat() to convert the given datetime object to an ISO-8601 date.

Code:

from datetime import datetime

def to_iso_date(d):

  return d.isoformat()

from datetime import datetime

to_iso_date(datetime(2020,10,25)) 

Output:

2020-10-25T00:00:00
