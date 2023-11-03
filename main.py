import calendar


is_leap = calendar.isleap(2027)
if is_leap:
    print("2027 год - високосный")
else:
    print("2027 год - не високосный")


day_of_week = calendar.weekday(1995, 6, 25)
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
print(f"25 июня 1995 года был {days[day_of_week]}")


calendar_2023 = calendar.TextCalendar(calendar.SUNDAY)
for month in range(1, 13):
    print("\n" + calendar.month_name[month])
    print(calendar_2023.formatmonth(2023, month))





import calendar

is_leap = calendar.isleap(2027)
if is_leap:
    print("2027 год - високосный")
else:
    print("2027 год - не високосный")

day_of_week = calendar.weekday(1995, 6, 25)
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
print(f"25 июня 1995 года был {days[day_of_week]}")


cal = calendar.Calendar()
for month in range(1, 13):
    print("\n" + calendar.month_name[month])
    for week in cal.monthdayscalendar(2023, month):
        for day in week:
            if day == 0:
                print("   ", end=" ")
            else:
                print(f"{day:2d} ", end=" ")
        print()