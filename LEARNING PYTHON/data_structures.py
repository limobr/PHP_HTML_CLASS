#tupples
time_table = {
    "Sunday": "Metrine",
    "Monday":[" Susan", "Enock"],
    "Tuesday": "Limo",
    "Wednesday": "Glassias",
    "Thursday": "Kennedy",
    "Friday": ["Anns", "Metrine", "Edith"],
    "Saturday": ["Senteu", "Jones"],
    "Sunday": "Morris"
}

# for (day, crushie) in time_table.items():
#     print(day, crushie)
# # print(time_table["Saturday"])

# Changing Metrine to Janet
if "Metrine" in time_table["Friday"]:
    index = time_table["Friday"].index("Metrine")
    time_table["Friday"][index] = "Janet"

print(time_table["Friday"])

# #Lists
# days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# crushies = ["Lavender", "Samantha", "Cynthia", "Ann", "Kevo", "Brayo"]

# #Looping
# print(days_of_the_week)
# for days in days_of_the_week:
#     print(days)

# i = 0
# while i < len(crushies):
#     print(i)
#     i += 1
# print(f"Senteu's crushies were: {crushies}")

# crushies[4] = "Mitchel"

# crushies.insert(0, "Karen")
# crushies.append("Griffins")
# crushies.remove("Ann")
# crushies.pop(3)
# print(f"Senteu's crushies were: {crushies}")


# if 'Friday' in days_of_the_week:
#     print('Yes, Friday is in the days of the week.')
# else:
#     print("No, it's not a day of the week.")
# print(len(days_of_the_week))
# print('The last element on the list is {}'.format(days_of_the_week[-2]))


# print('The weekdays are: {}'.format(days_of_the_week[1:6]))