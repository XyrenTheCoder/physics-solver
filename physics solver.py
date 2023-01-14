#----------IMPORTS----------#
from math import sqrt
from constants import *
from standard_units import *
#----------END OF IMPORTS----------#

#----------CONVERTERS----------#
#power to energy
def PtoQ(P : str, t : str):
    if P == None: pass
    elif not P.isalnum() and P.split()[1].lower() not in StandardUnits.UNITP:
        raise UnitError
    elif P.endswith("MW") or P.endswith("mw"):
        P = float(P.split()[0]) * 1000000
    elif P.endswith("kW") or P.endswith("kw"):
        P = float(P.split()[0]) * 1000
    elif P.endswith("W") or P.endswith("w"):
        P = float(P.split()[0])
    else:
        P = float(P)

    if t == None: pass
    elif not t.isalnum() and t.split()[1].lower() not in StandardUnits.UNITt:
        raise UnitError
    elif t.endswith("h"):
        t = float(t.split()[0]) * 3600
    elif t.endswith("mins"):
        t = float(t.split()[0]) * 60
    elif t.endswith("s"):
        t = float(t.split()[0])
    else:
        t = float(t)
    
    return print(f"{'%.5g' % (P * t / 1000000)} MJ or {'%.5g' % (P * t / 1000)} kJ or {'%.5g' % (P * t)} J")

#energy to power
def QtoP(Q : str, t : str):
    if Q == None: pass
    elif not Q.isalnum() and Q.split()[1].lower() not in StandardUnits.UNITQ:
        raise UnitError
    elif Q.endswith("MJ") or Q.endswith("mj") or Q.endswith("MW h") or Q.endswith("mw h"):
        Q = float(Q.split()[0]) * 1000000
    elif Q.endswith("kJ") or Q.endswith("kj") or Q.endswith("kW h") or Q.endswith("kw h"):
        Q = float(Q.split()[0]) * 1000
    elif Q.endswith("J") or Q.endswith("j") or Q.endswith("W h") or Q.endswith("w h"):
        Q = float(Q.split()[0])
    else:
        Q = float(Q)

    if t == None: pass
    elif not t.isalnum() and t.split()[1].lower() not in StandardUnits.UNITt:
        raise UnitError
    elif t.endswith("h"):
        t = float(t.split()[0]) * 3600
    elif t.endswith("mins"):
        t = float(t.split()[0]) * 60
    elif t.endswith("s"):
        t = float(t.split()[0])
    else:
        t = float(t)

    return print(f"{'%.5g' % (Q / t / 1000000)} MJ or {'%.5g' % (Q / t / 1000)} kJ or {'%.5g' % (Q / t)} J")

#celsius to fahrenheit
def CtoF(degc : float):
    degf = degc * 1.8 + 32
    return print(f"{degf} °F")

#celsius to kelvin
def CtoK(degc : float):
    k = degc + 273
    return print(f"{k} K")

#fahrenheit to celsius
def FtoC(degf : float):
    degc = degf / 1.8 - 32
    return print(f"{degc} °C")

#fahrenheit to kelvin
def FtoK(degf : float):
    k = (degf / 1.8 - 32) - 273
    return print(f"{k} K")

#kelvin to celsius
def KtoC(k : float):
    degc = k - 273
    return print(f"{degc} °C")

#kelvin to fahrenheit
def KtoF(degk : float):
    degf = (degk - 273) * 1.8 + 32
    return print(f"{degf} °F")
#----------END OF CONVERTERS----------#

#----------PHYSICS FUNCTIONS----------#
#energy transfer
def et(P : str = None, Q : str = None, t : str = None):
    if P == None: pass
    elif not P.isalnum() and P.split()[1].lower() not in StandardUnits.UNITP:
        raise UnitError
    elif P.endswith("MW") or P.endswith("mw"):
        P = float(P.split()[0]) * 1000000
    elif P.endswith("kW") or P.endswith("kw"):
        P = float(P.split()[0]) * 1000
    elif P.endswith("W") or P.endswith("w"):
        P = float(P.split()[0])
    else:
        P = float(P)

    if Q == None: pass
    elif not Q.isalnum() and Q.split()[1].lower() not in StandardUnits.UNITQ:
        raise UnitError
    elif Q.endswith("MJ") or Q.endswith("mj") or Q.endswith("MW h") or Q.endswith("mw h"):
        Q = float(Q.split()[0]) * 1000000
    elif Q.endswith("kJ") or Q.endswith("kj") or Q.endswith("kW h") or Q.endswith("kw h"):
        Q = float(Q.split()[0]) * 1000
    elif Q.endswith("J") or Q.endswith("j") or Q.endswith("W h") or Q.endswith("w h"):
        Q = float(Q.split()[0])
    else:
        Q = float(Q)
    
    if t == None: pass
    elif not t.isalnum() and t.split()[1].lower() not in StandardUnits.UNITt:
        raise UnitError
    elif t.endswith("h"):
        t = float(t.split()[0]) * 3600
    elif t.endswith("mins"):
        t = float(t.split()[0]) * 60
    elif t.endswith("s"):
        t = float(t.split()[0])
    else:
        t = float(t)

    if P == None and Q != None and t != None:
        P = Q / t
        #basic unit: watt
        return print(f"{'%.5g' % (P / 1000000)} MW or {'%.5g' % (P / 1000)} kW or {'%.5g' % (P)} W")

    elif P != None and Q == None and t != None:
        Q = P * t
        #basic unit: joule
        return print(f"{'%.5g' % (Q / 1000000)} MJ or {'%.5g' % (Q / 1000)} kJ or {'%.5g' % (Q)} J")
        
    elif P != None and Q != None and t == None:
        t = Q / P
        #basic unit: hours (?)
        return print(f"{'%.5g' % (t)} h or {'%.5g' % (t * 60)} mins or {'%.5g' % (t * 3600)} s")

