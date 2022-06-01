class item:

    def __init__(self,price,type,made_in):

        self.price=price
        self.type=type
        self.made_in=made_in

    def abt_price(self,typee):

        return "{} is the best country and this price is {}".format(typee,self.price)


    def abt_country(self,coountry):
        return "{} unfortunatly is the best but this phone is made in {}".format(coountry,self.made_in)




t=item(1200,"samsung","vietnam")
t.abt_price("italy")
t.abt_country("america")






