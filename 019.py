#!/usr/bin/python


months_days = [31,28,31,30,31,30,31,31,30,31,30,31]
months_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

class Date:
    day = 0
    month = 0
    year = 1900
    weekday = 0 # 1 jan 1900 is a monday

    def inc_month(self):
        days_added = months_days[self.month]
        if (self.month == 1
           and (self.year % 4 == 0)
           and ((self.year % 100 == 0) == (self.year % 400 == 0))):
            days_added += 1
        if self.month == 11:
            self.month = 0
            self.year += 1
        else:
            self.month += 1
        self.weekday = (self.weekday + days_added) % 7

    def inc_year(self):
        for i in xrange(0,12):
            self.inc_month()

d = Date()
d.inc_year()

sundays = 0
while d.year != 2001:
    if d.weekday == 6:
        # print "The first day of %s %s is a Sunday !" % (months_names[d.month], d.year)
        sundays += 1
    d.inc_month()

print sundays