#heat capacity
def hc(Q : str = None, C : str = None, dT : str = None):
    if Q == None: pass
    elif not Q.isalnum() and Q.split()[1].lower() not in StandardUnits.UNITQ:
        raise UnitError
    elif Q.endswith("MJ") or Q.endswith("mj") or Q.endswith("MW h") or Q.endswith("mw h"):
        Q = float(Q.split()[0]) * 1000000
    elif Q.endswith("kJ") or Q.endswith("kj") or Q.endswith("kW h") or Q.endswith("kw h"):
        Q = float(Q.split()[0]) * 1000
    elif Q.endswith("J") or Q.endswith("j") or Q.endswith("W h") or Q.endswith("w h"):
        Q = float(Q.split()[0])
    else:
        Q = float(Q)

    if C == None: pass
    elif not C.isalnum() and C.split()[1].lower() not in StandardUnits.UNITC:
        raise UnitError
    elif C.endswith("MJ degC-1") or C.endswith("mj degc-1"):
        C = float(C.split()[0]) * 1000000
    elif C.endswith("kJ degC-1") or C.endswith("kj degc-1"):
        C = float(C.split()[0]) * 1000
    elif C.endswith("J degC-1") or C.endswith("j degc-1"):
        C = float(C.split()[0])
    else:
        C = float(C)

    if dT == None: pass
    elif not dT.isalnum() and dT.split()[1].lower() not in StandardUnits.UNITdT:
        raise UnitError
    elif dT.endswith("degC") or dT.endswith("degc"):
        dT = float(dT.split()[0])
    else:
        dT = float(dT)

    if Q == None and C != None and dT != None:
        Q = C * dT
        #basic unit: joule
        return print(f"{'%.5g' % (Q / 1000000)} MJ or {'%.5g' % (Q / 1000)} kJ or {'%.5g' % (Q)} J")

    elif Q != None and C == None and dT != None:
        C = Q / dT
        #basic unit: joule degree celsius^-1
        return print(f"{'%.5g' % (C / 1000000)} MJ/°C or {'%.5g' % (C / 1000)} kJ/°C or {'%.5g' % (C)} J/°C")
        
    elif Q != None and C != None and dT == None:
        dT = Q / C
        #basic unit: degree celsius
        return print(f"{'%.5g' % (dT)} °C")

#specific heat capacity
def shc(Q : str = None, m : str = None, c : str = None, dT : str = None):
    if Q == None: pass
    elif not Q.isalnum() and Q.split()[1].lower() not in StandardUnits.UNITQ:
        raise UnitError
    elif Q.endswith("MJ") or Q.endswith("mj") or Q.endswith("MW h") or Q.endswith("mw h"):
        Q = float(Q.split()[0]) * 1000000
    elif Q.endswith("kJ") or Q.endswith("kj") or Q.endswith("kW h") or Q.endswith("kw h"):
        Q = float(Q.split()[0]) * 1000
    elif Q.endswith("J") or Q.endswith("j") or Q.endswith("W h") or Q.endswith("w h"):
        Q = float(Q.split()[0])
    else:
        Q = float(Q)

    if m == None: pass
    elif not m.isalnum() and m.split()[1].lower() not in StandardUnits.UNITm:
        raise UnitError
    elif m.endswith("kg"):
        m = float(m.split()[0])
    elif m.endswith("g"):
        m = float(m.split()[0]) / 1000
    else:
        m = float(m)

    if c == None: pass
    elif not c.isalnum() and c.split()[1].lower() not in StandardUnits.UNITc:
        raise UnitError
    elif c.endswith("MJ kg-1 degC-1") or c.endswith("mj kg-1 degc-1"):
        c = float(c.split()[0]) * 1000000
    elif c.endswith("kJ kg-1 degC-1") or c.endswith("kj kg-1 degc-1"):
        c = float(c.split()[0]) * 1000
    elif c.endswith("J kg-1 degC-1") or c.endswith("j kg-1 degc-1"):
        c = float(c.split()[0])
    else:
        c = float(c)

    if dT == None: pass
    elif not dT.isalnum() and dT.split()[1].lower() not in StandardUnits.UNITdT:
        raise UnitError
    elif dT.endswith("degC") or dT.endswith("degc"):
        dT = float(dT.split()[0])
    else:
        dT = float(dT)

    if Q == None and m != None and c != None and dT != None:
        Q = m * c * dT
        #basic unit: joule
        return print(f"{'%.5g' % (Q / 1000000)} MJ or {'%.5g' % (Q / 1000)} kJ or {'%.5g' % (Q)} J")

    elif Q != None and m == None and c != None and dT != None:
        m = Q / c / dT
        #basic unit: kg
        return print(f"{'%.5g' % (m)} kg or {'%.5g' % (m / 1000)} g")
        
    elif Q != None and m != None and c == None and dT != None:
        c = Q / m / dT
        #basic unit: joule kg^-1 degree celsius^-1
        return print(f"{'%.5g' % (c / 1000000)} MJ kg-1 °C-1 or {'%.5g' % (c /1000)} kJ kg-1 °C-1 or {'%.5g' % (c)} J kg-1 °C-1")

    elif Q != None and m != None and c != None and dT == None:
        dT = Q / m / c
        #basic unit: degree celsius
        return print(f"{'%.5g' % (dT)} °C")

