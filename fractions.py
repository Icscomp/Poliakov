def reduced_fr(num, den: int) -> int:
    for i in range(num, 1, -1):
        if num % i == den % i == 0:
            num //= i
            den //= i
    return (num, den)

def exist_per (den: int) -> bool:
    per = True
    while den % 5 == 0:
        den //= 5
    while den % 2 == 0:
        den //= 2
    if den == 1:
        per = False
    return (per)


def pre_per (den: int) -> int:
    pow_5 = pow_2 = 0
    while den % 5 == 0 or den % 2 == 0:
        if den % 5 == 0:
            pow_5 +=1
            den //= 5
        if den % 2 == 0:
            pow_2 += 1
            den //= 2
    return (max (pow_5, pow_2))

def wo_per (num, den: int) -> str:
    ans = '0,'
    dig = (num * 10) // den
    rest = (num * 10) % den
    ans += ('{:d}'.format(dig))
    while rest != 0:
        dig = (rest * 10) // den
        rest = (rest * 10) % den
        ans += ('{:d}'.format(dig))
    return (ans)

def per_ (num, den: int) -> str:
    ans = '('
    dig = (num * 10) // den
    rest_1 = (num * 10) % den
    ans += ('{:d}'.format(dig))
    dig = (rest_1 * 10) // den
    rest = (rest_1 * 10) % den
    while rest != rest_1:
        ans += ('{:d}'.format(dig))
        dig = (rest * 10) // den
        rest = (rest *10) % den
    ans += ')'
    return (ans)

if __name__=="__main__":
    num, den = map (int, input().split())
    rest, den = reduced_fr(num, den)
    if exist_per(den):
        ans = '0,'
        for i in range(pre_per(den)):
            dig = (rest * 10) // den
            rest = (rest * 10) % den
            ans += ('{:d}'.format(dig))
        ans += per_(rest, den)
    else:
        ans = wo_per(rest, den)
    print (ans)
            
        
