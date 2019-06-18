class Mony(object):
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, new_dollars):
        self.total_cents = 100 * new_dollars + self.cents

    # And the getter and setter for cents.
    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, new_cents):
        self.total_cents = 100 * self.dollars + new_cents


money = Mony(2, 20)
print('%d dollars %d cents.' % (money.dollars, money.cents))

money.dollars += 20
money.cents += 100
print('%d dollars %d cents.' % (money.dollars, money.cents))