#specific latent heat
def slh(l : str = None, Q : str = None, m : str = None):
    if l == None: pass
    elif not l.isalnum() and l.split()[1].lower() not in StandardUnits.UNITl:
        raise UnitError
    elif l.endswith("MJ kg-1") or l.endswith("mj kg-1"):
        l = float(l.split()[0]) * 1000000
    elif l.endswith("kJ kg-1") or l.endswith("kj kg-1"):
        l = float(l.split()[0]) * 1000
    elif l.endswith("J kg-1") or l.endswith("j kg-1"):
        l = float(l.split()[0])
    else:
        l = float(l)

    if Q == None: pass
    elif not Q.isalnum() and Q.split()[1].lower() not in StandardUnits.UNITQ:
        raise UnitError
    elif Q.endswith("MJ") or Q.endswith("mj") or Q.endswith("MW h") or Q.endswith("mw h"):
        Q = float(Q.split()[0]) * 1000000
    elif Q.endswith("kJ") or Q.endswith("kj") or Q.endswith("kW h") or Q.endswith("kw h"):
        Q = float(Q.split()[0]) * 1000
    elif Q.endswith("J") or Q.endswith("j") or Q.endswith("W h") or Q.endswith("w h"):
        Q = float(Q.split()[0])
    else:
        Q = float(Q)

    if m == None: pass
    elif not m.isalnum() and m.split()[1].lower() not in StandardUnits.UNITm:
        raise UnitError
    elif m.endswith("kg"):
        m = float(m.split()[0])
    elif m.endswith("g"):
        m = float(m.split()[0]) / 1000
    else:
        m = float(m)

    if l == None and Q != None and m != None:
        l = Q / m
        #basic unit: J kg-1
        return print(f"{'%.5g' % (l / 1000000)} MJ kg-1 or {'%.5g' % (l /1000)} kJ kg-1 or {'%.5g' % (l)} J kg-1")

    elif l != None and Q == None and m != None:
        Q = l * m
        #basic unit: joule
        return print(f"{'%.5g' % (Q / 1000000)} MJ or {'%.5g' % (Q / 1000)} kJ or {'%.5g' % (Q)} J")

    elif l != None and Q != None and m == None:
        m = Q / l
        #basic unit: kg
        return print(f"{'%.5g' % (m)} kg or {'%.5g' % (m / 1000)} g")

#total energy (E = ml + mcΔT)
def te(E : str = None, m : str = None, l : str = None, c : str = None, dT : str = None):
    if E == None: pass
    elif not E.isalnum() and E.split()[1].lower() not in StandardUnits.UNITE:
        raise UnitError
    elif E.endswith("MJ") or E.endswith("mj") or E.endswith("MW h") or E.endswith("mw h"):
        E = float(E.split()[0]) * 1000000
    elif E.endswith("kJ") or E.endswith("kj") or E.endswith("kW h") or E.endswith("kw h"):
        E = float(E.split()[0]) * 1000
    elif E.endswith("J") or E.endswith("j") or E.endswith("W h") or E.endswith("w h"):
        E = float(E.split()[0])
    else:
        E = float(E)

    if m == None: pass
    elif not m.isalnum() and m.split()[1].lower() not in StandardUnits.UNITm:
        raise UnitError
    elif m.endswith("kg"):
        m = float(m.split()[0])
    elif m.endswith("g"):
        m = float(m.split()[0]) / 1000
    else:
        m = float(m)

    if l == None: pass
    elif not l.isalnum() and l.split()[1].lower() not in StandardUnits.UNITl:
        raise UnitError
    elif l.endswith("MJ kg-1") or l.endswith("mj kg-1"):
        l = float(l.split()[0]) * 1000000
    elif l.endswith("kJ kg-1") or l.endswith("kj kg-1"):
        l = float(l.split()[0]) * 1000
    elif l.endswith("J kg-1") or l.endswith("j kg-1"):
        l = float(l.split()[0])
    else:
        l = float(l)

    if c == None: pass
    elif not c.isalnum() and c.split()[1].lower() not in StandardUnits.UNITc:
        raise UnitError
    elif c.endswith("MJ kg-1 degC-1") or c.endswith("mj kg-1 degc-1"):
        c = float(c.split()[0]) * 1000000
    elif c.endswith("kJ kg-1 degC-1") or c.endswith("kj kg-1 degc-1"):
        c = float(c.split()[0]) * 1000
    elif c.endswith("J kg-1 degC-1") or c.endswith("j kg-1 degc-1"):
        c = float(c.split()[0])
    else:
        c = float(c)

    if dT == None: pass
    elif not dT.isalnum() and dT.split()[1].lower() not in StandardUnits.UNITdT:
        raise UnitError
    elif dT.endswith("degC") or dT.endswith("degc"):
        dT = float(dT.split()[0])
    else:
        dT = float(dT)

    if E == None and m != None and l != None and c != None and dT != None:
        E = (m * l) + (m * c * dT)
        #basic unit: joule
        return print(f"{'%.5g' % (E / 1000000)} MJ or {'%.5g' % (E / 1000)} kJ or {'%.5g' % (E)} J")

    elif E != None and m == None and l != None and c != None and dT != None:
        m = E / (l + (c * dT))
        #basic unit: kg
        return print(f"{'%.5g' % (m)} kg or {'%.5g' % (m / 1000)} g")

    elif E != None and m != None and l == None and c != None and dT != None:
        l = (E / m) - (c * dT)
        #basic unit: joule kg-1
        return print(f"{'%.5g' % (l / 1000000)} MJ kg-1 or {'%.5g' % (l /1000)} kJ kg-1 or {'%.5g' % (l)} J kg-1")

    elif E != None and m != None and l != None and c == None and dT != None:
        c = ((E / m) - l) / dT
        #basic unit: joule kg^-1 degree celsius^-1
        return print(f"{'%.5g' % (c / 1000000)} MJ kg-1 °C-1 or {'%.5g' % (c /1000)} kJ kg-1 °C-1 or {'%.5g' % (c)} J kg-1 °C-1")

    elif E != None and m != None and l != None and c != None and dT == None:
        dT = ((E / m) - l) / c
        #basic unit: degree celsius
        return print(f"{'%.5g' % (dT)} °C")

