def mutable_link():
  """Return a functional implementation of a mutable linked list."""
  contents = empty
  def dispatch(message, value=None):
      nonlocal contents
      if message == 'len':
          return len_link(contents)
      elif message == 'getitem':
          return getitem_link(contents, value)
      elif message == 'push_first':
          contents = link(value, contents)
      elif message == 'pop_first':
          f = first(contents)
          contents = rest(contents)
          return f
      elif message == 'str':
          return join_link(contents, ", ")
  return dispatch

def to_mutable_link(source):
    '''Return a functional list with the same contents as source.'''
    s = mutable_link()
    for ele in reversed(source):
        s('push_first', ele)
    return s

def dictionary():
    '''Return a functional implementation of a dictionary.'''
    records = []
    def getitem(key):
        matches = [r for f in records if r[0] == key]
        if len(matches) == 1:
            key, value = matches[0]
            return value
    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in records if r[0] != key]
        records = non_matches + [[key, value]]
    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)
    return dispatch

def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw 
 
def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)


def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else: 
        return count_partitions(n-m, m) + count_partitions(n, m-1)

from math import gcd

def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx*dy + ny*dx, dx*dy)

def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def print_rational(x):
    print(numer(x), '/', denom(x))

def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

def rational(n, d):
    g = gcd(n, d)
    return (n//g, d//g)

def numer(x):
    return x[0]

def denom(x):
    return x[1]


def div(n, d):

  '''
  >>> q, r = div(2013, 10)
  >>> q
  201
  >>> r
  3
  '''
  return n//d, n%d

def fib(n):
  pre, cur = 0, 1
  while n > 0:
    pre, cur = cur, pre+cur
    n -= 1
    print(pre)
  return cur


def search(f):
  x = 0
  while True:
    if f(x):
      return x
    x += 1

def square(x):
  return x*x

def inverse(f):
  """Return a function g(y) that returns x such that f(x) == y
  >>> sqrt = inverse(square)
  >>> sqrt(16)
  4
  """
  def inverse_of_f(y):
    def is_inverse_of_y(x):
      return f(x) == y
    return search(is_inverse_of_y)
  return inverse_of_f
  # return lambda y: search(lambda x: f(x) == y)

def apply_twice(f, x):
  return f(f(x))

def make_adder(n):
  def adder(k):
    return k + n
  return adder

def compose(f, g):
  def h(x):
    return f(g(x))
  return h

def print_sums(n): 
  print(n)
  def next_sum(k):
    return print_sums(n+k)
  return next_sum

def curry2(f):
  """Return a curried version of the given two-arguments function"""
  def g(x):
    def h(y):
      return f(x, y)
    return h
  return g

def uncurry2(g):
  """Return a two-arguments version of the given curried function"""
  def f(x, y):
    return g(x)(y)
  return f

def remove(n, digit):
  kept, digits = 0, 0
  while n > 0:
    n, last = n // 10, n % 10
    if last != digit:
      kept = kept + last * pow(10, digits)
      digits += 1 
  print(kept)
  return kept

def sum_digits(n):
  if n<10:
    return n
  else:
    all_exclude_last, last = n // 10, n % 10
    return sum_digits(all_exclude_last) + last

def factorial(n):
  fact = 1
  i = 1
  while i <= n:
    fact *= i
    i += 1
  return fact
    
def fact(n):
  if n == 0:
    return 1
  else:
    return n * fact(n-1)

def cascade(n):
  if n < 10:
    print(n)
  else:
    print(n)
    cascade(n//10)
    print(n)

def cascade2(n):
  grow(n)
  print(n)
  shrink(n)

def f_then_g(f, g, n):
  if n: 
    f(n)
    g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

