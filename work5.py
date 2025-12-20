from datetime import datetime

moscow_times_date = datetime.strptime("Wednesday, October 2, 2002", "%A, %B %d, %Y")
print(moscow_times_date)

guardian_date = datetime.strptime("Friday, 11.10.13", "%A, %d.%m.%y")
print(guardian_date)

daily_news_date = datetime.strptime("Thursday, 18 August 1977", "%A, %d %B %Y")
print(daily_news_date)
