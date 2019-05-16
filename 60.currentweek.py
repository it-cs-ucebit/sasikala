import datetime
Jan1st = datetime.date(2017,10,12)
year,week_num,day_of_week = Jan1st.isocalendar() # DOW = day of week
print()
print("Year %d, Week Number %d, Day of the Week %d" %(year,week_num, day_of_week))
print()
