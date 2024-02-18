import csv
import json
from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'price', 'quantity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for product in self.products:
                writer.writerow(product.to_dict())

    def read_from_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.products.append(Product(row['name'], float(row['price']), int(row['quantity'])))

    def save_to_json(self, filename):
        with open(filename, 'w') as jsonfile:
            json.dump([product.to_dict() for product in self.products], jsonfile)

    def read_from_json(self, filename):
        with open(filename) as jsonfile:
            data = json.load(jsonfile)
            for item in data:
                self.products.append(Product(item['name'], item['price'], item['quantity']))

    def get_products(self):
        return self.products
