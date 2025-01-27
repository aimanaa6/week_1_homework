# import the values that are required from math
from math import pi, tan, cos
# assign the values given to each component of the equation
# Acceleration due to gravity
g = 9.81
# height of the barrel
y0 = 1
# the velocity
v0 = 80
# the horizontal distance travelled
x = 0.5

theta_deg = 80

theta = theta_deg * (pi/180)

y = y0 + x * tan(theta) - (g * x**2) / (2 * (v0 * cos(theta))**2)
print(f"The height of the projectile is: {y} meters")



