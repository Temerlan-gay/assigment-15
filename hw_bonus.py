class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserManagementSystem:
    def __init__(self):
        self.users = []

    def register(self, user):
        self.users.append(user)

    def delete_account(self, user):
        if user in self.users:
            self.users.remove(user)

    def update_info(self, user, new_info):
        user.name = new_info["name"]
        user.email = new_info["email"]


class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer


class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def calculate_score(self, user_answers):
        score = 0
        for q in self.questions:
            if user_answers[q.question] == q.correct_answer:
                score += 1
        return score


class Recipe:
    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps


class RecipeManagementSystem:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        if recipe in self.recipes:
            self.recipes.remove(recipe)

    def search_by_ingredient(self, ingredient):
        result = []
        for r in self.recipes:
            if ingredient in r.ingredients:
                result.append(r)
        return result


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def calculate_total(self):
        total = 0
        for p in self.products:
            total += p.price
        return total