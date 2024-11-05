# Класс, представляющий товар
class Product:
    def __init__(self, name, price):
        self.name = name  # Название товара
        self.price = price  # Цена товара

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"

    def __eq__(self, other):
        return self.price == other.price  # Сравнение товаров по цене

    def __lt__(self, other):
        return self.price < other.price  # Для сортировки товаров по цене


# Класс, представляющий клиента
class Customer:
    def __init__(self, name):
        self.name = name  # Имя клиента
        self.orders = []  # Список заказов клиента

    def add_order(self, order):
        self.orders.append(order)  # Добавление заказа клиенту

    def __str__(self):
        return f"Customer {self.name}, Orders: {len(self.orders)}"

    def __repr__(self):
        return f"Customer(name='{self.name}')"


# Класс, представляющий заказ
class Order:
    total_orders = 0  # Класс хранит общее количество заказов

    def __init__(self, products):
        self.products = products  # Список товаров в заказе
        Order.total_orders += 1  # Увеличиваем общее количество заказов

    @classmethod
    def total_order_count(cls):
        return cls.total_orders  # Получить общее количество заказов

    def total_price(self):
        # Рассчитываем общую стоимость заказа
        return sum(product.price for product in self.products)

    def __str__(self):
        return f"Order with {len(self.products)} products, Total: ${self.total_price():.2f}"

    def __repr__(self):
        return f"Order(products={self.products})"


# Класс, представляющий скидку
class Discount:
    def __init__(self, description, discount_percent):
        self.description = description  # Описание скидки
        self.discount_percent = discount_percent  # Процент скидки

    @staticmethod
    def apply_discount(price, discount_percent):
        # Статический метод для применения скидки к цене
        return price * (1 - discount_percent / 100)

    def apply_to_order(self, order):
        # Применить скидку ко всем товарам в заказе
        discounted_total = sum(
            self.apply_discount(product.price, self.discount_percent)
            for product in order.products
        )
        return discounted_total

    def __str__(self):
        return f"Discount: {self.description} ({self.discount_percent}%)"

    def __repr__(self):
        return f"Discount(description='{self.description}', discount_percent={self.discount_percent})"


# Тестирование функционала
# Создаем несколько товаров
product1 = Product("Laptop", 1000)
product2 = Product("Phone", 500)
product3 = Product("Headphones", 150)

# Создаем клиента и заказ
customer = Customer("Alice")
order = Order([product1, product2, product3])
customer.add_order(order)

# Применяем скидку
discount = Discount("Seasonal Discount", 10)
discounted_price = discount.apply_to_order(order)

# Вывод информации
print(customer)
print(order)
print(f"Original Price: ${order.total_price():.2f}")
print(f"Discounted Price: ${discounted_price:.2f}")
print(f"Total Orders Count: {Order.total_order_count()}")
print(product1 < product2)  # Сравнение продуктов по цене
print(product1 == product2)
