def invert(x):
        result = 1/x  # Raises a ZeroDivisionError if x is 0
        print('Never printed if x is 0')
        return result
def invert_safe(x):
        try:
            return invert(x)
        except ZeroDivisionError as e:
            return str(e)

def newton_update(f, df):
        def update(x):
            return x - f(x) / df(x)
        return update 

class IterImproveError(Exception):
        def __init__(self, last_guess):
            self.last_guess = last_guess

def improve(update, done, guess=1, max_updates=1000):
        k = 0
        try:
            while not done(guess) and k < max_updates:
                guess = update(guess)
                k = k + 1
            return guess
        except ValueError:
            raise IterImproveError(guess)

def find_zero(f, df, guess=1):
        def done(x):
            return f(x) == 0
        try:
            return improve(newton_update(f, df), done, guess)
        except IterImproveError as e:
            return e.last_guess

from math import sqrt
print(find_zero(lambda x: 2*x*x + sqrt(x), lambda x: 4*x + 1/2 * 1/sqrt(x)))

from operator import add, mul, truediv

def divide_all(n, ds):
  try:
    return reduce(truediv, ds, n)
  except ZeroDivisionError:
    return float('inf')

def reduce(f, s, initial):
  """Combine elements of s using f starting with initial
  >>> reduce(mul, [2, 4, 8], 1)
  64
  >>> reduce(add, [1, 2, 3, 4], 0)
  10
  """
  for x in s:
    initial = f(x, initial)
  return initial

def reduce(f, s, initial):
  """Combine elements of s using f starting with initial
  >>> reduce(mul, [2, 4, 8], 1)
  64
  >>> reduce(add, [1, 2, 3, 4], 0)
  10
  """
  if not s:
    return initial
  else:
    first, rest = s[0], s[1:]
    return reduce(f, rest, f(initial, first))
