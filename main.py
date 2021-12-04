class Buyer:
    def __init__(self):
        self.surname = None
        self.name = None
        self.patronymic = None
        self.address = None
        self.card = None
        self.count = None

    def add(self):
        self.surname = input("Введите фамилию ")
        self.name = input("Введите имя ")
        self.patronymic = input("Введите отчество ")
        self.address = input("Введите адресс ")
        self.card = input("Введите номер карточки ")
        self.count = input("Введите банковский счет ")

    def stats(self):
        print("Фамилия:", self.surname)
        print("Имя:", self.name)
        print("Отчество:", self.patronymic)
        print("Адрес:", self.address)
        print("Номер карты:", self.card)
        print("Банковский счет:", self.count)


users = []

time = int(input("Сколько будем добавлять? "))

for i in range(time):
    buyer = Buyer()
    buyer.add()
    buyer.stats()
    users.append(buyer)
print(users)








