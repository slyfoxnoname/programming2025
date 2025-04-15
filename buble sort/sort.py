class cat:
    def __init__(self):
        self.name = None
        self.is_happy = None
        self.age = None


    def add_Cat(self,name , age ,is_happy):
        self.name(name)
        self.age(age)
        self.is_happy(is_happy)

    def print(self):
        print(self.name, "age:", self.age, "Is Happy", self.is_happy)



cat1 = cat()
cat2 = cat()
cat1.add_Cat("SOsi", 12, True)
cat2.add_Cat("cat", 23, False)



