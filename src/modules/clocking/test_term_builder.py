import unittest

from modules.clocking.term_builder import Var, op, Op, Const


class TestTermBuilder(unittest.TestCase):
    def test_basic(self):
        a = Var()
        self.assertEqual(a.vars(), {a})

    def test_var_repr(self):
        a = Var(iterator=range(0, 1))
        self.assertEqual(repr(a), "<Var a iterator=range(0, 1)>")

    def test_op_repr(self):
        op = Op(first_operand="a", operation="__mul__", other_operands=["b", "c"])
        self.assertEqual(repr(op), "<Op  'a'.__mul__('b', 'c')>")

    def test_multiplication(self):
        a = Var()
        b = Var()
        self.assertEqual((a * b).vars(), {a, b})
        self.assertTrue("__mul__" in (a * b)._function_part()[0])

    def test_get_function(self):
        a = Var()
        self.assertEqual((a * 10).get_function(a)(10), 100)

    def test_eval(self):
        a = Var()
        self.assertEqual(a.eval(a=1), 1)

        b = Var()
        self.assertEqual((a * b).eval(a=4, b=3), 12)
        self.assertEqual((a * b * b).eval(a=10, b=2), 40)
        self.assertEqual((a / 10 * b).eval(a=10, b=2), 2)
        self.assertEqual(op.round(10 / 3).eval(), 3)

    def test_get_vars(self):
        a = Var()
        b = Var()
        c = Var()
        self.assertEqual((a * (b * c)).vars(), {a, b, c})
        self.assertEqual((a * b * c).vars(), {a, b, c})

    # this is rather separate
    def test_op_builder(self):
        self.assertEqual(op.round(1), Op(operation="round", first_operand=None, other_operands=[Const(1)]))
