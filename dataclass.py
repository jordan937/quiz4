from dataclasses import dataclass

@dataclass
class Antiques:
    age: int
    value: int
    reproduction: bool
    type: str

    def auth(self)->None:
        if(self.reproduction == False):
            print(f"The {self.type} is not a reproduction")
        
        else:
            print(f"The {self.type} is a reproduction")
        

def main():
    data = [
        Antiques(70, 100000, False, "Tiffany Lamp"),
        Antiques(3, 50, True, "Reproduced Coca Cola Sign")
    ]

    data.append(Antiques(300, 500, True, "Chess Board"))
    print(f"I want to buy a {data[0].type} for ${data[1].value}")
    data[0].auth()

if __name__=="__main__":
    main()