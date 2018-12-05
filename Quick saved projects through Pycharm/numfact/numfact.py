def getPrimes():
    data = [];
    arr = [0 for x in range(0, 1000001)];
    for i in range(2, 1000001):
        if arr[i] != 1:
            j = i * 2;
            while j <= 1000000:
                arr[j] = 1;
                j += i;
    for i in range(2, len(arr)):
        if arr[i] == 0:
            data.append(i);
    return data;


def getFactors(factors, primes, n):
    k = n;
    for x in primes:
        if x > k:
            break;
        while n % x == 0 and n >= x:
            if x in factors:
                factors[x] += 1;
            else:
                factors[x] = 1;
            n /= x;
    return factors;


data = getPrimes();
t = int(input());
while t:
    n = int(input());
    factors = dict();
    arr = [int(x) for x in input().split()];
    res = 1;
    for x in arr:
        factors = getFactors(factors, data, x);
    for key, value in factors.items():
        res *= (value + 1);
    print(res);
    t -= 1;