# Classes and Inheritance

class House:
    def __init__(self,door,bed,wardrobe):
        self.door=door
        self.bed=bed
        self.wardrobe=wardrobe
        print("This shows house details")

    def balcony(self):
        return print("This is the balcony")

class Bedroom1(House):
    def __init__(self,door,bed,wardrobe,windows_style):
        super().__init__(door,bed,wardrobe)
        self.windows=windows_style

    def type_of_balcony(self):
        print("This is bedroom balcony with plants")

master_bedroom=Bedroom1(2,1,2,"French")
print("Style of bedroom windows is ",master_bedroom.windows)
print(master_bedroom.balcony())
#master_bedroom.type_of_balcony()

House3bhk=House(5,2,4)
print(House3bhk)
# print(dir(House3bhk))
print(dir(master_bedroom))