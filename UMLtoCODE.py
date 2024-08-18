import datetime

class User:
    def __init__(self, Name, Status, ID, Password):
        self.Name = Name
        self.Status = Status
        self.ID = ID
        self.Password = Password

    def login(self):
        return f'user name: {self.Name}, status: {self.Status}, id: {self.ID}, password: {self.Password}'

    def logout(self):
        return f'user name: {self.Name}, status: {self.Status}, id: {self.ID}, password: {self.Password}'


class Manager(User):
    def __init__(self, Name, Status, ID, Password, EmployeeID, Price, RoomID):
        super().__init__(Name, Status, ID, Password)
        self.EmployeeID = EmployeeID
        self.Price = Price
        self.RoomID = RoomID

    def login(self):
        return f'{super().login()}'

    def logout(self):
        return f'{super().logout()}'

    def add_employee(self):
        return f'manager employeeid: {self.EmployeeID}'

    def remove_employee(self):
        return f'manager employeeid: {self.EmployeeID}'

    def add_room(self):
        return f'manager roomid: {self.RoomID}'

    def delete_room(self):
        return f'manager roomid: {self.RoomID}'

    def update_room_price(self):
        return f'manager roomid: {self.RoomID}, price: {self.Price}'


class Guest(User):
    def __init__(self, Name, Status, ID, Password, Email, Phone_no):
        super().__init__(Name, Status, ID, Password)
        self.Email = Email
        self.Phone_no = Phone_no

    def login(self):
        return f'{super().login()}'

    def logout(self):
        return f'{super().logout()}'

    def book_package(self):
        return f'guest id: {self.ID}, phone: {self.Phone_no}, name: {self.Name}, email: {self.Email}'

    def create_account(self):
        return f'guest id: {self.ID}, phone: {self.Phone_no}, name: {self.Name}, email: {self.Email}, status: {self.Status}'


class FrontDesk(User):
    def __init__(self, Name, Status, ID, Password, RoomID, guests):
        super().__init__(Name, Status, ID, Password)
        self.RoomID = RoomID
        self.guests = guests

    def login(self):
        return f'{super().login()}'

    def logout(self):
        return f'{super().logout()}'

    def add_guest(self, guest):
        self.guests.append(guest)
        return f'FrontDesk guestid: {guest.ID}, phone: {guest.Phone_no}, name: {guest.Name}, email: {guest.Email}'

    def search_room(self):
        return f'FrontDesk roomid: {self.RoomID}'

    def book_package(self):
        return f'FrontDesk roomid: {self.RoomID}, guestid: {self.guests[0].ID}' if self.guests else 'No guest available'


class Room:
    def __init__(self, RoomNo, RoomType, RoomPrice, RoomStatus):
        self.RoomNo = RoomNo
        self.RoomType = RoomType
        self.RoomPrice = RoomPrice
        self.RoomStatus = RoomStatus

    def check_availability(self):
        return f'Room roomno: {self.RoomNo}, roomtype: {self.RoomType}, roomPrice: {self.RoomPrice}, roomstatus: {self.RoomStatus}'

    def check_in(self):
        return f'Room roomno: {self.RoomNo}, roomtype: {self.RoomType}, roomPrice: {self.RoomPrice}, roomstatus: {self.RoomStatus}'

    def check_out(self):
        return f'Room roomno: {self.RoomNo}, roomtype: {self.RoomType}, roomPrice: {self.RoomPrice}, roomstatus: {self.RoomStatus}'


class Booking:
    def __init__(self, BookingNo, CheckInDate, CheckOutDate, BookingStatus, room):
        self.BookingNo = BookingNo
        self.CheckInDate = CheckInDate
        self.CheckOutDate = CheckOutDate
        self.BookingStatus = BookingStatus
        self.room = room

    def room_booking(self):
        return f'Booking bookingno: {self.BookingNo}, checkindate: {self.CheckInDate}, checkoutdate: {self.CheckOutDate}, bookingstatus: {self.BookingStatus}'


class Invoice:
    def __init__(self, InvoiceNo, Amount, Date, front_desk):
        self.InvoiceNo = InvoiceNo
        self.Amount = Amount
        self.Date = Date
        self.front_desk = front_desk

    def print_receipt(self):
        return f'Invoice invoiceno: {self.InvoiceNo}, amount: {self.Amount}, date: {self.Date}'


# Usage:
guest1 = Guest("John", "Active", "G001", "guestpass", "john@example.com", "123456789")
front_desk = FrontDesk("FrontDeskName", "Active", "FD001", "frontdeskpass", "Room001", [])

front_desk.add_guest(guest1)

room1 = Room("Room001", "Single", 100, "Available")
booking1 = Booking("B001", "2023-01-01", "2023-01-05", "Confirmed", room1)

invoice1 = Invoice("I001", 500, datetime.date.today(), front_desk)

# Additional test
print(front_desk.book_package())  # Output: FrontDesk roomid: Room001, guestid: G001
