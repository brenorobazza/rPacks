from Regressions import Regressions

linReg = Regressions.Linear('test.csv', 'X', 'Y')
polReg = Regressions.Polinomial('test.csv', 'X', 'Y', order=2)

print(linReg.r_squared)
print(polReg.r_squared)
print(polReg.predict(10))
print(linReg.predict(10))

linReg.plot('linear')
polReg.plot('polinomial')

