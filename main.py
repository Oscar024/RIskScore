import math

edad =28
sexo = 1 #mujer
bmi = 29.76222
sys = 123
dia = 82
fuma = 0
padres = 2
agedb = edad*dia



riesgo=1-math.exp(-math.exp((math.log(4) - (22.949536 + (-0.156412*edad )+( -0.202933*sexo) + (-0.033881*bmi) + (-0.05933*sys) + (-0.128468*dia) + (-0.190731*fuma) +  (-0.166121*padres) + (0.001624*agedb)))/0.876925))
riesgo = riesgo*100
print(riesgo)