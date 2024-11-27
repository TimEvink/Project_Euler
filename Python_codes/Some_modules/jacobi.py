#jacobi symbol module

def jac(a,b): # Computes the value of the jacobi symbol (a/b). Can be called without error for non-zero even b, even though for such b the symbol is not defined.
    anew = a % b
    if anew == 0:
        if b == 1: #if indeed b == 1 then also anew == 0 so the function will never fail to notice that b == 1
            return 1
        return 0
    k = 0
    while anew % 2 == 0: #replaces anew with its prime-to-2 part and keeps track of 2-valuation
        k += 1
        anew //= 2
    if (k % 2 == 1) and (b % 8 in [3,5]): #accounts for the value of jac(2^k,b)
        twopart = -1
    else:
        twopart = 1
    if (anew % 4 == 3) and (b % 4 == 3): #accounts for sign change upon applying reciprocity for recursive step
        twopart *= -1
    return twopart * jac(b,anew)
