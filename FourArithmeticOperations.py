class _deArithmetic:
    def Mathadd(self, addend1, addend2):
        result = addend1 + addend2
        return result
    def Mathsubtraction(self, minuend, subtrahend):
        result = minuend - subtrahend
        return result
    def Mathmultiply(self, multiplier1, multiplier2):
        result = multiplier1 + multiplier2
        return result
    def Mathdivision(self, dividend, divisor):
        result = dividend / divisor
        return result

if __name__ == '__main__':
    a = 9
    b = 3
    cal = _deArithmetic()
    c1 = cal.Mathadd(a, b)
    c2 = cal.Mathsubtraction(a, b)
    c3 = cal.Mathmultiply(a, b)
    c4 = cal.Mathdivision(a, b)
