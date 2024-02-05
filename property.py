class Info:

    name: str
    condition: str
    weight: int

    def __init__(self) -> None:
        self.name = "redacted"
        self.weight = 120
        print(f"{self.name}'s account has been created.")

    @property
    def condition(self)->str:
        self.condition = "healthy"
        return "healthy"
    
    @property
    def weightImpact(self)->int:
        self.weight = self.weight + 10
        return self.weight

def main():
    new_account = Info()
    print(f"New added weight: {new_account.weight}")
    new_account.wei
    print(f"New added weight: {new_account.weightImpact}")


if __name__ == "__main__":
    main()