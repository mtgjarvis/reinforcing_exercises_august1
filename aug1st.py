seats = [
        [None, "Pumpkin", None, None],
        ["Socks", None, "Mimi", None],
        ["Gismo", "Shadow", None, None],
        ["Smokey","Toast","Pacha","Mau"]
        ]


def check_seat(seating_arangement):
    seat_available = seating_arangement
    for row_index, row in enumerate(seating_arangement):
        row_index += 1
        for seat_index, seat in enumerate(row):
            seat_index += 1
            if seat == "None":
                print(f'Row {row_index} seat {seat_index} is free')
                confirm = input("Would you like to reserve this seat? Y/N:\t").lower()

                if confirm == "y":
                    name = input(f'What is your name?\t')
                seat_available[row_index-1][seat_index-1] = name

                print(seat_available)
                exit()

            # elif: 
            #     seat == "None"


check_seat(seats)


# to iterate over values in lists (with index), wrap list in enumerate
# for index, value in enumerate(seats):
#     print("Value:", value, "Index: ", index)



# student_list = [
#     "bob",
#     33
# ]

# student_list[0] #=> "bob"

# list  vs dict
# index == key
# value == value


# student_dict = {
#     "name": "bob",
#     "age": 33
# }

# student_dict["name"] #=> "bob"


# to iterate over values in dictionaries, use .items()
# for key, value in student_dict.items():
#     print("Key:", key, "value", value) 
    




