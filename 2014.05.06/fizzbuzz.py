import pytest

def validate_input(number):
  if type(number) != int:
    raise TypeError("number must be an int instead of %s" % type(number))
    # raise TypeError("\U0001f4a9")   # not documented here
  if number < 1 or number > 100:
    raise ValueError("\U0001f4a9")   # not documented here


def converted(number):
  validate_input(number)
  if number % 15 == 0:
    return 'fizzbuzz'
  elif number % 3 == 0:
    return 'fizz'
  elif number % 5 == 0:
    return 'buzz'
  return number

def test_three_to_fizz():
  assert 'fizz' == converted(3)

def test_five_to_buzz():
  assert 'buzz' == converted(5)

def test_fifteen_to_fizzbuzz():
  assert 'fizzbuzz' == converted(15)

def test_1_to_1():
  assert 1 == converted(1)

def test_multiples_of_3():
  for i in range(3, 100, 3):
    if i % 15:
      assert 'fizz' == converted(i)

def test_multiples_of_5():
  for i in range(5, 100, 5):
    if i % 15:
      assert 'buzz' == converted(i)

def test_multiples_of_15():
  for i in range(15, 100, 15):
    assert 'fizzbuzz' == converted(i)

def test_non_special():
  for i in range(1, 100):
    if i % 3 and i % 5:
      assert converted(i) == i

def test_zero():
  with pytest.raises(ValueError):
    converted(0)

def test_negatives():
  with pytest.raises(ValueError):
    converted(-1)

def test_out_of_range():
  with pytest.raises(ValueError):
    converted(101)

def test_invalid_types():
  with pytest.raises(TypeError):
    converted(float('inf'))
    converted(float('-inf'))
    converted(float('NaN'))
    converted(None)
    converted('foobar')
