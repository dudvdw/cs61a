class Complex(Number):
  def add(self, other):
      return ComplexRI(self.real + other.real, self.imag + other.imag)
  def mul(self, other):
      magnitude = self.magnitude * other.magnitude
      return ComplexMA(magnitude, self.angle + other.angle)

from math import atan2
class ComplexRI(Complex):
  def __init__(self, real, imag):
      self.real = real
      self.imag = imag
  @property
  def magnitude(self):
      return (self.real ** 2 + self.imag ** 2) ** 0.5
  @property
  def angle(self):
      return atan2(self.imag, self.real)
  def __repr__(self):
      return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)
  
from math import sin, cos, pi
class ComplexMA(Complex):
  def __init__(self, magnitude, angle):
      self.magnitude = magnitude
      self.angle = angle
  @property
  def real(self):
      return self.magnitude * cos(self.angle)
  @property
  def imag(self):
      return self.magnitude * sin(self.angle)
  def __repr__(self):
      return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle/pi)

from fractions import gcd
class Rational(Number):
  def __init__(self, numer, denom):
      g = gcd(numer, denom)
      self.numer = numer // g
      self.denom = denom // g
  def __repr__(self):
      return 'Rational({0}, {1})'.format(self.numer, self.denom)
  def add(self, other):
      nx, dx = self.numer, self.denom
      ny, dy = other.numer, other.denom
      return Rational(nx * dy + ny * dx, dx * dy)
  def mul(self, other):
      numer = self.numer * other.numer
      denom = self.denom * other.denom
      return Rational(numer, denom)

def is_real(c):
  """Return whether c is a real number with no imaginary part."""
  if isinstance(c, ComplexRI):
      return c.imag == 0
  elif isinstance(c, ComplexMA):
      return c.angle % pi == 0

def add_complex_and_rational(c, r):
  return ComplexRI(c.real + r.numer/r.denom, c.imag)

def mul_complex_and_rational(c, r):
  r_magnitude, r_angle = r.numer/r.denom, 0
  if r_magnitude < 0:
      r_magnitude, r_angle = -r_magnitude, pi
  return ComplexMA(c.magnitude * r_magnitude, c.angle + r_angle)

def add_rational_and_complex(r, c):
  return add_complex_and_rational(c, r)

def mul_rational_and_complex(r, c):
  return mul_complex_and_rational(c, r)

def rational_to_complex(r):
  return ComplexRI(r.numer/r.denom, 0)
  
class Number:
  def __add__(self, other):
      x, y = self.coerce(other)
      return x.add(y)
  def __mul__(self, other):
      x, y = self.coerce(other)
      return x.mul(y)
  def coerce(self, other):
      if self.type_tag == other.type_tag:
          return self, other
      elif (self.type_tag, other.type_tag) in self.coercions:
          return (self.coerce_to(other.type_tag), other)
      elif (other.type_tag, self.type_tag) in self.coercions:
          return (self, other.coerce_to(self.type_tag))
  def coerce_to(self, other_tag):
      coercion_fn = self.coercions[(self.type_tag, other_tag)]
      return coercion_fn(self)
  coercions = {('rat', 'com'): rational_to_complex}