

#-----constants-----#
l_f = 334000 #J kg-1 (specific latent heat of fusion)
l_v = 2260000 #J kg-1 (specific latent heat of vaporization)
c_w = 4200 #J kg-1 degC-1 (specific heat capacity of water)
abszero = 0 #K (absolute zero)
N_A = 6.02 * (10 ** 23) #(avogadro's const)
R = 8.31 #J mol-1 K-1 (universal gas const)
g = 9.80665 #m s-2 (earth's gravital acceleration)
#-----end of constants-----#

#energy transfer
def et(P : str = None, Q : str = None, t : str = None):
    if P == None: pass
    elif P.endswith("MW") or P.endswith("mw"):
        P = float(P.split()[0]) * 1000000
    elif P.endswith("kW") or P.endswith("kw"):
        P = float(P.split()[0]) * 1000
    elif P.endswith("W") or P.endswith("w"):
        P = float(P.split()[0])
    else:
        P = float(P)
    
    if Q == None: pass
    elif Q.endswith("MJ") or Q.endswith("mj") or Q.endswith("MW h") or Q.endswith("mw h"):
        Q = float(Q.split()[0]) * 1000000
    elif Q.endswith("kJ") or Q.endswith("kj") or Q.endswith("kW h") or Q.endswith("kw h"):
        Q = float(Q.split()[0]) * 1000
    elif Q.endswith("J") or Q.endswith("j") or Q.endswith("W h") or Q.endswith("w h"):
        Q = float(Q.split()[0])
    else:
        Q = float(Q)
    
    if t == None: pass
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
        #base unit: watt
        return print(f"{'%.5g' % (P / 1000000)} MW or {'%.5g' % (P / 1000)} kW or {'%.5g' % (P)} W")
    
    elif P != None and Q == None and t != None:
        Q = P * t
        #base unit: joule
        return print(f"{'%.5g' % (Q / 1000000)} MJ or {'%.5g' % (Q / 1000)} kJ or {'%.5g' % (Q)} J")
        
    elif P != None and Q != None and t == None:
        t = Q / P
        #base unit: hours
        return print(f"{'%.5g' % (t)} h or {'%.5g' % (t * 60)} mins or {'%.5g' % (t * 3600)} s")

#heat capacity
def hc(Q : str = None, C : str = None, dT : str = None):
    if Q == None: pass
    elif Q.endswith("MJ") or Q.endswith("mj") or Q.endswith("MW h") or Q.endswith("mw h"):
        Q = float(Q.split()[0]) * 1000000
    elif Q.endswith("kJ") or Q.endswith("kj") or Q.endswith("kW h") or Q.endswith("kw h"):
        Q = float(Q.split()[0]) * 1000
    elif Q.endswith("J") or Q.endswith("j") or Q.endswith("W h") or Q.endswith("w h"):
        Q = float(Q.split()[0])
    else:
        Q = float(Q)

    if C == None: pass
    elif C.endswith("MJ degC-1") or C.endswith("mj degc-1"):
        C = float(C.split()[0]) * 1000000
    elif C.endswith("kJ degC-1") or C.endswith("kj degc-1"):
        C = float(C.split()[0]) * 1000
    elif C.endswith("J degC-1") or C.endswith("j degc-1"):
        C = float(C.split()[0])
    else:
        C = float(C)

    if dT == None: pass
    elif dT.endswith("degC") or dT.endswith("degc"):
        dT = float(dT.split()[0])
    else:
        dT = float(dT)

    if Q == None and C != None and dT != None:
        Q = C * dT
        #base unit: joule
        return print(f"{'%.5g' % (Q / 1000000)} MJ or {'%.5g' % (Q / 1000)} kJ or {'%.5g' % (Q)} J")
    
    elif Q != None and C == None and dT != None:
        C = Q / dT
        #base unit: joule degree celsius^-1
        return print(f"{'%.5g' % (C / 1000000)} MJ/°C or {'%.5g' % (C / 1000)} kJ/°C or {'%.5g' % (C)} J/°C")
        
    elif Q != None and C != None and dT == None:
        dT = Q / C
        #base unit: degree celsius
        return print(f"{'%.5g' % (dT)} °C")

