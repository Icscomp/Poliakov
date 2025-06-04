'''
переводит правильную дробь  в десятичную, выделив (если нужно), период
'''
num, den = map(int, input().split())
for i in range(den // 2, 1, -1):
    if num % i == 0 and den % i == 0:
        num //= i
        den //= i
n = den
pow_2 = pow_5 = 0
while n % 5 == 0 or n % 2 == 0:
    if n % 5 == 0:
        pow_5 += 1
        n //= 5
    if n % 2 == 0:
        pow_2 +=1
        n //= 2
ans = '0,'
if n == 1:
    dig, rest = divmod(num * 10, den)
    ans += ('{:d}'.format(dig))
    while rest != 0:
        dig, rest = divmod(rest*10, den)
        ans += ('{:d}'.format(dig))
else:
    rest = num
    for i in range(max(pow_5, pow_2)):
        dig, rest = divmod(rest * 10, den)
        ans += ('{:d}'.format(dig))
    ans += '('
    dig_1, rest_1 = divmod(rest * 10, den)
    dig, rest = divmod(rest_1 * 10, den)
    ans += ('{:d}'.format(dig_1))
    while dig_1 != dig and rest_1 != rest:
        ans += ('{:d}'.format(dig))
        dig, rest = divmod(rest * 10, den)
    ans += ')'
print(ans)
        
'''
3 14
0,2(142857)

3 7
0,(428571)

121 125
0,968
'''
    