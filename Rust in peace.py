import copy

# 1)
class Temperature:
    def __init__(self, celsius: float = 0.0):
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._m_celsius if hasattr(self, '_m_celsius') else self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля (-273.15°C)")
        self._celsius = value
        self._m_celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        celsius_val = (value - 32) * 5 / 9
        self.celsius = celsius_val

t = Temperature(20)
print(t.celsius)
print(t.fahrenheit)

t.fahrenheit = 100
print(f"{t.celsius:.2f}")


# 2)
class User:
    def __init__(self, username: str, password: str):
        if not username or not isinstance(username, str):
            raise ValueError("Username должен быть непустой строкой")
        self._username = username
        self.password = password

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self):
        raise AttributeError("Пароль недоступен для чтения")

    @password.setter
    def password(self, value: str):
        if len(value) < 6:
            raise ValueError("Пароль должен содержать минимум 6 символов")
        self._password = value

    def check_password(self, pwd: str) -> bool:
        return self._password == pwd

user = User("alex_99", "secret123")
print(user.username)

try:
    print(user.password)
except AttributeError as e:
    print(e)

print(user.check_password("secret123"))
print(user.check_password("wrong_pwd"))


# 3)
class Cart:
    def __init__(self):
        self._items = []

    def add(self, name: str, price: float, qty: int = 1):
        for item in self._items:
            if item['name'] == name:
                item['qty'] += qty
                return
        self._items.append({'name': name, 'price': price, 'qty': qty})

    def remove(self, name: str):
        self._items = [item for item in self._items if item['name'] != name]

    @property
    def items(self) -> list:
        return copy.deepcopy(self._items)

    @property
    def total(self) -> float:
        return sum(item['price'] * item['qty'] for item in self._items)

cart = Cart()
cart.add("Ноутбук", 50000, 1)
cart.add("Мышка", 1500, 2)
print(cart.items)
print(cart.total)

my_items = cart.items
if my_items:
    my_items[0]['price'] = 0

print(cart.total)


# 4)
class Product:
    def __init__(self, price: float):
        self.price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = value

prod = Product(250)
print(prod.price)

try:
    prod.price = -10
except ValueError as e:
    print(e)
      
