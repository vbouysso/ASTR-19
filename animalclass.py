class SnowLeopard():
    def __init__(self):
        self.armlength = 3.5
        self.leglength = 4.2
        self.numofeyes = 2
        self.hastail = True
        self.isfurry = True


    def printdetails(self):
        print("The Snow Leapord has arms that are ", self.armlength, " feet long!")
        print("The Snow Leapord has legs that are ", self.leglength, " feet long!")
        print("The Snow Leapord has ", self.numofeyes, " beautiful eyes :)")
        if self.hastail:
            print("The Snow Leapord has a long tail.")
        else:
            print("The snow leopard has no tail!")
        if self.isfurry:
            print("The Snow Leapord has a beautiful furry coat.")
        else:
            print("The snow leopard is not soft to the touch.")

jason = SnowLeopard();
print("test :")
jason.printdetails()
jason.hastail = False
jason.printdetails()
