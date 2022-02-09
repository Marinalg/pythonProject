from datetime import datetime

class Odd_Days_January:
    current_month = datetime.now().month
    current_year = datetime.now().year

    def __init__(self, month_days: int, month_num: int, day_inyear: int):

        self.day_inyear == day_inyear
        self.month_num == month_num
        self.month_days == month_days

    def show(self):
        return self.day_inyear, self.month_num, self.month_days

    def total_of_count(self, count):
        result = 30
        for day in self.count.value():
            if day == count:
                result -= 1
        return result
        print(total_of_count())

if __name__ == "__main__":
    day_inyear = Odd_Days_January(365)
    month_num = Odd_Days_January(1)
    month_days = Odd_Days_January(31)
print(day_inyear())
print(month_num())
print(month_days())










