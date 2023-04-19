class Human:
    name = ""
    balance = 0
    tickets = []

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def searchTickets(self, BoxOffice):
        print(self.name, ' is looking at:')
        BoxOffice.showTickets()
        print()

    def buyTicket(self, BoxOffice, dest):
        BoxOffice.sellTicket(self, dest)

    def hasTicketsTo(self):
        print(self.name, ' has tickets to ', str(self.tickets), '.')
        print()


class BoxOffice:
    location = ""
    tickets = {
        'SaintP': 3600,
        'Moscow': 5800,
        'Kazan': 3200,
        'Samara': 1800,
    }

    def __init__(self, location):
        self.location = location

    def showTickets(self):
        for dest, price in self.tickets.items():
            print(dest, '\t', str(price), ' rub')

    def sellTicket(self, Human, dest):
        if dest in self.tickets:
            price = self.tickets.get(dest)
            if Human.balance >= price:
                Human.balance -= price
                Human.tickets.append(dest)
                print('You are buying a ticket to ', dest, '.')
                print('Thank you, ', Human.name, ', for your purchase! Happy Traveling to ', dest, '!')
                print('You have ', str(Human.balance), ' rubles left.')
                print()
            else:
                print('Sorry, ', Human.name, ', your balance (', str(Human.balance), ' rub) is too low for this purchase (', dest, ').')
                print('Maybe, you can travel somewhere else. Take a look at available tickets:')
                self.showTickets()
                print()
        else:
            print('Sorry, ', Human.name, ', no tickets to ', dest, ' available.')
            print('Please, take a look at available tickets:')
            self.showTickets()
            print()


human1 = Human('Nadya', 10000)
boxOffice = BoxOffice('Novosibirsk')

human1.searchTickets(boxOffice)
human1.buyTicket(boxOffice, 'Moscow')
human1.hasTicketsTo()
human1.buyTicket(boxOffice, 'Kazan')
human1.hasTicketsTo()
human1.buyTicket(boxOffice, 'Vladivostok')
human1.buyTicket(boxOffice, 'Samara')
human1.hasTicketsTo()