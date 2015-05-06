from itertools import zip_longest
"""
This source code can act as base for a coding dojo.

It implements and test a function `iter_is_equal()` that take two sequences
as parameters and returns `True` if all there items are equal.

  >>> iter_is_equal([1, 2, 3], [1, 2, 3])
  True
  >>> iter_is_equal([1, 2, 3], [1, 3])
  False

The implementation provided works but is horribly inefficient. When passed
two generators, it produces all items of both generators.

The challenge is to compare one item after another (consequently using less
memory) and once two items differ, stop and return `False` (consequently
using less CPU).

For a proper function see <TODO>.

Written by Thomas Aglassinger, placed in the public domain.
"""
import unittest

def iter_is_equal(a, b):
    if a is b:
        return True
    return all(v_a == v_b for v_a, v_b in zip_longest(a, b, fillvalue=object()))


def some():
    yield 1
    yield 2
    yield None
    yield 3


def same():
    yield 1
    yield 2
    yield None
    yield 3


def less():
    yield 1
    yield 2
    yield None


def more():
    yield 1
    yield 2
    yield None
    yield 3
    yield 4


def nothing():
	# Yield no data.
	# HACK: Use yield in the code to change the function into a generator but
	#       never actually yield anything.
	if False:
		yield None


class IterIsEqualTest(unittest.TestCase):
    def test_some_is_equal(self):
        self.assertTrue(iter_is_equal(some(), some()))

    def test_identical_generators(self):
        gen = some()
        self.assertTrue(iter_is_equal(gen, gen))

    def test_same_is_equal(self):
	    self.assertTrue(iter_is_equal(some(), same()))

    def test_less_differs(self):
        self.assertFalse(iter_is_equal(some(), less()))

    def test_more_differs(self):
        self.assertFalse(iter_is_equal(some(), more()))

    def test_more_differs(self):
	    self.assertFalse(iter_is_equal(some(), more()))

    def test_nothing_differs(self):
        self.assertFalse(iter_is_equal(some(), nothing()))

    def test_different(self):
        self.assertFalse(iter_is_equal([1], [2]))

    def test_secret_handling(self):
        self.assertTrue(iter_is_equal(['secrect_default'], [ 'secrect_default']))

    def test_secret_obj_handling(self):
        i = object()
        self.assertFalse(iter_is_equal([i], [i,i]))

if __name__ == '__main__':
	unittest.main()
