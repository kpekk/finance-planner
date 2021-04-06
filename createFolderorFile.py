import datetime
import os

year = input("year: ")
month = input("month: ")
day = input("day: ")

path_ = year
if not os.path.exists(path_):
    os.mkdir(path_)

path_ = os.path.join(year,month)
if not os.path.exists(path_):
    os.mkdir(path_)

path_ = os.path.join(path_,day+".txt")
if not os.path.exists(path_):
    with open(path_, "w+") as f:
        f.write("hlo dear show bob")

newDate = datetime.date(int(year),int(month),int(day))
print(newDate)