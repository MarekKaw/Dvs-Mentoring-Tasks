import decimal
from decimal import Decimal
from decimal import getcontext
getcontext().prec = 2
getcontext().rounding = decimal.ROUND_UP
PRECISION = 2


wzrost = float(input("Podaj swój wzrost w centymetrach: "))
wzrost /= 100
wzrost **= 2
waga = float(input("Podaj swoją wagę: "))
bmi = Decimal(waga) / Decimal(wzrost)
# bmi = waga / wzrost
# bmi = round(bmi, PRECISION)
print("Wartość Twojego BMI wynosi {}.".format(bmi))
