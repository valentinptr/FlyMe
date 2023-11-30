from flylib import CalculTrajet

Vp = 100 #knots
Vw = 5 #knots
Dw = 180 #degres
Trajet = [
    [253, 9],
    [273, 18],
    [273, 16],
    [273, 15],
    [101, 17],
    [101, 16],
    [101, 8],
    [61, 11],
    [73, 9]
]
conso = 35 #l/h

CalculTrajet(Trajet, Vw, Dw, Vp, conso)