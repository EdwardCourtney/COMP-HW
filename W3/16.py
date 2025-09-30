a = float(input())
sw = False
if (a<0):
    sw = True
    a *= -1
rdown = int(a)
rup = int(a)
rnear = int(a)
if (a - rdown != 0):
    rup = rdown + 1
if (a - rdown < 0.5):
    rnear = rdown
else:
    rnear = rup

if (sw):
    rup *= -1
    rdown *= -1
    rnear *= -1
    rup = rup ^ rdown
    rdown = rup ^ rdown
    rup = rup ^ rdown
print(f"{rup} {rdown} {rnear}")
