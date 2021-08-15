import numpy
import oil_years
import oil_production


year = oil_years.years
productions = oil_production.production

mymodel = numpy.poly1d(numpy.polyfit(year, productions, 18))


run_prediction = mymodel(2028)
print(run_prediction)

#2022 = 3121150.0
#2023 = 3266480.625
#2024 = 3386635.9375
#2025 = 3463634.5625
#2026 = 3475001.625
#2027 = 3393293.1875


