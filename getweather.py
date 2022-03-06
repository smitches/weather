from meteostat import Point, Hourly
from datetime import datetime
import pytz
# here is the documentation
# https://dev.meteostat.net/python/#example


# havent figured out how to do timezone. do 6 hours difference to match utc offset
# this represents midnight morning
start = datetime(2022, 3, 1, 6)  # , tzinfo=pytz.timezone('US/Central'))
# this represents 11:59 pm in austin at UTC time
end = datetime(2022, 3, 2, 5, 59, 59)  # , tzinfo=pytz.timezone('US/Central'))
# if no zip code use lat/long coordinates
austin = Point(30.427071, -97.801445)
# data = Hourly('78750', start, end)
data = Hourly(austin, start, end)

df = data.fetch()

# options are [temp, dwpt, rhum, prcp, snow, wdir, wspd, wpgt, pres, tsun, coco]
print(df[['temp', 'wdir', 'wspd']])
