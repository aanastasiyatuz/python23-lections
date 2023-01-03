catalog = [
    {
        "id": 1,
        "title": "молоко",
        "quantity": 25,
        "price": 75
    },
    {
        "id": 2,
        "title": "мясо",
        "quantity": 10,
        "price": 700
    },
    {
        "id": 3,
        "title": "nitro",
        "quantity": 5,
        "price": 68
    },
    {
        "id": 4,
        "title": "хлеб",
        "quantity": 3,
        "price": 30
    }
]

cart = {}

print("Добро пожаловать в наш магазин!\nУ нас есть:")

for product in catalog:
    print(f"Название: {product['title']}, кол-во: {product['quantity']}, цена: {product['price']}")

product_title = input("Введите название продукта, если хотите выйти (q): ").lower()

while product_title != 'q':
    product_quantity = int(input(f"Введите кол-во {product_title}: "))
    if product_quantity < 1:
        continue
    for product in catalog:
        if product.get("title") == product_title:
            if product["quantity"] < product_quantity:
                print(f"Недостаточно {product_title}, у нас есть {product['quantity']}")
                break
            if product_title in cart:
                is_delete = input("Вы хотите удалить продукт (y/n)? ").lower()
                if is_delete == 'y':
                    deleted_price = cart.pop(product_title)
                    product["quantity"] += deleted_price // product["price"]
                    print(deleted_price // product["price"])
                else:
                    cart[product_title] += product.get("price")*product_quantity
                    product["quantity"] -= product_quantity
            else:
                cart[product_title] = product.get("price")*product_quantity
                product["quantity"] -= product_quantity
            print(product)
    print(cart)
    product_title = input("Введите название продукта, если хотите выйти (q): ").lower()

print("Чек:")
print("======================================")
for title, price in cart.items():
    print(f"{title} - {price}")
print("Итого к оплате:", sum(cart.values()))
print("""
#######
# ### #
# ### #
#######
""")
print("======================================")
print("До свидания!")