#specific heat capacity
def shc(Q : str = None, m : str = None, c : str = None, dT : str = None):
    if Q == None: pass
    elif Q.endswith("MJ") or Q.endswith("mj") or Q.endswith("MW h") or Q.endswith("mw h"):
        Q = float(Q.split()[0]) * 1000000
    elif Q.endswith("kJ") or Q.endswith("kj") or Q.endswith("kW h") or Q.endswith("kw h"):
        Q = float(Q.split()[0]) * 1000
    elif Q.endswith("J") or Q.endswith("j") or Q.endswith("W h") or Q.endswith("w h"):
        Q = float(Q.split()[0])
    else:
        Q = float(Q)

    if m == None: pass
    elif m.endswith("kg"):
        m = float(m.split()[0])
    elif m.endswith("g"):
        m = float(m.split()[0]) / 1000
    else:
        m = float(m)

    if c == None: pass
    elif c.endswith("MJ kg-1 degC-1") or c.endswith("mj kg-1 degc-1"):
        c = float(c.split()[0]) * 1000000
    elif c.endswith("kJ kg-1 degC-1") or c.endswith("kj kg-1 degc-1"):
        c = float(c.split()[0]) * 1000
    elif c.endswith("J kg-1 degC-1") or c.endswith("j kg-1 degc-1"):
        c = float(c.split()[0])
    else:
        c = float(c)

    if dT == None: pass
    elif dT.endswith("degC") or dT.endswith("degc"):
        dT = float(dT.split()[0])
    else:
        dT = float(dT)

    if Q == None and m != None and c != None and dT != None:
        print(m, c, dT)
        Q = m * c * dT
        #base unit: joule
        return print(f"{'%.5g' % (Q / 1000000)} MJ or {'%.5g' % (Q / 1000)} kJ or {'%.5g' % (Q)} J")
    
    elif Q != None and m == None and c != None and dT != None:
        m = Q / c / dT
        #base unit: kg
        return print(f"{'%.5g' % (m)} kg or {'%.5g' % (m / 1000)} g")
        
    elif Q != None and m != None and c == None and dT != None:
        c = Q / m / dT
        #base unit: joule kg^-1 degree celsius^-1
        return print(f"{'%.5g' % (c / 1000000)} MJ kg-1 °C-1 or {'%.5g' % (c /1000)} kJ kg-1 °C-1 or {'%.5g' % (c)} J kg-1 °C-1")
    
    elif Q != None and m != None and c != None and dT == None:
        dT = Q / m / c
        #base unit: degree celsius
        return print(f"{'%.5g' % (dT)} °C")

#power to energy
def PtoQ(P : str, t : str):
    if P == None: pass
    elif P.endswith("MW") or P.endswith("mw"):
        P = float(P.split()[0]) * 1000000
    elif P.endswith("kW") or P.endswith("kw"):
        P = float(P.split()[0]) * 1000
    elif P.endswith("W") or P.endswith("w"):
        P = float(P.split()[0])
    else:
        P = float(P)

    if t == None: pass
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
    elif Q.endswith("MJ") or Q.endswith("mj") or Q.endswith("MW h") or Q.endswith("mw h"):
        Q = float(Q.split()[0]) * 1000000
    elif Q.endswith("kJ") or Q.endswith("kj") or Q.endswith("kW h") or Q.endswith("kw h"):
        Q = float(Q.split()[0]) * 1000
    elif Q.endswith("J") or Q.endswith("j") or Q.endswith("W h") or Q.endswith("w h"):
        Q = float(Q.split()[0])
    else:
        Q = float(Q)

    if t == None: pass
    elif t.endswith("h"):
        t = float(t.split()[0]) * 3600
    elif t.endswith("mins"):
        t = float(t.split()[0]) * 60
    elif t.endswith("s"):
        t = float(t.split()[0])
    else:
        t = float(t)
        
    return print(f"{'%.5g' % (Q / t / 1000000)} MJ or {'%.5g' % (Q / t / 1000)} kJ or {'%.5g' % (Q / t)} J")

