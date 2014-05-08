import pytest

SYMBOLS = ('rock', 'paper', 'scissors')

BEAT_MAP = {
  ('rock', 'scissors'): 1,
  ('paper', 'rock'): 1,
  ('scissors', 'paper'): 1
}


def validate_symbol(symbol):
  if symbol not in SYMBOLS:
    raise ValueError

def winner(symbol1, symbol2):
  validate_symbol(symbol1)
  validate_symbol(symbol2)
  result = BEAT_MAP.get((symbol1, symbol2))
  if result is None and BEAT_MAP.get((symbol2, symbol1)) == 1:
    return 2
  return result if result is not None else 0

def test_exists():
  winner('rock', 'paper')

def test_only_two_players():
  with pytest.raises(TypeError):
    winner('rock', 'paper', 'paper')

def test_rock_beats_scissors():
  assert winner('rock', 'scissors') == 1

def test_scissors_loses_to_rock():
  assert winner('scissors', 'rock') == 2

def test_rock_and_rock_draw():
  assert winner('rock', 'rock') == 0

def test_paper_and_paper_draw():
  assert winner('paper', 'paper') == 0

def test_scissors_and_scissors_draw():
  assert winner('scissors', 'scissors') == 0

def test_paper_beats_rock():
  assert winner('paper', 'rock') == 1

def test_rock_loses_to_paper():
  assert winner('rock', 'paper') == 2

def test_scissors_beats_paper():
  assert winner('scissors', 'paper') == 1

def test_paper_loses_to_scissors():
  assert winner('paper', 'scissors') == 2

def test_flower_and_house_are_not_valid():
  with pytest.raises(ValueError):
    winner('flower', 'house')

def test_scissors_beats_paper():
  assert winner('scissors', 'paper') == 1

def test_flower_and_rock_are_not_valid():
  with pytest.raises(ValueError):
    winner('flower', 'rock')

def test_rock_and_house_are_not_valid():
  with pytest.raises(ValueError):
    winner('rock', 'house')
