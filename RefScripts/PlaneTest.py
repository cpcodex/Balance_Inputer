class Seat:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.paid = 0.0

    def reserve(self, fn, ln, pd):
        self.first_name = fn
        self.last_name = ln
        self.paid = pd

    def make_empty(self):
        self.first_name = ""
        self.last_name = ""
        self.paid = 0.0

    def is_empty(self):
        return self.first_name == ""

    def print_seat(self):
        print("{} {}, Paid: {:.2f}".format(self.first_name, self.last_name, self.paid))


def make_seats_empty(seats):
    for s in seats:
        s.make_empty()


def print_seats(seats):
    for s in range(len(seats)):
        print("{}:".format(s), end=" ")
        seats[s].print_seat()


num_seats = 8

available_seats = []
for i in range(num_seats):
    available_seats.append(Seat())

command = input("Enter command (p/r/q): ")
while command != "q":
    if command == "p":  # Print seats
        print_seats(available_seats)
    elif command == "r":  # Reserve a seat
        seat_num = int(input("Enter seat num:\n"))
        if not available_seats[seat_num].is_empty():
            print("Seat not empty")
        else:
            fname = input("Enter first name:\n")
            lname = input("Enter last name:\n")
            paid = float(input("Enter amount paid:\n"))
            available_seats[seat_num].reserve(fname, lname, paid)
    else:
        print("Invalid command.")

    command = input("Enter command (p/r/q):\n")
