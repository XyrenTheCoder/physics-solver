#----------EXCEPTIONS----------#
class UnitError(Exception): "Incorrect unit in argument(s)."
#----------END OF EXCEPTIONS----------#

#----------STANDARD UNITS----------#
'''
all units are in descending order, from the largest to the smallest.
note: there can be more than 1 basic unit for some of the items e.g. Q and E
'''
class StandardUnits():
    UNITP = ['mw', 'kw', 'w']
    UNITt = ['h', 'mins', 's']
    UNITQ = ['mj', 'mw h', 'kj', 'kw h', 'j', 'w h']
    UNITC = ['mj degc-1', 'kj degc-1', 'j degc-1']
    UNITdT = ['degc']
    UNITm = ['kg', 'g']
    UNITc = ['mj kg-1 degc-1', 'kj kg-1 degc-1', 'j kg-1 degc-1']
    UNITl = ['mj kg-1', 'kj kg-1', 'j kg-1']
    UNITE = ['mj', 'mw h', 'kj', 'kw h', 'j', 'w h']
    UNITp = ['mpa', 'kpa', 'pa']
    UNITF = ['n']
    UNITA = ['m^2', 'cm^2']
    UNITV = ['m^3', 'cm^3']
    UNITT = ['k', 'degc']
    UNITn = ['mol']
    UNITv = ['m s-1']
    UNITu = ['m s-1']
    UNITa = ['m s-2']
    UNITs = ['km', 'm', 'cm']
#----------END OF STANDARD UNITS----------#
