from product_manager import ProductManager
from product import Product

class ConsoleApp:
    def __init__(self):
        self.product_manager = ProductManager()

    def add_product(self):
        name = input("Введите название товара: ")
        price = float(input("Введите цену товара: "))
        quantity = int(input("Введите количество товара: "))
        product = Product(name, price, quantity)
        self.product_manager.add_product(product)
        self.product_manager.save_to_csv("products.csv")
        self.product_manager.save_to_json("products.json")
        print("Товар добавлен успешно.")

    def show_products(self):
        products = self.product_manager.get_products()
        if products:
            print("Список товаров:")
            for i, product in enumerate(products, start=1):
                print(f"{i}. {product.name} - Цена: {product.price}, Количество: {product.quantity}")
        else:
            print("Список товаров пуст.")

    def run(self):
        while True:
            print("\nМеню:")
            print("1. Добавить товар")
            print("2. Показать список товаров")
            print("3. Выход")
            choice = input("Выберите действие: ")

            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.show_products()
            elif choice == '3':
                print("Выход из программы.")
                break
            else:
                print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    app = ConsoleApp()
    app.run()
