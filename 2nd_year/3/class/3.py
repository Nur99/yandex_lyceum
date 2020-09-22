class Cinema:
    def __init__(self):
        self.halls = []
        
    def add_hall(hall):
        self.halls.append(hall)

    def get_ticket(start_time, hall_number, row_number, col_number):
        for i in self.halls[hall_number].schedule.order:
            if i[0] == start_time:
                session = i
                initial_length = len(halls[hall_number].bought_places)
                halls[hall_number].bought_places.add((start_time, row_number, col_number))
                current_length = len(halls[hall_number].bought_places)
                if initial_length == current_length:
                    print("Place is sold")
                else:     


class Hall:
    def __init__(self, rows, columns, schedules=None):
        if invalid_data(rows, columns, schedules):
            return
        
        self.bought_places = set()
        self.schedule = Schedule(schedules)
        self.configuration = Scheme(rows, columns)

    def invalid_data(rows, columns, schedules):
        if rows <= 0 or columns <= 0:
            print("Invalid rows or columns")
            return True
        
        schedules.sort()
        for i in range(1, len(schedules)):
            if not schedules[i - 1][1] < schedules[i][0]:
                print("You cannot schedule in that order")
                return True
        return False
                
    def add_session(new_session):
        if self.schedule.safe_addition(new_session):
            self.schedule.order.append(new_session)
        else:
            print("You cannot add this session")
        

class Scheme:
    def __init__(self, rows, columns):
        self.table = []
        for i in range(rows):
            new_row = []
            for j in range(columns):
                new_row.append(0)
            self.table.append(new_row)
        

class Schedule:
    def __init__(self, schedules=None):
        self.order = []
        if schedules:
            self.order = schedules.copy()

    def safe_addition(new_session):
        for session in self.order:
            if overlap(session, new_session):
                return False
        self.order.append(new_session)
        
    def overlap(a, b):
        if(a[0] < b[0] and b[0] < a[1]):
            return True
        if(b[0] < a[0] and a[1] < b[1]):
            return True
        if(a[0] < b[0] and b[1] < a[1]):
            return True
        return False


1) Cinema, Hall, Scheme (two dimensional array), Schedule, Session
2) 0 or 1, 0 empty, 1 sold; 
3) 14 - 16, F1, H1;   15 - 17, F2, H1  >>> overlap >> Hall


cinema 
hall1
hall2
cinema.add_hall(hall1)
cinema.add_hall(hall2)

hall.add_configuration(10, 20)
hall.add_schedule(start_time, finish_time, movie_name)


cinema.get_ticket(movie_name)
    "Success"
"Fail"

