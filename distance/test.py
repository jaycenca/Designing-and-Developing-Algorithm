import calculation 
import math

result = calculation.distanceLatLong(43.73254, -79.30589, 43.73241, -79.30583)

test_calculateDestination = calculation.calculateDestination(43.73254, -79.30589, 45.0, 4.0)

print(test_calculateDestination)

test_calculateBearing = calculation.calculateBearing(43.73254, -79.30589, test_calculateDestination[0], test_calculateDestination[1])

#print(test_calculateBearing)
#print(result)
