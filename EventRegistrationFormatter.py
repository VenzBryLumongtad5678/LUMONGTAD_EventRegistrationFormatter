from datetime import datetime

first_name = input("Enter student first name: ").strip()
last_name = input("Enter student last name: ").strip()
section = input("Enter section: ").strip()
event_name = input("Enter event name: ").strip()
year = int(input("Enter event year: "))
month = int(input("Enter event month: "))
day = int(input("Enter event day: "))

full_name = f"{first_name.title()} {last_name.title()}"
name_code = full_name.upper()
section_upper = section.upper()
clean_event_name = event_name.title()

event_datetime = datetime(year, month, day)
formatted_date = event_datetime.strftime("%B %d, %Y")

print("\nStudent Event Registration Summary")
print(f"Name: {full_name}")
print(f"Name Code: {name_code}")
print(f"Section: {section_upper}")
print(f"Event: {clean_event_name}")
print(f"Event Date: {formatted_date}")
print(f"Language Used: Python")
print(f"String Feature Used: strip(), title(), upper()")
print(f"Date/Time Feature Used: datetime")
print("Registration record created successfully.")