#specific latent heat
def slh(l : str = None, Q : str = None, m : str = None):
    if l == None: pass
    elif l.endswith("MJ kg-1") or l.endswith("mj kg-1"):
        l = float(l.split()[0]) * 1000000
    elif l.endswith("kJ kg-1") or l.endswith("kj kg-1"):
        l = float(l.split()[0]) * 1000
    elif l.endswith("J kg-1") or l.endswith("j kg-1"):
        l = float(l.split()[0])
    else:
        l = float(l)

    if Q == None: pass
    elif Q.endswith("MJ") or Q.endswith("mj") or Q.endswith("MW h") or Q.endswith("mw h"):
        Q = float(Q.split()[0]) * 1000000
    elif Q.endswith("kJ") or Q.endswith("kj") or Q.endswith("kW h") or Q.endswith("kw h"):
        Q = float(Q.split()[0]) * 1000
    elif Q.endswith("J") or Q.endswith("j") or Q.endswith("W h") or Q.endswith("w h"):
        Q = float(Q.split()[0])
    else:
        Q = float(Q)

    if m == None: pass
    elif m.endswith("kg"):
        m = float(m.split()[0])
    elif m.endswith("g"):
        m = float(m.split()[0]) / 1000
    else:
        m = float(m)

    if l == None and Q != None and m != None:
        l = Q / m
        #base unit: J kg-1
        return print(f"{'%.5g' % (l / 1000000)} MJ kg-1 or {'%.5g' % (l /1000)} kJ kg-1 or {'%.5g' % (l)} J kg-1")
    
    elif l != None and Q == None and m != None:
        Q = l * m
        #base unit: joule
        return print(f"{'%.5g' % (Q / 1000000)} MJ or {'%.5g' % (Q / 1000)} kJ or {'%.5g' % (Q)} J")

    elif l != None and Q != None and m == None:
        m = Q / l
        #base unit: kg
        return print(f"{'%.5g' % (m)} kg or {'%.5g' % (m / 1000)} g")

