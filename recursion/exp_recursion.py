
def  pow(dblbase, ipower):
    if ipower < 0:
        ipower = -ipower
        dblbase = 1/dblbase
    
    if ipower == 0:
        return 1
    
    dblbase *= pow(dblbase, ipower - 1)
    return dblbase