#total energy2 (E = ml + CΔT)
def te2(E : str = None, m : str = None, l : str = None, C : str = None, dT : str = None):
    if E == None: pass
    elif not E.isalnum() and E.split()[1].lower() not in StandardUnits.UNITE:
        raise UnitError
    elif E.endswith("MJ") or E.endswith("mj") or E.endswith("MW h") or E.endswith("mw h"):
        E = float(E.split()[0]) * 1000000
    elif E.endswith("kJ") or E.endswith("kj") or E.endswith("kW h") or E.endswith("kw h"):
        E = float(E.split()[0]) * 1000
    elif E.endswith("J") or E.endswith("j") or E.endswith("W h") or E.endswith("w h"):
        E = float(E.split()[0])
    else:
        E = float(E)

    if m == None: pass
    elif not m.isalnum() and m.split()[1].lower() not in StandardUnits.UNITm:
        raise UnitError
    elif m.endswith("kg"):
        m = float(m.split()[0])
    elif m.endswith("g"):
        m = float(m.split()[0]) / 1000
    else:
        m = float(m)

    if l == None: pass
    elif not l.isalnum() and l.split()[1].lower() not in StandardUnits.UNITl:
        raise UnitError
    elif l.endswith("MJ kg-1") or l.endswith("mj kg-1"):
        l = float(l.split()[0]) * 1000000
    elif l.endswith("kJ kg-1") or l.endswith("kj kg-1"):
        l = float(l.split()[0]) * 1000
    elif l.endswith("J kg-1") or l.endswith("j kg-1"):
        l = float(l.split()[0])
    else:
        l = float(l)

    if C == None: pass
    elif not C.isalnum() and C.split()[1].lower() not in StandardUnits.UNITC:
        raise UnitError
    elif C.endswith("MJ degC-1") or C.endswith("mj degc-1"):
        C = float(C.split()[0]) * 1000000
    elif C.endswith("kJ degC-1") or C.endswith("kj degc-1"):
        C = float(C.split()[0]) * 1000
    elif C.endswith("J degC-1") or C.endswith("j degc-1"):
        C = float(C.split()[0])
    else:
        C = float(C)

    if dT == None: pass
    elif not dT.isalnum() and dT.split()[1].lower() not in StandardUnits.UNITdT:
        raise UnitError
    elif dT.endswith("degC") or dT.endswith("degc"):
        dT = float(dT.split()[0])
    else:
        dT = float(dT)

    if E == None and m != None and l != None and C != None and dT != None:
        E = (m * l) + (C * dT)
        #basic unit: joule
        return print(f"{'%.5g' % (E / 1000000)} MJ or {'%.5g' % (E / 1000)} kJ or {'%.5g' % (E)} J")

    elif E != None and m == None and l != None and C != None and dT != None:
        m = (E - (C * dT)) / l
        #basic unit: kg
        return print(f"{'%.5g' % (m)} kg or {'%.5g' % (m / 1000)} g")

    elif E != None and m != None and l == None and C != None and dT != None:
        l = (E - (C * dT)) / m
        #basic unit: joule kg-1
        return print(f"{'%.5g' % (l / 1000000)} MJ kg-1 or {'%.5g' % (l /1000)} kJ kg-1 or {'%.5g' % (l)} J kg-1")

    elif E != None and m != None and l != None and C == None and dT != None:
        C = (E - (m * l)) / dT
        #basic unit: joule kg^-1 degree celsius^-1
        return print(f"{'%.5g' % (C / 1000000)} MJ kg-1 °C-1 or {'%.5g' % (C /1000)} kJ kg-1 °C-1 or {'%.5g' % (C)} J kg-1 °C-1")

    elif E != None and m != None and l != None and C != None and dT == None:
        dT = (E - (m * l)) / C
        #basic unit: degree celsius
        return print(f"{'%.5g' % (dT)} °C")

#pressure force
def pf(p : str = None, F : str = None, A : str = None):
    if p == None: pass
    elif not p.isalnum() and p.split()[1].lower() not in StandardUnits.UNITp:
        raise UnitError
    elif p.endswith("MPa") or p.endswith("mpa"):
        p = float(p.split()[0]) * 1000000
    elif p.endswith("kPa") or p.endswith("kpa"):
        p = float(p.split()[0]) * 1000
    elif p.endswith("Pa") or p.endswith("pa") or p.endswith("N m-2") or p.endswith("n m-2"):
        p = float(p.split()[0])
    else:
        p = float(p)

    if F == None: pass
    elif not F.isalnum() and F.split()[1].lower() not in StandardUnits.UNITF:
        raise UnitError
    elif F.endswith("N") or F.endswith("n"):
        F = float(F.split()[0])
    else:
        F = float(F)

    if A == None: pass
    elif not A.isalnum() and A.split()[1].lower() not in StandardUnits.UNITA:
        raise UnitError
    elif A.endswith("cm^2"):
        A = float(A.split()[0]) * 10000
    elif A.endswith("m^2"):
        A = float(A.split()[0])
    else:
        A = float(A)

    if p == None and F != None and A != None:
        p = F / A
        #basic unit: Pa
        return print(f"{'%.5g' % (p / 1000)} kPa or {'%.5g' % (p)} Pa")

    elif p != None and F == None and A != None:
        F = p * A
        #basic unit: N
        return print(f"{'%.5g' % (F)} N")

    elif p != None and F != None and A == None:
        A = F / p
        #basic unit: m^2
        return print(f"{'%.5g' % (A)} m^2 or {'%.5g' % (A * 10000)} cm^2")

#boyle's law
def bl(p1 : str = None, V1 : str = None, p2 : str = None, V2 : str = None):
    if p1 == None: pass
    elif not p1.isalnum() and p1.split()[1].lower() not in StandardUnits.UNITp:
        raise UnitError
    elif p1.endswith("MPa") or p1.endswith("mpa"):
        p1 = float(p1.split()[0]) * 1000000
    elif p1.endswith("kPa") or p1.endswith("kpa"):
        p1 = float(p1.split()[0]) * 1000
    elif p1.endswith("Pa") or p1.endswith("pa") or p1.endswith("N m-2") or p1.endswith("n m-2"):
        p1 = float(p1.split()[0])
    else:
        p1 = float(p1)

    if V1 == None: pass
    elif not V1.isalnum() and V1.split()[1].lower() not in StandardUnits.UNITV:
        raise UnitError
    elif V1.endswith("cm^3"):
        V1 = float(V1.split()[0]) / 1000000
    elif V1.endswith("m^3"):
        V1 = float(V1.split()[0])
    else:
        V1 = float(V1)

    if p2 == None: pass
    elif not p2.isalnum() and p2.split()[1].lower() not in StandardUnits.UNITp:
        raise UnitError
    elif p2.endswith("MPa") or p2.endswith("mpa"):
        p2 = float(p2.split()[0]) * 1000000
    elif p2.endswith("kPa") or p2.endswith("kpa"):
        p2 = float(p2.split()[0]) * 1000
    elif p2.endswith("Pa") or p2.endswith("pa") or p2.endswith("N m-2") or p2.endswith("n m-2"):
        p2 = float(p2.split()[0])
    else:
        p2 = float(p2)

    if V2 == None: pass
    elif not V2.isalnum() and V2.split()[1].lower() not in StandardUnits.UNITV:
        raise UnitError
    elif V2.endswith("cm^3"):
        V2 = float(V2.split()[0]) / 1000000
    elif V2.endswith("m^3"):
        V2 = float(V2.split()[0])
    else:
        V2 = float(V2)

    if p1 == None and V1 != None and p2 != None and V2 != None:
        p1 = (p2 * V2) / V1
        #basic unit: Pa
        return print(f"{'%.5g' % (p1 / 1000)} kPa or {'%.5g' % (p1)} Pa")

    elif p1 != None and V1 == None and p2 != None and V2 != None:
        V1 = (p2 * V2) / p1
        #basic unit: cm^3 or m^3 (if the input value of V2 is m^3, take m^3 as common unit (use the same unit as input)
        return print(f"{'%.5g' % (V1)} m^3 or {'%.5g' % (V1 * 1000000)} cm^3")

    elif p1 != None and V1 != None and p2 == None and V2 != None:
        p2 = (p1 * V1) / V2
        #basic unit: Pa
        return print(f"{'%.5g' % (p2 / 1000)} kPa or {'%.5g' % (p2)} Pa")

    elif p1 != None and V1 != None and p2 != None and V2 == None:
        V2 = (p1 * V1) / p2
        #basic unit: cm^3 or m^3 (if the input value of V1 is m^3, take m^3 as common unit (use the same unit as input))
        return print(f"{'%.5g' % (V2)} m^3 or {'%.5g' % (V2 * 1000000)} cm^3")

