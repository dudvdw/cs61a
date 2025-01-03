class A:
  z = -1
  def f(self, x):
    return B(x-1)

class B(A):
  n = 4
  def __init__(self, y):
    if y:
      self.z = self.f(y)
    else:
      self.z = C(y+1)

class C(B):
  def f(self, x):
    return x

a = A()
b = B(1)
b.n = 5

print(C(2).n)
print(a.z == C.z)
print(a.z == b.z)

class Account:
  interest = 0.02
  def __init__(self, account_holder):
    self.balance = 0
    self.holder = account_holder