"""Task 4
Створити лист із днями тижня.
В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,"""

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dict_weekdays = {i+1: weekdays[i] for i in range(len(weekdays))}
dict_weekdays_reverse = {weekdays[i]: i+1 for i in range(len(weekdays))}
print(dict_weekdays)
print(dict_weekdays_reverse)