#pressure law
def pl(p1 : str = None, T1 : str = None, p2 : str = None, T2 : str = None):
    if p1 == None: pass
    elif not p1.isalnum() and p1.split()[1].lower() not in StandardUnits.UNITp:
        raise UnitError
    elif p1.endswith("MPa") or p1.endswith("mpa"):
        p1 = float(p1.split()[0]) * 1000000
    elif p1.endswith("kPa") or p1.endswith("kpa"):
        p1 = float(p1.split()[0]) * 1000
    elif p1.endswith("Pa") or p1.endswith("pa") or p1.endswith("N m-2") or p1.endswith("n m-2"):
        p1 = float(p1.split()[0])
    else:
        p1 = float(p1)

    if T1 == None: pass
    elif not T1.isalnum() and T1.split()[1].lower() not in StandardUnits.UNITT:
        raise UnitError
    elif T1.endswith("degC") or T1.endswith("degc"):
        T1 = float(T1.split()[0]) + 273
    elif T1.endswith("K") or T1.endswith("k"):
        T1 = float(T1.split()[0])
    else:
        T1 = float(T1)

    if p2 == None: pass
    elif not p2.isalnum() and p2.split()[1].lower() not in StandardUnits.UNITp:
        raise UnitError
    elif p2.endswith("MPa") or p2.endswith("mpa"):
        p2 = float(p2.split()[0]) * 1000000
    elif p2.endswith("kPa") or p2.endswith("kpa"):
        p2 = float(p2.split()[0]) * 1000
    elif p2.endswith("Pa") or p2.endswith("pa") or p2.endswith("N m-2") or p2.endswith("n m-2"):
        p2 = float(p2.split()[0])
    else:
        p2 = float(p2)

    if T2 == None: pass
    elif not T2.isalnum() and T2.split()[1].lower() not in StandardUnits.UNITT:
        raise UnitError
    elif T2.endswith("degC") or T2.endswith("degc"):
        T2 = float(T2.split()[0]) + 273
    elif T2.endswith("K") or T2.endswith("k"):
        T2 = float(T2.split()[0])
    else:
        T2 = float(T2)

    if p1 == None and T1 != None and p2 != None and T2 != None:
        p1 = (p2 / T2) * T1
        #basic unit: Pa
        return print(f"{'%.5g' % (p1 / 1000)} kPa or {'%.5g' % (p1)} Pa")

    elif p1 != None and T1 == None and p2 != None and T2 != None:
        T1 = (T2 / p2) * p1
        #basic unit: K
        return print(f"{T1} K")

    elif p1 != None and T1 != None and p2 == None and T2 != None:
        p2 = (p1 / T1) * T2
        #basic unit: Pa
        return print(f"{'%.5g' % (p2 / 1000)} kPa or {'%.5g' % (p2)} Pa")

    elif p1 != None and T1 != None and p2 != None and T2 == None:
        T2 = (T1 / p1) * p2
        #basic unit: K
        return print(f"{T2} K")

#charles' law
def cl(V1 : str = None, T1 : str = None, V2 : str = None, T2 : str = None):
    if V1 == None: pass
    elif not V1.isalnum() and V1.split()[1].lower() not in StandardUnits.UNITV:
        raise UnitError
    elif V1.endswith("cm^3"):
        V1 = float(V1.split()[0]) / 1000000
    elif V1.endswith("m^3"):
        V1 = float(V1.split()[0])
    else:
        V1 = float(V1)

    if T1 == None: pass
    elif not T1.isalnum() and T1.split()[1].lower() not in StandardUnits.UNITT:
        raise UnitError
    elif T1.endswith("degC") or T1.endswith("degc"):
        T1 = float(T1.split()[0]) + 273
    elif T1.endswith("K") or T1.endswith("k"):
        T1 = float(T1.split()[0])
    else:
        T1 = float(T1)

    if V2 == None: pass
    elif not V2.isalnum() and V2.split()[1].lower() not in StandardUnits.UNITV:
        raise UnitError
    elif V2.endswith("cm^3"):
        V2 = float(V2.split()[0]) / 1000000
    elif V2.endswith("m^3"):
        V2 = float(V2.split()[0])
    else:
        V2 = float(V2)

    if T2 == None: pass
    elif not T2.isalnum() and T2.split()[1].lower() not in StandardUnits.UNITT:
        raise UnitError
    elif T2.endswith("degC") or T2.endswith("degc"):
        T2 = float(T2.split()[0]) + 273
    elif T2.endswith("K") or T2.endswith("k"):
        T2 = float(T2.split()[0])
    else:
        T2 = float(T2)

    if V1 == None and T1 != None and V2 != None and T2 != None:
        V1 = (V2 / T2) * T1
        #basic unit: m^3
        return print(f"{'%.5g' % (V1)} m^3 or {'%.5g' % (V1 * 1000000)} cm^3")

    elif V1 != None and T1 == None and V2 != None and T2 != None:
        T1 = (T2 / V2) * V1
        #basic unit: K
        return print(f"{T1} K")

    elif V1 != None and T1 != None and V2 == None and T2 != None:
        V2 = (V1 / T1) * T2
        #basic unit: m^3
        return print(f"{'%.5g' % (V2)} m^3 or {'%.5g' % (V2 * 1000000)} cm^3")

    elif V1 != None and T1 != None and V2 != None and T2 == None:
        T2 = (T1 / V1) * V2
        #basic unit: K
        return print(f"{T2} K")