#total energy
def te(E : str = None, m : str = None, l : str = None, c : str = None, dT : str = None):
    if E == None: pass
    elif E.endswith("MJ") or E.endswith("mj") or E.endswith("MW h") or E.endswith("mw h"):
        E = float(E.split()[0]) * 1000000
    elif E.endswith("kJ") or E.endswith("kj") or E.endswith("kW h") or E.endswith("kw h"):
        E = float(E.split()[0]) * 1000
    elif E.endswith("J") or E.endswith("j") or E.endswith("W h") or E.endswith("w h"):
        E = float(E.split()[0])
    else:
        E = float(E)

    if m == None: pass
    elif m.endswith("kg"):
        m = float(m.split()[0])
    elif m.endswith("g"):
        m = float(m.split()[0]) / 1000
    else:
        m = float(m)

    if l == None: pass
    elif l.endswith("MJ kg-1") or l.endswith("mj kg-1"):
        l = float(l.split()[0]) * 1000000
    elif l.endswith("kJ kg-1") or l.endswith("kj kg-1"):
        l = float(l.split()[0]) * 1000
    elif l.endswith("J kg-1") or l.endswith("j kg-1"):
        l = float(l.split()[0])
    else:
        l = float(l)

    if c == None: pass
    elif c.endswith("MJ kg-1 degC-1") or c.endswith("mj kg-1 degc-1"):
        c = float(c.split()[0]) * 1000000
    elif c.endswith("kJ kg-1 degC-1") or c.endswith("kj kg-1 degc-1"):
        c = float(c.split()[0]) * 1000
    elif c.endswith("J kg-1 degC-1") or c.endswith("j kg-1 degc-1"):
        c = float(c.split()[0])
    else:
        c = float(c)

    if dT == None: pass
    elif dT.endswith("degC") or dT.endswith("degc"):
        dT = float(dT.split()[0])
    else:
        dT = float(dT)

    if E == None and m != None and l != None and c != None and dT != None:
        E = (m * l) + (m * c * dT)
        #base unit: joule
        return print(f"{'%.5g' % (E / 1000000)} MJ or {'%.5g' % (E / 1000)} kJ or {'%.5g' % (E)} J")

    elif E != None and m == None and l != None and c != None and dT != None:
        m = E / (l + (c * dT))
        #base unit: kg
        return print(f"{'%.5g' % (m)} kg or {'%.5g' % (m / 1000)} g")
    
    elif E != None and m != None and l == None and c != None and dT != None:
        l = (E / m) - (c * dT)
        #base unit: joule kg-1
        return print(f"{'%.5g' % (l / 1000000)} MJ kg-1 or {'%.5g' % (l /1000)} kJ kg-1 or {'%.5g' % (l)} J kg-1")
    
    elif E != None and m != None and l != None and c == None and dT != None:
        c = ((E / m) - l) / dT
        #base unit: joule kg^-1 degree celsius^-1
        return print(f"{'%.5g' % (c / 1000000)} MJ kg-1 °C-1 or {'%.5g' % (c /1000)} kJ kg-1 °C-1 or {'%.5g' % (c)} J kg-1 °C-1")
    
    elif E != None and m != None and l != None and c != None and dT == None:
        dT = ((E / m) - l) / c
        #base unit: degree celsius
        return print(f"{'%.5g' % (dT)} °C")

#pressure force
def pf(p : str = None, F : str = None, A : str = None):
    if p == None: pass
    elif p.endswith("MPa") or p.endswith("mpa"):
        p = float(p.split()[0]) * 1000000
    elif p.endswith("kPa") or p.endswith("kpa"):
        p = float(p.split()[0]) * 1000
    elif p.endswith("Pa") or p.endswith("pa") or p.endswith("N m-2") or p.endswith("n m-2"):
        p = float(p.split()[0])
    else:
        p = float(p)

    if F == None: pass
    elif F.endswith("N") or F.endswith("n"):
        F = float(F.split()[0])
    else:
        F = float(F)

    if A == None: pass
    elif A.endswith("cm^2"):
        A = float(A.split()[0]) * 10000
    elif A.endswith("m^2"):
        A = float(A.split()[0])
    else:
        A = float(A)

    if p == None and F != None and A != None:
        p = F / A
        #base unit: Pa
        return print(f"{'%.5g' % (p / 1000)} kPa or {'%.5g' % (p)} Pa")

    elif p != None and F == None and A != None:
        F = p * A
        #base unit: N
        return print(f"{'%.5g' % (F)} N")

    elif p != None and F != None and A == None:
        A = F / p
        #base unit: m^2
        return print(f"{'%.5g' % (A)} m^2 or {'%.5g' % (A * 10000)} cm^2")

