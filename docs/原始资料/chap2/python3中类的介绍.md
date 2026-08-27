# Python3 中类的简要指南
## 目录

1. [类的基本概念](#section-1)  
2. [定义类](#section-2)  
3. [构造函数和初始化](#section-3)  
4. [类属性和实例属性](#section-4)  
5. [方法类型](#section-5)  
6. [继承](#section-6)  
7. [多态](#section-7)  
8. [封装](#section-8)  
9. [特殊方法](#section-9)  
10. [属性装饰器](#section-10)  
11. [抽象基类](#section-11)  
12. [类的高级用法](#section-12)

<a id="section-1"></a>
## 1. 类的基本概念
类是面向对象编程的核心概念，是创建对象的蓝图。类封装了数据（属性）和行为（方法），使代码更具组织性和可重用性。

``` python
# 最简单的类定义
class MyClass:
    pass

# 创建类的实例
obj = MyClass()
```

<a id="section-2"></a>
## 2. 定义类
使用 `class` 关键字定义类，类名通常采用驼峰命名法。

``` python
class Person:
    # 类属性
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age
    
    # 实例方法
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    # 类方法
    @classmethod
    def get_species(cls):
        return cls.species
    
    # 静态方法
    @staticmethod
    def is_adult(age):
        return age >= 18

# 使用类
person1 = Person("Alice", 25)
print(person1.introduce())  # Hi, I'm Alice and I'm 25 years old.
print(Person.get_species())  # Homo sapiens
print(Person.is_adult(20))  # True
```

<a id="section-3"></a>
## 3. 构造函数和初始化

__init__方法是类的构造函数，在创建对象时自动调用。

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 默认值
    
    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"
    
    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it."
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

# 使用示例
my_car = Car("Tesla", "Model S", 2023)
print(my_car.get_descriptive_name())  # 2023 Tesla Model S
print(my_car.read_odometer())  # This car has 0 miles on it.

my_car.update_odometer(100)
print(my_car.read_odometer())  # This car has 100 miles on it.

```

<a id="section-4"></a>
## 4. 类属性和实例属性
类属性是属于类的属性，实例属性是属于对象的属性。

```python
class Dog:
    # 类属性
    species = "Canis familiaris"
    count = 0  # 跟踪创建的实例数量
    
    def __init__(self, name, breed):
        # 实例属性
        self.name = name
        self.breed = breed
        Dog.count += 1  # 更新类属性
    
    def bark(self):
        return f"{self.name} says woof!"
    
    @classmethod
    def get_count(cls):
        return cls.count

# 使用示例
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris

# 修改类属性会影响所有实例
Dog.species = "Canis lupus familiaris"
print(dog1.species)  # Canis lupus familiaris

print(Dog.get_count())  # 2
```

<a id="section-5"></a>
## 5. 方法类型 

Python类中有三种方法：实例方法、类方法和静态方法。
```python
class Calculator:
    # 类属性
    operation_count = 0
    
    def __init__(self, value=0):
        self.value = value
    
    # 实例方法 - 可以访问和修改实例和类属性
    def add(self, amount):
        self.value += amount
        Calculator.operation_count += 1
        return self.value
    
    # 类方法 - 可以访问和修改类属性
    @classmethod
    def get_operation_count(cls):
        return cls.operation_count
    
    @classmethod
    def from_string(cls, string_value):
        return cls(float(string_value))
    
    # 静态方法 - 不能访问实例或类属性，只是普通函数
    @staticmethod
    def is_even(number):
        return number % 2 == 0

# 使用示例
calc1 = Calculator(10)
calc1.add(5)  # 15

calc2 = Calculator.from_string("20")
print(calc2.value)  # 20.0

print(Calculator.get_operation_count())  # 1
print(Calculator.is_even(4))  # True
```
<a id="section-6"></a>
## 6. 继承
继承允许一个类（子类）继承另一个类（父类）的属性和方法。

```python
# 基类
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

# 派生类
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"
    
    def purr(self):
        return f"{self.name} is purring..."

# 多级继承
class Puppy(Dog):
    def speak(self):
        return f"{self.name} says yip yip!"

# 使用示例
animals = [Dog("Buddy"), Cat("Whiskers"), Puppy("Spot")]

for animal in animals:
    print(animal.speak())

# 输出:
# Buddy says woof!
# Whiskers says meow!
# Spot says yip yip!

print(isinstance(animals[0], Animal))  # True
print(issubclass(Puppy, Animal))  # True
```
<a id="section-7"></a>
# 7. 多态
多态允许不同类的对象以相同的接口调用方法。

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

# 多态示例 - 不同对象，相同方法名
shapes = [Rectangle(3, 4), Circle(5)]

for shape in shapes:
    print(f"Area: {shape.area():.2f}")

# 输出:
# Area: 12.00
# Area: 78.54
```
<a id="section-8"></a>
## 8. 封装
封装通过将数据和方法绑定在一起，并限制对某些组件的访问来保护对象的完整性。

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # 私有属性
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance

# 使用示例
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # 1300

# 尝试直接访问私有属性会失败
# print(account.__balance)  # AttributeError
```
<a id="section-9"></a>
# 9. 特殊方法
特殊方法（魔术方法）允许自定义类的行为，如运算符重载。特殊方法以双下划线开头和结尾，用于实现类的特定行为。

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

# 使用示例
v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1)  # Vector(2, 3)
print(v1 + v2)  # Vector(6, 8)
print(v1 * 3)  # Vector(6, 9)
print(v1 == Vector(2, 3))  # True
print(len(v1))  # 3 (近似)
```

<a id="section-10"></a>
## 10. 属性装饰器
属性装饰器用于将方法转换为属性，允许通过属性访问方法的结果。@property装饰器允许将方法当作属性访问。

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

# 使用示例
temp = Temperature(25)
print(temp.celsius)  # 25
print(temp.fahrenheit)  # 77.0

temp.fahrenheit = 100
print(temp.celsius)  # 37.777...
```
<a id="section-11"></a>
## 11. 抽象基类
抽象基类（ABC）用于定义接口，强制子类实现特定方法

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

# 不能直接实例化抽象类
# shape = Shape()  # TypeError

# 必须实现所有抽象方法
square = Square(5)
print(square.area())  # 25
print(square.perimeter())  # 20
```

<a id="section-12"></a>
## 12. 类的高级用法

```python
# 多重继承
class A:
    def method(self):
        return "A method"

class B:
    def method(self):
        return "B method"

class C(A, B):
    def method(self):
        return super().method()  # 调用A的方法，因为A在继承列表中排在前面

# 使用示例
c = C()
print(c.method())  # A method

# 查看方法解析顺序(MRO)
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

# 动态创建类
def create_class(class_name, base_classes=(), attributes=None):
    if attributes is None:
        attributes = {}
    return type(class_name, base_classes, attributes)

# 使用type动态创建类
DynamicClass = create_class('DynamicClass', (), {'x': 42, 'hello': lambda self: f"Hello, x = {self.x}"})
obj = DynamicClass()
print(obj.hello())  # Hello, x = 42

# 元类示例
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['created_by'] = 'MetaClass'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.created_by)  # MetaClass
```

## 总结
Python的类系统提供了强大的面向对象编程能力。通过类，你可以：

1. 封装数据和行为

2. 实现代码重用通过继承

3. 实现多态性

4. 使用特殊方法自定义类行为

5. 使用属性装饰器创建更简洁的API

6. 使用抽象基类定义接口

7. 掌握这些概念将帮助你编写更加模块化、可维护和可扩展的代码。

