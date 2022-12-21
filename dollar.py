class moneyfmt:
    def __init__(self, x):
        self.x = x
    def __str__(self):
        if self.x >= 0:
            return '${:,.2f}'.format(self.x)
        else:
            return '-${:,.2f}'.format(-self.x)

    def update(self,x):
        self.x = x
        return '${:,.2f}'.format(self.x)
    def __repr__(self):
        a = self.x
        return round(a, 1)

a = moneyfmt(4563782983746.1234567890)
print(a.update(432123.3213456))
print(a.__repr__())
print(a)