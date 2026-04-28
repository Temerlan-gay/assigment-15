import unittest
import hw


class TestExercise(unittest.TestCase):

    def test_add_ingredient(self):
        pizza = hw.Pizza()
        pizza.add_ingredient("cheese")
        self.assertIn("cheese", pizza.ingredients)
        with self.assertRaises(ValueError):
            pizza.add_ingredient("cheese")

    def test_elevator_movement(self):
        elevator = hw.Elevator()
        elevator.go_up()
        self.assertEqual(elevator.get_current_floor(), 1)

    def test_stack(self):
        s = hw.Stack()
        self.assertTrue(s.is_empty())

    def test_bank(self):
        b = hw.BankAccount(100)
        self.assertEqual(b.check_balance(), 100)

    def test_person(self):
        p = hw.Person("A", 10)
        p.birthday()
        self.assertEqual(p.age, 11)


if __name__ == "__main__":
    unittest.main()