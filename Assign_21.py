
# 1. Add the current date to the text file today.txt as a string.

import datetime
file = open('today.txt','w')
file.write(datetime.datetime.now().strftime("%d-%m-%Y"))
file.close()
file = open('today.txt','r')
print(file.read())
file.close()

# 2. Read the text file today.txt into the string today_string

file = open('today.txt','r')
today_string = file.read()
print(today_string)

# 3. Parse the date from today_string.

from datetime import datetime
parsed_data = datetime.strptime(today_string, '%d-%m-%Y')
print(parsed_data)

# 4. List the files in your current directory

import os
for folders, subfolders, files in os.walk(os.getcwd()) :
    for file in files :
        print(file)

# 5. Create a list of all the files in your parent directory (minimum five files should be available).

import os
os.listdir()

# 6. Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one
# and five, print the current time, and then exit.

import multiprocessing
import time
import random
import datetime

def procOne() :
    print(f'Proc_one_Starttime -> {datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    print(f'Proc_one_Endtime -> {datetime.datetime.now()}')

def procTwo():
    print(f'Proc_two_Starttime -> {datetime.datetime.now()}')
    time.sleep(random.randint(1, 5))
    print(f'Proc_two_Endtime -> {datetime.datetime.now()}')


def procThree():
    print(f'Proc_two_Starttime -> {datetime.datetime.now()}')
    time.sleep(random.randint(1, 5))
    print(f'Proc_two_Endtime -> {datetime.datetime.now()}')


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=procOne)
    p2 = multiprocessing.Process(target=procTwo)
    p3 = multiprocessing.Process(target=procThree)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

# 7. create a date object of your day of birth.

from datetime import datetime
my_dob = datetime.strptime('01/02/1999','%d/%m/%Y')
print(my_dob, type(my_dob))

# 8. What day of the week was your day of birth?

from datetime import datetime
my_dob = datetime(1997,4,22)
my_dob.strftime("%A")

# 9. When will you be (or whom were you) 10,000 days old?

from datetime import datetime, timedelta
my_dob = datetime.strptime("01/02/1999",'%d/%m/%Y')
future_date = my_dob-timedelta(10000)
future_date










