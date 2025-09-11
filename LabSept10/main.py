#Q1
print("Welcome to the area calculator\nLet's calculate the area of your triangle!")
height = int(input('Enter Height: '))
base = int(input('Enter Base: '))
print(f"{0.5 * height * base } is the area of your triange")

#Q2
miles = 3
km = miles * 1.61
print(f"Your converted distance from {miles} to km is {km}km")

#Q3
the_name = "Dr Strange"
the_sport = "Ping Pong"
the_day = "4th September, 2025"
the_sentence = "{the_name} played {the_sport} on {the_day}".format(the_name=the_name, the_sport=the_sport, the_day=the_day)
print(the_sentence)