#general gas law
def ggl(p : str = None, V : str = None, n : str = None, T : str = None):
    if p == None: pass
    elif not p.isalnum() and p.split()[1].lower() not in StandardUnits.UNITp:
        raise UnitError
    elif p.endswith("MPa") or p.endswith("mpa"):
        p = float(p.split()[0]) * 1000000
    elif p.endswith("kPa") or p.endswith("kpa"):
        p = float(p.split()[0]) * 1000
    elif p.endswith("Pa") or p.endswith("pa") or p.endswith("N m-2") or p.endswith("n m-2"):
        p = float(p.split()[0])
    else:
        p = float(p)

    if V == None: pass
    elif not V.isalnum() and V.split()[1].lower() not in StandardUnits.UNITV:
        raise UnitError
    elif V.endswith("cm^3"):
        V = float(V.split()[0]) / 1000000
    elif V.endswith("m^3"):
        V = float(V.split()[0])
    else:
        V = float(V)

    if n == None: pass
    elif not n.isalnum() and n.split()[1].lower() not in StandardUnits.UNITn:
        raise UnitError
    elif n.endswith("mol"):
        n = float(n.split()[0])
    else:
        n = float(n)

    if T == None: pass
    elif not T.isalnum() and T.split()[1].lower() not in StandardUnits.UNITT:
        raise UnitError
    elif T.endswith("degC") or T.endswith("degc"):
        T = float(T.split()[0]) + 273
    elif T.endswith("K") or T.endswith("k"):
        T = float(T.split()[0])
    else:
        T = float(T)

    if p == None and V != None and n != None and T != None:
        p = (n * R * T) / V
        #basic unit: Pa
        return print(f"{'%.5g' % (p / 1000)} kPa or {'%.5g' % (p)} Pa")

    elif p != None and V == None and n != None and T != None:
        V = (n * R * T) / p
        #basic unit: m^3
        return print(f"{'%.5g' % (V)} m^3 or {'%.5g' % (V * 1000000)} cm^3")

    elif p != None and V != None and n == None and T != None:
        n = (p * V) / (R * T)
        #basic unit: mol
        return print(f"{'%.5g' % (n)} mol")

    elif p != None and V != None and n != None and T == None:
        T = (p * V) / (n * R)
        #basic unit: K
        return print(f"{T} K")

