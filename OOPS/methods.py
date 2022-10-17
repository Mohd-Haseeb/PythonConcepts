class FixedFloat:
    def __init__(self, amount) -> None:
        self.amount = amount

    def __repr__(self) -> str:
        return f"<FixedFloat> {self.amount:.2f}"
    
    @staticmethod
    def from_sum(n1, n2):
        return FixedFloat(n1+n2)

    @classmethod
    def to_sum(cls,n1, n2):
        return cls(n1+n2)



ans = FixedFloat.from_sum(16.64,86.655)

# print(ans)


class Dollar(FixedFloat):
    def __init__(self, amount) -> None:
        super().__init__(amount)
        self.symbol = "$"

    def __repr__(self) -> str:
        return f"<Dollar> {self.symbol}{self.amount} "



money = Dollar.to_sum(13.754,645.64)
money2 = Dollar.from_sum(153.64,8976.54)

# CAREFULLY OBSERVE THE OUTPUT
print(money)
print(money2)