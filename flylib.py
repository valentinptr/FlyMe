from math import cos, radians, sin


def FacteurBase(speed):
    return 60 / speed


def TempsVol(fb, distance):
    return round(fb * distance)


def VentEffectif(alpha, Vw):
    return Vw * cos(radians(alpha))


def VentArriere(alpha, Vw):
    return Vw * sin(radians(alpha))


def DeriveMax(Vw, fb):
    return fb * Vw


def Derive(X, alpha):
    return X * sin(radians(alpha))


def VitesseSol(Vp, Ve):
    return Vp - Ve


def AngleVent(Rm, Dw):
    return (Rm - Dw) % 360


def ConsoMinutes(conso):
    return conso / 60


def ConsoBranche(consomn, tps):
    return round(consomn * tps)


def PoidsConso(conso):
    return conso * 0.72


def LitresToGallons(l):
    return round(l / 3.7854, 2)


def GallonsToLitres(usg):
    return round(3.7854 * usg, 2)


def CalculTrajet(parcour, Vw, Dw, Vp, conso):
    TpsVol = 0
    ConsoTt = 0
    ConsoMn = ConsoMinutes(conso)
    for i in range(len(parcour)):
        Tsv = TempsVol(FacteurBase(Vp), parcour[i][1])
        Ve = VentEffectif(AngleVent(parcour[i][0], Dw), Vw)
        Vs = VitesseSol(Vp, Ve)
        Tav = TempsVol(FacteurBase(Vs), parcour[i][1])
        ConsoBr = ConsoBranche(ConsoMn, Tav)
        TpsVol += Tav
        ConsoTt += ConsoBr
        print(
            f'Branche {i + 1}, Rm = {parcour[i][0]}°, Dist = {parcour[i][1]}Nm, Tsv = {Tsv}m, Tav = {Tav}m, Consommation : {LitresToGallons(ConsoBr)}usg')
    print(
        f'Temps total de vol : {int(TpsVol)} minutes pour une consommation totale de {LitresToGallons(ConsoTt)}usg et un poids de {int(PoidsConso(ConsoTt))}kg')
