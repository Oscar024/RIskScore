import math

edad =60
sexo = 1 #mujer
bmi = 32
sys = 128
dia = 85
fuma = 1
padres = 2
agedb = edad*dia



rirsk = 1-math.exp(-math.exp((math.log(4) - (22.9495 + (-0.1564*edad )+( -0.2029*sexo) + (-0.0339*bmi) + (-0.0593*sys) + (-0.1285*dia) + (-0.1907*fuma) +  (-0.1661*padres) + (0.0016*agedb))/0.8769)))

print(rirsk)