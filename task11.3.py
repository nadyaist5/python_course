class Worker:
    name = ""
    surname = ""
    position = ""
    salary = 0

    def __init__(self, name, surname, position, salary):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary

    def have_workers(self):
        print(self.workers)

    def show_info(self):
        print(self.name, self.surname, 'is a', self.position, 'and has salary', self.salary, ' rub.')


class Cleaner(Worker):
    def __init__(self, name, surname, position, salary, place):
        super().__init__(name, surname, position, salary)
        self.place = place

    def show_info(self):
        print(self.name, self.surname, 'is a', self.position, ', has salary ', self.salary, 'rub and cleans in', self.place, '.')


class Cooker(Worker):
    def __init__(self, name, surname, position, salary, dish):
        super().__init__(name, surname, position, salary)
        self.dish = dish

    def show_info(self):
        print(self.name, self.surname, 'is a', self.position, ', has salary ', self.salary, 'rub and cooks', self.dish, '.')


class Accountent(Worker):
    def __init__(self, name, surname, position, salary):
        super().__init__(name, surname, position, salary)

    def show_info(self):
        print(self.name, self.surname, 'is a', self.position, 'and has salary', self.salary, 'rub.')


class Employee(Worker):
    def __init__(self, name, surname, position, salary):
        super().__init__(name, surname, position, salary)

    def show_info(self):
        print(self.name, self.surname, 'is a', self.position, 'and has salary', self.salary, 'rub.')

class Manager(Employee):
    subworkers = []

    def __init__(self, name, surname, position, salary):
        super().__init__(name, surname, position, salary)

    def add_subworker(self, Worker):
        self.subworkers.append(Worker.name + ' ' + Worker.surname)

    def show_info(self):
        print(self.name, self.surname, 'is a', self.position, ', has salary', self.salary, 'rub and has subworkers:', self.subworkers)

class Deputy_Director(Manager):

    def __init__(self, name, surname, position, salary):
        super().__init__(name, surname, position, salary)

    def add_subworker(self, Worker):
        self.subworkers.append(Worker.name + ' ' + Worker.surname)

    def show_info(self):
        print(self.name, self.surname, 'is a', self.position, ', has salary', self.salary, 'rub and has subworkers:', self.subworkers)

class Director(Deputy_Director):

    def __init__(self, name, surname, position, salary):
        super().__init__(name, surname, position, salary)

    def add_subworker(self, Worker):
        self.subworkers.append(Worker.name + ' ' + Worker.surname)

    def show_info(self):
        print(self.name, self.surname, 'is a', self.position, ', has salary', self.salary, 'rub and has subworkers:', self.subworkers)

worker_1 = Cleaner('John', 'Green', 'cleaner', 25000, 'cabinet 1')
worker_1.show_info()
worker_2 = Cooker('Bob', 'Nash', 'cooker', 30000, 'meat with potatoes')
worker_2.show_info()
worker_3 = Accountent('Jude', 'Tompson', 'accountent', 45000)
worker_3.show_info()
worker_4 = Employee('Tom', 'Brite', 'employee', 40000)
worker_4.show_info()
worker_5 = Manager('George', 'Pitt', 'manager', 62000)
worker_5.add_subworker(worker_4)
worker_5.show_info()
worker_6 = Deputy_Director('Bill', 'Shmidt', 'deputy director', 85000)
worker_6.add_subworker(worker_5)
worker_6.show_info()
worker_7 = Director('Yury', 'Spotich', 'director', 140000)
worker_7.add_subworker(worker_6)
worker_7.show_info()