#boyle's law
def bl(p1 : str = None, V1 : str = None, p2 : str = None, V2 : str = None):
    if p1 == None: pass
    elif p1.endswith("MPa") or p1.endswith("mpa"):
        p1 = float(p1.split()[0]) * 1000000
    elif p1.endswith("kPa") or p1.endswith("kpa"):
        p1 = float(p1.split()[0]) * 1000
    elif p1.endswith("Pa") or p1.endswith("pa") or p1.endswith("N m-2") or p1.endswith("n m-2"):
        p1 = float(p1.split()[0])
    else:
        p1 = float(p1)

    if V1 == None: pass
    elif V1.endswith("cm^3"):
        V1 = float(V1.split()[0]) / 1000000
    elif V1.endswith("m^3"):
        V1 = float(V1.split()[0])
    else:
        V1 = float(V1)

    if p2 == None: pass
    elif p2.endswith("MPa") or p2.endswith("mpa"):
        p2 = float(p2.split()[0]) * 1000000
    elif p2.endswith("kPa") or p2.endswith("kpa"):
        p2 = float(p2.split()[0]) * 1000
    elif p2.endswith("Pa") or p2.endswith("pa") or p2.endswith("N m-2") or p2.endswith("n m-2"):
        p2 = float(p2.split()[0])
    else:
        p2 = float(p2)

    if V2 == None: pass
    elif V2.endswith("cm^3"):
        V2 = float(V2.split()[0]) / 1000000
    elif V2.endswith("m^3"):
        V2 = float(V2.split()[0])
    else:
        V2 = float(V2)

    if p1 == None and V1 != None and p2 != None and V2 != None:
        p1 = (p2 * V2) / V1
        #base unit: Pa
        return print(f"{'%.5g' % (p1 / 1000)} kPa or {'%.5g' % (p1)} Pa")

    elif p1 != None and V1 == None and p2 != None and V2 != None:
        V1 = (p2 * V2) / p1
        #base unit: cm^3 or m^3 (if the input value of V2 is m^3, take m^3 as common unit (use the same unit as input)
        return print(f"{'%.5g' % (V1)} m^3 or {'%.5g' % (V1 * 1000000)} cm^3")

    elif p1 != None and V1 != None and p2 == None and V2 != None:
        p2 = (p1 * V1) / V2
        #base unit: Pa
        return print(f"{'%.5g' % (p2 / 1000)} kPa or {'%.5g' % (p2)} Pa")
    
    elif p1 != None and V1 != None and p2 != None and V2 == None:
        V2 = (p1 * V1) / p2
        #base unit: cm^3 or m^3 (if the input value of V1 is m^3, take m^3 as common unit (use the same unit as input))
        return print(f"{'%.5g' % (V2)} m^3 or {'%.5g' % (V2 * 1000000)} cm^3")

#celsius to kelvin
def CtoK(degc : float):
    degk = degc + 273
    return print(f"{degk} K")

#kelvin to celsius
def KtoC(degk : float):
    degc = degk - 273
    return print(f"{degc} °C")

#pressure law
def pl(p1 : str = None, T1 : str = None, p2 : str = None, T2 : str = None):
    if p1 == None: pass
    elif p1.endswith("MPa") or p1.endswith("mpa"):
        p1 = float(p1.split()[0]) * 1000000
    elif p1.endswith("kPa") or p1.endswith("kpa"):
        p1 = float(p1.split()[0]) * 1000
    elif p1.endswith("Pa") or p1.endswith("pa") or p1.endswith("N m-2") or p1.endswith("n m-2"):
        p1 = float(p1.split()[0])
    else:
        p1 = float(p1)

    if T1 == None: pass
    elif T1.endswith("degC") or T1.endswith("degc"):
        T1 = float(T1.split()[0]) + 273
    elif T1.endswith("K") or T1.endswith("k"):
        T1 = float(T1.split()[0])
    else:
        T1 = float(T1)

    if p2 == None: pass
    elif p2.endswith("MPa") or p2.endswith("mpa"):
        p2 = float(p2.split()[0]) * 1000000
    elif p2.endswith("kPa") or p2.endswith("kpa"):
        p2 = float(p2.split()[0]) * 1000
    elif p2.endswith("Pa") or p2.endswith("pa") or p2.endswith("N m-2") or p2.endswith("n m-2"):
        p2 = float(p2.split()[0])
    else:
        p2 = float(p2)

    if T2 == None: pass
    elif T2.endswith("degC") or T2.endswith("degc"):
        T2 = float(T2.split()[0]) + 273
    elif T2.endswith("K") or T2.endswith("k"):
        T2 = float(T2.split()[0])
    else:
        T2 = float(T2)

    if p1 == None and T1 != None and p2 != None and T2 != None:
        p1 = (p2 / T2) * T1
        #base unit: Pa
        return print(f"{'%.5g' % (p1 / 1000)} kPa or {'%.5g' % (p1)} Pa")

    elif p1 != None and T1 == None and p2 != None and T2 != None:
        T1 = (T2 / p2) * p1
        #base unit: K
        return print(f"{T1} K")

    elif p1 != None and T1 != None and p2 == None and T2 != None:
        p2 = (p1 / T1) * T2
        #base unit: Pa
        return print(f"{'%.5g' % (p2 / 1000)} kPa or {'%.5g' % (p2)} Pa")

    elif p1 != None and T1 != None and p2 != None and T2 == None:
        T2 = (T1 / p1) * p2
        #base unit: K
        return print(f"{T2} K")

