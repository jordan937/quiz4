class Info:
    def __init__(self) -> None:
        self.name = "redacted"
        self._condition = "unknown"
        self._weight = 120
        print(f"{self.name}'s account has been created.")

    def get_condition(self) -> str:
        self._condition = "healthy"
        return "healthy"

    def get_weight_impact(self) -> int:
        self._weight += 10
        return self._weight

    def set_condition(self, value: str) -> None:
        self._condition = value

    def set_weight(self, value: int) -> None:
        if value < 0:
            raise ValueError("Weight cannot be negative")
        self._weight = value

def main():
    new_account = Info()
    print(f"New added weight: {new_account._weight}")
    new_account.set_weight(new_account.get_weight_impact())
    print(f"New added weight: {new_account.get_weight_impact()}")

if __name__ == "__main__":
    main()