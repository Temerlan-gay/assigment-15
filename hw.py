import math
import random


class Pizza:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            raise ValueError
        self.ingredients.append(ingredient)


class Elevator:
    def __init__(self):
        self.floor = 0

    def go_up(self):
        self.floor += 1

    def go_down(self):
        if self.floor > 0:
            self.floor -= 1

    def get_current_floor(self):
        return self.floor


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise IndexError
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError
        self.balance -= amount

    def check_balance(self):
        return self.balance


class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Woof"


class Cat(Animal):
    def sound(self):
        return "Meow"


class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError
        return x / y


class Car:
    def __init__(self, speed, mileage):
        if speed < 0 or mileage < 0:
            raise ValueError
        self.speed = speed
        self.mileage = mileage


class Student:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self):
        self.students = []

    def enroll(self, student):
        self.students.append(student)


class Flight:
    def __init__(self, destination, departure):
        self.destination = destination
        self.departure = departure
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def change_destination(self, new_destination):
        self.destination = new_destination

    def delay(self, delay_time):
        h, m = map(int, self.departure.split(":"))
        h += delay_time
        self.departure = f"{h}:{m}"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self, title):
        for b in self.books:
            if b.title == title:
                return b


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, other):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def is_square(self):
        return self.height == self.width


class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


class Triangle:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.current_song = None
        self.index = -1

    def add_song(self, song):
        self.playlist.append(song)

    def play_song(self):
        if self.playlist:
            self.index = 0
            self.current_song = self.playlist[0]

    def next_song(self):
        if self.index + 1 < len(self.playlist):
            self.index += 1
            self.current_song = self.playlist[self.index]

    def shuffle(self):
        random.shuffle(self.playlist)


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, quantity):
        self.quantity += quantity

    def sell(self, quantity):
        if quantity > self.quantity:
            raise ValueError
        self.quantity -= quantity

    def check_stock(self):
        return self.quantity


class VideoGame:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def change_rating(self, rating):
        self.rating = rating

    def change_genre(self, genre):
        self.genre = genre


class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class SchoolStudent:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class School:
    def __init__(self):
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def get_all(self):
        return self.teachers + self.students


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = list(range(2, 15))
        self.cards = [Card(s, r) for s in suits for r in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def count(self):
        return len(self.cards)