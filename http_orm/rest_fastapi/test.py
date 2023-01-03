from settings import SessionLocal
from app.models import Product


# созздаем сессию, чтобы отправлять запросы
db = SessionLocal()

def create():
    new_product = Product(
            title='product1',
            price=10,
            quantity=2,
            description='...'
            )
    db.add(new_product) # добавляем запрос в сессию
    db.commit() # отправляем весь список запросов (сессию)

def listing():
    products = db.query(Product).all()
    print(products)

def get(id):
    product = db.query(Product).filter(Product.id == id).first()
    print(product)

def delete(id):
    product = db.query(Product).filter(Product.id == id).first()
    db.delete(product)
    db.commit()

# id_ = int(input("Введите id: "))
# print("DELETE product")
# delete(id_)
# print("DONE")

# id_ = int(input("Введите id: "))
# print("SELECT product")
# get(id_)
# print("DONE")

# print("SELECT products")
# listing()
# print("DONE")

# print("CREATE PRODUCT")
# create()
# print("DONE")