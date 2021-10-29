import numpy
from decimal import *


x="10.000000"
count=6

print(Decimal(x.split('.')[0]+'.'+x.split('.')[1][0:count+2]))

