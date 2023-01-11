

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
        return print(f"{'%.5g' % (P / 1000000)} MW or {'%.5g' % (P / 1000)} kW or {'{:.4e}'.format(P)} W")
    
    elif P != None and Q == None and t != None:
        Q = P * t
        #base unit: joule
        return print(f"{'%.5g' % (Q / 1000000)} MJ or {'%.5g' % (Q / 1000)} kJ or {'{:.4e}'.format(Q)} J")
        
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
        return print(f"{'%.5g' % (Q / 1000000)} MJ or {'%.5g' % (Q / 1000)} kJ or {'{:.4e}'.format(Q)} J")
    
    elif Q != None and C == None and dT != None:
        C = Q / dT
        #base unit: joule degree celsius^-1
        return print(f"{'%.5g' % (C / 1000000)} MJ/°C or {'%.5g' % (C / 1000)} kJ/°C or {'{:.4e}'.format(C)} J/°C")
        
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
        return print(f"{'%.5g' % (Q / 1000000)} MJ or {'%.5g' % (Q / 1000)} kJ or {'{:.4e}'.format(Q)} J")
    
    elif Q != None and m == None and c != None and dT != None:
        m = Q / c / dT
        #base unit: kg
        return print(f"{'%.5g' % (m)} kg or {'%.5g' % (m / 1000)} g")
        
    elif Q != None and m != None and c == None and dT != None:
        c = Q / m / dT
        #base unit: joule kg^-1 degree celsius^-1
        return print(f"{'%.5g' % (c / 1000000)} MJ kg-1 °C-1 or {'%.5g' % (c /1000)} kJ kg-1 °C-1 or {'{:.4e}'.format(c)} J kg-1 °C-1")
    
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
        
    return print(f"{P * t}")

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
        return print(f"{'%.5g' % (l / 1000000)} MJ kg-1 or {'%.5g' % (l /1000)} kJ kg-1 or {'{:.4e}'.format(l)} J kg-1")
    
    elif l != None and Q == None and m != None:
        Q = l * m
        #base unit: joule
        return print(f"{'%.5g' % (Q / 1000000)} MJ or {'%.5g' % (Q / 1000)} kJ or {'{:.4e}'.format(Q)} J")

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
        return print(f"{'%.5g' % (E / 1000000)} MJ or {'%.5g' % (E / 1000)} kJ or {'{:.4e}'.format(E)} J")

    elif E != None and m == None and l != None and c != None and dT != None:
        m = E / (l + (c * dT))
        #base unit: kg
        return print(f"{'%.5g' % (m)} kg or {'%.5g' % (m / 1000)} g")
    
    elif E != None and m != None and l == None and c != None and dT != None:
        l = (E / m) - (c * dT)
        #base unit: joule kg-1
        return print(f"{'%.5g' % (l / 1000000)} MJ kg-1 or {'%.5g' % (l /1000)} kJ kg-1 or {'{:.4e}'.format(l)} J kg-1")
    
    elif E != None and m != None and l != None and c == None and dT != None:
        c = ((E / m) - l) / dT
        #base unit: joule kg^-1 degree celsius^-1
        return print(f"{'%.5g' % (c / 1000000)} MJ kg-1 °C-1 or {'%.5g' % (c /1000)} kJ kg-1 °C-1 or {'{:.4e}'.format(c)} J kg-1 °C-1")
    
    elif E != None and m != None and l != None and c != None and dT == None:
        dT = ((E / m) - l) / c
        #base unit: degree celsius
        return print(f"{'%.5g' % (dT)} °C")

#

while True:
    inp = input(">> ")
    eval(inp)

        

