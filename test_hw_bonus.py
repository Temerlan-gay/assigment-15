import unittest
from hw_bonus import User, UserManagementSystem, Question, Quiz, Recipe, RecipeManagementSystem, Product, ShoppingCart


class TestBonus(unittest.TestCase):

    def test_user(self):
        system = UserManagementSystem()
        u = User("a", "b")
        system.register(u)
        self.assertIn(u, system.users)

    def test_quiz(self):
        q = Quiz()
        question = Question("Q", ["a", "b"], "a")
        q.add_question(question)
        score = q.calculate_score({"Q": "a"})
        self.assertEqual(score, 1)

    def test_recipe(self):
        r = RecipeManagementSystem()
        rec = Recipe("r", ["salt"], ["cook"])
        r.add_recipe(rec)
        self.assertIn(rec, r.recipes)

    def test_cart(self):
        c = ShoppingCart()
        p = Product("apple", 10)
        c.add_product(p)
        self.assertEqual(c.calculate_total(), 10)


if __name__ == "__main__":
    unittest.main()