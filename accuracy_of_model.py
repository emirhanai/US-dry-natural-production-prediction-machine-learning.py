import numpy
from sklearn.metrics import r2_score
import oil_years
import oil_production


year = oil_years.years
productions = oil_production.production
mymodel = numpy.poly1d(numpy.polyfit(year,productions, 18))
result = r2_score(productions, mymodel(year))


if (result * 100) > float(95):
  print("""Congratulations, the success rate of your
  '\r'artificial intelligence (machine learning) software is above 95%, as a result of {}""".format(result * 100))
else:
  print("""I am sad! This data and software do not meet Artificial Intelligence and Machine Learning standards! """)


#Accuracy of model: 96.72362502364177