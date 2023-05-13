class Human:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.tickets = []

    def searchTickets(self, boxoffice):
        print(self.name, ' is looking at:')
        boxoffice.showTickets()
        print()

    def buyTicket(self, boxoffice, dest):
        boxoffice.sellTicket(self, dest)

    def hasTicketsTo(self):
        print(self.name, ' has tickets to ', str(self.tickets), '.')
        print()


class BoxOffice:

    def __init__(self, location):
        self.location = location
        self.tickets = {
            'SaintP': 3600,
            'Moscow': 5800,
            'Kazan': 3200,
            'Samara': 1800,
        }

    def showTickets(self):
        for dest, price in self.tickets.items():
            print(dest, '\t', str(price), ' rub')

    def sellTicket(self, human, dest):
        if dest in self.tickets:
            price = self.tickets.get(dest)
            if human.balance >= price:
                human.balance -= price
                human.tickets.append(dest)
                print('You are buying a ticket to ', dest, '.')
                print('Thank you, ', human.name, ', for your purchase! Happy Traveling to ', dest, '!')
                print('You have ', str(human.balance), ' rubles left.')
                print()
            else:
                print('Sorry, ', human.name, ', your balance (', str(human.balance), ' rub) is too low for this purchase (', dest, ').')
                print('Maybe, you can travel somewhere else. Take a look at available tickets:')
                self.showTickets()
                print()
        else:
            print('Sorry, ', human.name, ', no tickets to ', dest, ' available.')
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
