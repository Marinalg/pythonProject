import datetime

d = datetime.date.today()
while d.year == 2022:
        if d.day % 2 == 0:                      # Print if even date
                print(d.strftime('%a, %d %b %Y'))
        d += datetime.timedelta(days=1)