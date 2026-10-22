import contextlib
import io
import unittest
from decimal import Decimal
from unittest.mock import patch

import main as tracker


class AmountTests(unittest.TestCase):
    @patch("builtins.input", side_effect=["abc", "-5", "0", "150"])
    def test_reprompts_until_valid(self, _mock):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(tracker.get_amount(), Decimal("150.00"))

    @patch("builtins.input", side_effect=["12.345"])
    def test_rounds_to_two_places(self, _mock):
        self.assertEqual(tracker.get_amount(), Decimal("12.35"))


class CategoryTests(unittest.TestCase):
    @patch("builtins.input", side_effect=["9", "0", "2"])
    def test_rejects_out_of_range_choice(self, _mock):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(tracker.get_category(), "Transport")


class SummaryTests(unittest.TestCase):
    def setUp(self):
        self.expenses = [
            {"amount": Decimal("150.00"), "category": "Food", "description": "Lunch"},
            {"amount": Decimal("50.50"), "category": "Food", "description": "Coffee"},
            {"amount": Decimal("1200.00"), "category": "Bills", "description": "Power"},
        ]

    def test_total_spending_is_exact(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            tracker.total_spending(self.expenses)
        self.assertIn("1400.50", buffer.getvalue())

    def test_category_summary_groups_by_category(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            tracker.category_summary(self.expenses)
        output = buffer.getvalue()
        self.assertIn("Food: 200.50", output)
        self.assertIn("Bills: 1200.00", output)

    def test_empty_state_does_not_crash(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            tracker.view_expenses([])
            tracker.category_summary([])
        self.assertIn("No expenses recorded yet.", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
