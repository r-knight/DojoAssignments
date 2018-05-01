import product
class Store:

    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
    
    def add_product(self, product):
        self.products.append(product)
        return self
    
    def remove_product(self, product_name):
        for i in range(0, len(self.products)):
            if self.products[i]["item_name"] == product_name:
                self.products.pop(i)
                break
        return self
    
    def inventory(self):
        for product in self.products:
            product.displayInfo()
        return self

if __name__ == "__main__":
    products = []
    product = product.Product(150,"potato", 1, "spess")
    products.append(product)
    store = Store(products, "California", "Some guy")
    print(store.owner)
    store.inventory()