import numpy
import matplotlib.pyplot as plt
import oil_years
import oil_production
import logging


logging.basicConfig(
    filename='emirhan-polynomial.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s',
    level = logging.DEBUG
)


year = oil_years.years
productions = oil_production.production

mymodel = numpy.poly1d(numpy.polyfit(year, productions, 57))

myline = numpy.linspace(2002, 2021, 100)

plt.scatter(year, productions)

plt.plot(myline, mymodel(myline))

plt.show()
