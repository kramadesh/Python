
from typing import List


class ShoppingCart:
    def __init__(self, max_size) -> None:
        self.items:List[str] = []
        self.max_size = max_size

    def addItem(self, item:str):
        if self.getSize() == self.max_size:
            raise OverflowError("cannot add more item")
        self.items.append(item)

    def getSize(self)->int:
        return len(self.items)

    def getItems(self)->List[str]:
        return self.items

    def getTotalPrice(self, priceList):
        total_price = 0
        for item in self.items:
            total_price += priceList.get(item)
        return total_price

