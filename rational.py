class RationalError(ZeroDivisionError):
    """Виключення для випадку, коли знаменник дорівнює нулю."""
    def __init__(self, message="Знаменник не може дорівнювати нулю"):
        super().__init__(message)

class RationalValueError(Exception):
    """Виключення для некоректних даних при операціях з раціональними числами."""
    def __init__(self, message="Некоректне значення для раціонального числа"):
        super().__init__(message)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise RationalError()
        self.numerator = numerator
        self.denominator = denominator
        self._normalize()

    def _normalize(self):
        d = gcd(self.numerator, self.denominator)
        self.numerator //= d
        self.denominator //= d
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise RationalValueError("Додавати можна лише об'єкти Rational")
        return Rational(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator
        )

    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise RationalValueError("Віднімати можна лише об'єкти Rational")
        return Rational(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator
        )

    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise RationalValueError("Множити можна лише об'єкти Rational")
        return Rational(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            raise RationalValueError("Ділити можна лише об'єкти Rational")
        if other.numerator == 0:
            raise RationalError("Ділення на нуль")
        return Rational(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Rational({self.numerator}, {self.denominator})"

class RationalList:
    def __init__(self):
        self.data = []

    def add(self, value):
        if not isinstance(value, Rational):
            raise RationalValueError("Можна додавати лише об'єкти Rational")
        self.data.append(value)

    def __str__(self):
        return "[" + ", ".join(str(r) for r in self.data) + "]"