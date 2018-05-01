import store
import product

tater = product.Product(150,"potato", 1, "spess")
tater.add_tax(0.18)

taters =[]
taters.append(tater)
taterShop = store.Store(taters, "The Shire", "Samwise")
taterShop.inventory()
print (taterShop.owner, taterShop.location)