#pressure, volume, mole, and temperature ratio formula (p1V1/n1T1 = p2V2/n2T2, transformed by the general gas law)
def ggl2(p1 : str = None, V1 : str = None, n1 : str = None, T1 : str = None, p2 : str = None, V2 : str = None, n2 : str = None, T2 : str = None):
    if p1 == None: pass
    elif not p1.isalnum() and p1.split()[1].lower() not in StandardUnits.UNITp:
        raise UnitError
    elif p1.endswith("MPa") or p1.endswith("mpa"):
        p1 = float(p1.split()[0]) * 1000000
    elif p1.endswith("kPa") or p1.endswith("kpa"):
        p1 = float(p1.split()[0]) * 1000
    elif p1.endswith("Pa") or p1.endswith("pa") or p1.endswith("N m-2") or p1.endswith("n m-2"):
        p1 = float(p1.split()[0])
    else:
        p1 = float(p1)

    if V1 == None: pass
    elif not V1.isalnum() and V1.split()[1].lower() not in StandardUnits.UNITV:
        raise UnitError
    elif V1.endswith("cm^3"):
        V1 = float(V1.split()[0]) / 1000000
    elif V1.endswith("m^3"):
        V1 = float(V1.split()[0])
    else:
        V1 = float(V1)

    if n1 == None: pass
    elif not n1.isalnum() and n1.split()[1].lower() not in StandardUnits.UNITn:
        raise UnitError
    elif n1.endswith("mol"):
        n1 = float(n1.split()[0])
    else:
        n1 = float(n1)
    
    if T1 == None: pass
    elif not T1.isalnum() and T1.split()[1].lower() not in StandardUnits.UNITT:
        raise UnitError
    elif T1.endswith("degC") or T1.endswith("degc"):
        T1 = float(T1.split()[0]) + 273
    elif T1.endswith("K") or T1.endswith("k"):
        T1 = float(T1.split()[0])
    else:
        T1 = float(T1)

    if p2 == None: pass
    elif not p2.isalnum() and p2.split()[1].lower() not in StandardUnits.UNITp:
        raise UnitError
    elif p2.endswith("MPa") or p2.endswith("mpa"):
        p2 = float(p2.split()[0]) * 1000000
    elif p2.endswith("kPa") or p2.endswith("kpa"):
        p2 = float(p2.split()[0]) * 1000
    elif p2.endswith("Pa") or p2.endswith("pa") or p2.endswith("N m-2") or p2.endswith("n m-2"):
        p2 = float(p2.split()[0])
    else:
        p2 = float(p2)

    if V2 == None: pass
    elif not V2.isalnum() and V2.split()[1].lower() not in StandardUnits.UNITV:
        raise UnitError
    elif V2.endswith("cm^3"):
        V2 = float(V2.split()[0]) / 1000000
    elif V2.endswith("m^3"):
        V2 = float(V2.split()[0])
    else:
        V2 = float(V2)

    if n2 == None: pass
    elif not n2.isalnum() and n2.split()[1].lower() not in StandardUnits.UNITn:
        raise UnitError
    elif n2.endswith("mol"):
        n2 = float(n2.split()[0])
    else:
        n2 = float(n2)
    
    if T2 == None: pass
    elif not T2.isalnum() and T2.split()[1].lower() not in StandardUnits.UNITT:
        raise UnitError
    elif T2.endswith("degC") or T2.endswith("degc"):
        T2 = float(T2.split()[0]) + 273
    elif T2.endswith("K") or T2.endswith("k"):
        T2 = float(T2.split()[0])
    else:
        T2 = float(T2)

    if p1 == None and V1 != None and n1 != None and T1 != None and p2 != None and V2 != None and n2 != None and T2 != None:
        p1 = ((p2 * V2) / (n2 * T2)) * (n1 * T1) / V1
        #basic unit: Pa
        return print(f"{'%.5g' % (p1 / 1000)} kPa or {'%.5g' % (p1)} Pa")

    elif p1 != None and V1 == None and n1 != None and T1 != None and p2 != None and V2 != None and n2 != None and T2 != None:
        V1 = ((p2 * V2) / (n2 * T2)) * (n1 * T1) / p1
        #basic unit: cm^3 or m^3 (if the input value of V2 is m^3, take m^3 as common unit (use the same unit as input)
        return print(f"{'%.5g' % (V1)} m^3 or {'%.5g' % (V1 * 1000000)} cm^3")

    elif p1 != None and V1 != None and n1 == None and T1 != None and p2 != None and V2 != None and n2 != None and T2 != None:
        n1 = p1 * V1 * ((n2 * T2) / (p2 * V2)) / T1
        #basic unit: mol
        return print(f"{'%.5g' % (n1)} mol")

    elif p1 != None and V1 != None and n1 != None and T1 == None and p2 != None and V2 != None and n2 != None and T2 != None:
        T1 = p1 * V1 * ((n2 * T2) / (p2 * V2)) / n1
        #basic unit: K
        return print(f"{T1} K")

    elif p1 != None and V1 != None and n1 != None and T1 != None and p2 == None and V2 != None and n2 != None and T2 != None:
        p2 = ((p1 * V1) / (n1 * T1)) * (n2 * T2) / V2
        #basic unit: Pa
        return print(f"{'%.5g' % (p2 / 1000)} kPa or {'%.5g' % (p2)} Pa")

    elif p1 != None and V1 != None and n1 != None and T1 != None and p2 != None and V2 == None and n2 != None and T2 != None:
        V2 = ((p1 * V1) / (n1 * T1)) * (n2 * T2) / p2
        #basic unit: cm^3 or m^3 (if the input value of V2 is m^3, take m^3 as common unit (use the same unit as input)
        return print(f"{'%.5g' % (V1)} m^3 or {'%.5g' % (V1 * 1000000)} cm^3")

    elif p1 != None and V1 != None and n1 != None and T1 != None and p2 != None and V2 != None and n2 == None and T2 != None:
        n2 = p2 * V2 * ((n1 * T1) / (p1 * V1)) / T2
        #basic unit: mol
        return print(f"{'%.5g' % (n2)} mol")

    elif p1 != None and V1 != None and n1 != None and T1 != None and p2 != None and V2 != None and n2 != None and T2 == None:
        T2 = p2 * V2 * ((n2 * T2) / (p1 * V1)) / n2
        #basic unit: K
        return print(f"{T1} K")

#equations of motion1 (v = u + at)
def eom1(v : str = None, u : str = None, a : str = None, t : str = None):
    if v == None: pass
    elif not v.isalnum() and v.split()[1].lower() not in StandardUnits.UNITv:
        raise UnitError
    elif v.endswith("m s-1"):
        v = float(v.split()[0])
    else:
        v = float(v)

    if u == None: pass
    elif not u.isalnum() and u.split()[1].lower() not in StandardUnits.UNITu:
        raise UnitError
    elif u.endswith("m s-1"):
        u = float(u.split()[0])
    else:
        u = float(u)

    if a == None: pass
    elif not a.isalnum() and a.split()[1].lower() not in StandardUnits.UNITa:
        raise UnitError
    elif a.endswith("m s-2"):
        a = float(a.split()[0])
    else:
        a = float(a)

    if t == None: pass
    elif not t.isalnum() and t.split()[1].lower() not in StandardUnits.UNITt:
        raise UnitError
    elif t.endswith("h"):
        t = float(t.split()[0]) * 3600
    elif t.endswith("mins"):
        t = float(t.split()[0]) * 60
    elif t.endswith("s"):
        t = float(t.split()[0])
    else:
        t = float(t)

    if v == None and u != None and a != None and t != None:
        v = u + (a * t)
        #basic unit: m s-1
        return print(f"{v} m s-1")

    elif v != None and u == None and a != None and t != None:
        u = v - (a * t)
        #basic unit: m s-1
        return print(f"{v} m s-1")

    elif v != None and u != None and a == None and t != None:
        a = (v - u) / t
        #basic unit: m s-2
        return print(f"{a} m s-2")

    elif v != None and u != None and a != None and t == None:
        t = (v - u) / a
        #basic unit: seconds (?????????)
        return print(f"{'%.5g' % (t)} h or {'%.5g' % (t * 60)} mins or {'%.5g' % (t * 3600)} s")

