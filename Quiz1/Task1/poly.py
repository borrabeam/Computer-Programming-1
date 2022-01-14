from OO_complex import *

class Polynomial:

    def __init__(self, coefficients):
        self.coefficients = list(coefficients)


    def add(self, other):

        coefficients1 = self.coefficients[::-1]
        coefficients2 = other.coefficients[::-1]
        return Polynomial(coefficients1*coefficients2)
        
    def val(self, v):
        pass
    
    def mul(self, other):
        new_coeff = self.coefficients * other.coefficients

        return Polynomial(new_coeff)
    
    def coeff(self, i):
        pass
    
    def roots(self):
        pass

    def __call__(self, v):
        pass

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)

    def __str__(self):
        res = ""
        degree = len(self.coefficients) - 1
        res += str(self.coefficients[0]) + "Z**" + str(degree)
        for i in range(1, len(self.coefficients)-1):
            coeff = self.coefficients[i]
            if coeff < 0:
                res += " - " +  str(-coeff) + "Z**" + str(degree - i)
            else:
                res += " + " +  str(coeff) + "Z**" + str(degree - i)
                
        if self.coefficients[-1] < 0:
            res += " - " + str(-self.coefficients[-1])
        else:
            res += " + " + str(self.coefficients[-1])

        return res
    