#charles' law
def cl(V1 : str = None, T1 : str = None, V2 : str = None, T2 : str = None):
    if V1 == None: pass
    elif V1.endswith("cm^3"):
        V1 = float(V1.split()[0]) / 1000000
    elif V1.endswith("m^3"):
        V1 = float(V1.split()[0])
    else:
        V1 = float(V1)

    if T1 == None: pass
    elif T1.endswith("degC") or T1.endswith("degc"):
        T1 = float(T1.split()[0]) + 273
    elif T1.endswith("K") or T1.endswith("k"):
        T1 = float(T1.split()[0])
    else:
        T1 = float(T1)

    if V2 == None: pass
    elif V2.endswith("cm^3"):
        V2 = float(V2.split()[0]) / 1000000
    elif V2.endswith("m^3"):
        V2 = float(V2.split()[0])
    else:
        V2 = float(V2)

    if T2 == None: pass
    elif T2.endswith("degC") or T2.endswith("degc"):
        T2 = float(T2.split()[0]) + 273
    elif T2.endswith("K") or T2.endswith("k"):
        T2 = float(T2.split()[0])
    else:
        T2 = float(T2)

    if V1 == None and T1 != None and V2 != None and T2 != None:
        V1 = (V2 / T2) * T1
        #base unit: m^3
        return print(f"{'%.5g' % (V1)} m^3 or {'%.5g' % (V1 * 1000000)} cm^3")

    elif V1 != None and T1 == None and V2 != None and T2 != None:
        T1 = (T2 / V2) * V1
        #base unit: K
        return print(f"{T1} K")

    elif V1 != None and T1 != None and V2 == None and T2 != None:
        V2 = (V1 / T1) * T2
        #base unit: m^3
        return print(f"{'%.5g' % (V2)} m^3 or {'%.5g' % (V2 * 1000000)} cm^3")

    elif V1 != None and T1 != None and V2 != None and T2 == None:
        T2 = (T1 / V1) * V2
        #base unit: K
        return print(f"{T2} K")

#general gas law
def ggl(p : str = None, V : str = None, n : str = None, T : str = None):
    if p == None: pass
    elif p.endswith("MPa") or p.endswith("mpa"):
        p = float(p.split()[0]) * 1000000
    elif p.endswith("kPa") or p.endswith("kpa"):
        p = float(p.split()[0]) * 1000
    elif p.endswith("Pa") or p.endswith("pa") or p.endswith("N m-2") or p.endswith("n m-2"):
        p = float(p.split()[0])
    else:
        p = float(p)

    if V == None: pass
    elif V.endswith("cm^3"):
        V = float(V.split()[0]) / 1000000
    elif V.endswith("m^3"):
        V = float(V.split()[0])
    else:
        V = float(V)

    if n == None: pass
    elif n.endswith("mol"):
        n = float(n.split()[0])
    else:
        n = float(n)

    if T == None: pass
    elif T.endswith("degC") or T.endswith("degc"):
        T = float(T.split()[0]) + 273
    elif T.endswith("K") or T.endswith("k"):
        T = float(T.split()[0])
    else:
        T = float(T)

    if p == None and V != None and n != None and T != None:
        p = (n * R * T) / V
        #base unit: Pa
        return print(f"{'%.5g' % (p / 1000)} kPa or {'%.5g' % (p)} Pa")

    elif p != None and V == None and n != None and T != None:
        V = (n * R * T) / p
        #base unit: m^3
        return print(f"{'%.5g' % (V)} m^3 or {'%.5g' % (V * 1000000)} cm^3")

    elif p != None and V != None and n == None and T != None:
        n = (p * V) / (R * T)
        #base unit: mol
        return print(f"{'%.5g' % (n)} mol")

    elif p != None and V != None and n != None and T == None:
        T = (p * V) / (n * R)
        #base unit: K
        return print(f"{T} K")

