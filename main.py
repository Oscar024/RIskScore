import math

edad =26
sexo = 0 #mujer
bmi = 26.1
sys = 110
dia = 75
fuma = 0
padres = 0
agedb = edad*dia



risk = 1-math.exp(-math.exp((math.log(4) - (22.9495 + (-0.1564*edad )+( -0.2029*sexo) + (-0.0339*bmi) + (-0.0593*sys) + (-0.1285*dia) + (-0.1907*fuma) +  (-0.1661*padres) + (0.0016*agedb))/0.8769)))
risk = risk*100
print(risk)