#equations of motion2 (s = 1/2(u + v)t)
def eom2(s : str = None, u : str = None, v : str = None, t : str = None):
    if s == None: pass
    elif not s.isalnum() and s.split()[1].lower() not in StandardUnits.UNITs:
        raise UnitError
    elif s.endswith("cm"):
        s = float(s.split()[0]) / 100
    elif s.endswith("km"):
        s = float(s.split()[0]) / 100000
    elif s.endswith("m"):
        s = float(s.split()[0])
    else:
        s = float(s)

    if u == None: pass
    elif not u.isalnum() and u.split()[1].lower() not in StandardUnits.UNITu:
        raise UnitError
    elif u.endswith("m s-1"):
        u = float(u.split()[0])
    else:
        u = float(u)

    if v == None: pass
    elif not v.isalnum() and v.split()[1].lower() not in StandardUnits.UNITv:
        raise UnitError
    elif v.endswith("m s-1"):
        v = float(v.split()[0])
    else:
        v = float(v)

    if t == None: pass
    elif not t.isalnum() and t.split()[1].lower() not in StandardUnits.UNITt:
        raise UnitError
    elif t.endswith("h"):
        t = float(t.split()[0]) * 3600
    elif t.endswith("mins"):
        t = float(t.split()[0]) * 60
    elif t.endswith("s"):
        t = float(t.split()[0])
    else:
        t = float(t)

    if s == None and u != None and v != None and t != None:
        s = 1/2 * (u + v) * t
        #basic unit: m
        return print(f"{s / 1000} km or {s} m or {s * 100} cm")

    elif s != None and u == None and v != None and t != None:
        u = ((2 * s) / t) - v
        #basic unit: m s-1
        return print(f"{v} m s-1")

    elif s != None and u != None and v == None and t != None:
        v = ((2 * s) / t) - u
        #basic unit: m s-1
        return print(f"{v} m s-1")

    elif s != None and u != None and v != None and t == None:
        t = (2 * s) / (u + v)
        #basic unit: seconds (?????????)
        return print(f"{'%.5g' % (t)} h or {'%.5g' % (t * 60)} mins or {'%.5g' % (t * 3600)} s")

#equations of motion3 (s = ut + 1/2at^2)
def eom3(s : str = None, u : str = None, t : str = None, a : str = None):
    if s == None: pass
    elif not s.isalnum() and s.split()[1].lower() not in StandardUnits.UNITs:
        raise UnitError
    elif s.endswith("cm"):
        s = float(s.split()[0]) / 100
    elif s.endswith("km"):
        s = float(s.split()[0]) / 100000
    elif s.endswith("m"):
        s = float(s.split()[0])
    else:
        s = float(s)

    if u == None: pass
    elif not u.isalnum() and u.split()[1].lower() not in StandardUnits.UNITu:
        raise UnitError
    elif u.endswith("m s-1"):
        u = float(u.split()[0])
    else:
        u = float(u)

    if t == None: pass
    elif not t.isalnum() and t.split()[1].lower() not in StandardUnits.UNITt:
        raise UnitError
    elif t.endswith("h"):
        t = float(t.split()[0]) * 3600
    elif t.endswith("mins"):
        t = float(t.split()[0]) * 60
    elif t.endswith("s"):
        t = float(t.split()[0])
    else:
        t = float(t)

    if a == None: pass
    elif not a.isalnum() and a.split()[1].lower() not in StandardUnits.UNITa:
        raise UnitError
    elif a.endswith("m s-2"):
        a = float(a.split()[0])
    else:
        a = float(a)

    if s == None and u != None and t != None and a != None:
        s = u * t + (1/2 * a * t**2)
        #basic unit: m
        return print(f"{s / 1000} km or {s} m or {s * 100} cm")

    elif s != None and u == None and t != None and a != None:
        u = s - (1/2 * a * t)
        #basic unit: m s-1
        return print(f"{u} m s-1")

    elif s != None and u != None and t == None and a != None:
        t = u / (s - (1/2 * a))
        #basic unit: seconds (?????????)
        return print(f"{'%.5g' % (t)} h or {'%.5g' % (t * 60)} mins or {'%.5g' % (t * 3600)} s")

    elif s != None and u != None and t != None and a == None:
        a = 2 * (t / u + s)
        #basic unit: m s-2
        return print(f"{a} m s-2")

#equations of motion4 (v^2 = u^2 + 2as)
def eom4(v : str = None, u : str = None, a : str = None, s : str = None):
    if v == None: pass
    elif not v.isalnum() and v.split()[1].lower() not in StandardUnits.UNITv:
        raise UnitError
    elif v.endswith("m s-1"):
        v = float(v.split()[0])
    else:
        v = float(v)

    if u == None: pass
    elif not u.isalnum() and u.split()[1].lower() not in StandardUnits.UNITu:
        raise UnitError
    elif u.endswith("m s-1"):
        u = float(u.split()[0])
    else:
        u = float(u)

    if a == None: pass
    elif not a.isalnum() and a.split()[1].lower() not in StandardUnits.UNITa:
        raise UnitError
    elif a.endswith("m s-2"):
        a = float(a.split()[0])
    else:
        a = float(a)

    if s == None: pass
    elif not s.isalnum() and s.split()[1].lower() not in StandardUnits.UNITs:
        raise UnitError
    elif s.endswith("cm"):
        s = float(s.split()[0]) / 100
    elif s.endswith("km"):
        s = float(s.split()[0]) / 100000
    elif s.endswith("m"):
        s = float(s.split()[0])
    else:
        s = float(s)

    if v == None and u != None and a != None and s != None:
        v = sqrt(u**2 + (2 * a * s))
        #basic unit: m s-1
        return print(f"{v} m s-1")

    elif v != None and u == None and a != None and s != None:
        u = sqrt(v**2 - (2 * a * s))
        #basic unit: m s-1
        return print(f"{u} m s-1")

    elif v != None and u != None and a == None and s != None:
        a = (v**2 - u**2) / (2 * s)
        #basic unit: m s-2
        return print(f"{a} m s-2")

    elif v != None and u != None and a != None and s == None:
        s = (v**2 - u**2) / (2 * a)
        #basic unit: m
        return print(f"{s / 1000} km or {s} m or {s * 100} cm")

#initial speed, displacement ratio formula (u1^2/u2^2 = s1/s2, transformed by the fourth equation of motion)
def eom5(u1 : str = None, u2 : str = None, s1 : str = None, s2 : str = None):
    ...

#----------END OF PHYSICS FUNCTIONS----------#

#----------CODE (yes, code)----------#
while True:
    inp = input("Enter function: >> ")
    try:
        eval(inp)
    except AttributeError:
        print("Incorrect input type, please enter argument value as a string. (e.g. P = '200 W')")
    except UnitError:
        print("Unit in argument(s) incorrect or invalid, please use a valid unit and try again.")
    except NameError:
        print("Invalid constant name.")
    except SyntaxError:
        print("Invalid syntax. Please check your input if mistakes were made.")
#----------END OF CODE (yes, code)----------#