#pressure, volume, mole, and temperature ratio formula (transformed by the general gas law)
def ggl2(p1 : str = None, V1 : str = None, n1 : str = None, T1 : str = None, p2 : str = None, V2 : str = None, n2 : str = None, T2 : str = None):
    if p1 == None: pass
    elif p1.endswith("MPa") or p1.endswith("mpa"):
        p1 = float(p1.split()[0]) * 1000000
    elif p1.endswith("kPa") or p1.endswith("kpa"):
        p1 = float(p1.split()[0]) * 1000
    elif p1.endswith("Pa") or p1.endswith("pa") or p1.endswith("N m-2") or p1.endswith("n m-2"):
        p1 = float(p1.split()[0])
    else:
        p1 = float(p1)

    if V1 == None: pass
    elif V1.endswith("cm^3"):
        V1 = float(V1.split()[0]) / 1000000
    elif V1.endswith("m^3"):
        V1 = float(V1.split()[0])
    else:
        V1 = float(V1)

    if n1 == None: pass
    elif n1.endswith("mol"):
        n1 = float(n1.split()[0])
    else:
        n1 = float(n1)
    
    if T1 == None: pass
    elif T1.endswith("degC") or T1.endswith("degc"):
        T1 = float(T1.split()[0]) + 273
    elif T1.endswith("K") or T1.endswith("k"):
        T1 = float(T1.split()[0])
    else:
        T1 = float(T1)

    if p2 == None: pass
    elif p2.endswith("MPa") or p2.endswith("mpa"):
        p2 = float(p2.split()[0]) * 1000000
    elif p2.endswith("kPa") or p2.endswith("kpa"):
        p2 = float(p2.split()[0]) * 1000
    elif p2.endswith("Pa") or p2.endswith("pa") or p2.endswith("N m-2") or p2.endswith("n m-2"):
        p2 = float(p2.split()[0])
    else:
        p2 = float(p2)

    if V2 == None: pass
    elif V2.endswith("cm^3"):
        V2 = float(V2.split()[0]) / 1000000
    elif V2.endswith("m^3"):
        V2 = float(V2.split()[0])
    else:
        V2 = float(V2)

    if n2 == None: pass
    elif n2.endswith("mol"):
        n2 = float(n2.split()[0])
    else:
        n2 = float(n2)
    
    if T2 == None: pass
    elif T2.endswith("degC") or T2.endswith("degc"):
        T2 = float(T2.split()[0]) + 273
    elif T2.endswith("K") or T2.endswith("k"):
        T2 = float(T2.split()[0])
    else:
        T2 = float(T2)

    if p1 == None and V1 != None and n1 != None and T1 != None and p2 != None and V2 != None and n2 != None and T2 != None:
        p1 = ((p2 * V2) / (n2 * T2)) * (n1 * T1) / V1
        #base unit: Pa
        return print(f"{'%.5g' % (p / 1000)} kPa or {'%.5g' % (p)} Pa")

while True:
    inp = input(">> ")
    eval(inp)

        

