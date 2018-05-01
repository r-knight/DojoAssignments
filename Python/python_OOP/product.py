class Product:
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.price = self.price*(1+tax)
        return self

    def Return(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        elif reason_for_return == "like new":
            self.status = "for sale"
        elif reason == "opened":
            self.price = self.price *.8
            self.status = "used"
        return self

    def displayInfo(self):
        print("Price:", self.price, "\nItem name:",
              self.item_name, "\nWeight:", self.weight, "\nBrand:", self.brand, "\nStatus: ", self.status)
        return self


if __name__ == "__main__":
    product = Product(150,"potato", 1, "spess")
    print(product)
    print(product.add_tax(0.18))
    product.displayInfo()