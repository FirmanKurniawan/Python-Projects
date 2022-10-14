class Animal:
    def __init__(self, name="", sound="", type="", legs=0):
        self.name = name
        self.sound = sound
        self.type = type
        self.legs = legs

    def returnAnimal(self):
        print(
            "binatang jenis "
            + self.name
            + " yang memiliki suara "
            + self.sound
            + " binatang ini termasuk jenis "
            + self.type
            + " yang memiliki jumlah kaki ",
            self.legs,
            "/n",
        )

    def getName(self):
        return self.name

    def getName(self):
        return self.sound

    def getName(self):
        return self.type

    def getName(self):
        return self.legs


animalList = []
kucing = Animal("kucing", "meow meow", "omnivora", 4)
animalList.append(kucing)

anjing = Animal("anjing", "guk guk", "omnivora", 4)
animalList.append(anjing)

macan = Animal("macan", "roar", "karnivora", 4)
animalList.append(macan)

sapi = Animal("sapi", "moooow", "herbivora", 4)
animalList.append(sapi)

kambing = Animal("kambing", "mbeek", "herbivora", 4)
animalList.append(kambing)

for x in animalList:
    print(x.returnAnimal())
