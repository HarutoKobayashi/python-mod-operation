# 例 （ABC405E）
# 前処理を実施するケース

## main.py ##
# MAXは登場しえる最大の数。これが 10e+7 だと時間ギリギリ（1700ms, 539MB）という感覚。
# 最初にここを修正すること
MAX = 10**7
MOD = 998244353

# 割り算・階乗を計算するかどうか。Trueの場合、事前にMAX回を計算する。Falseの場合、前処理を行わない。
cal_div = True

if cal_div:
    # fac[i] には i! が格納されている
    # finv[i] には (i!)^{-1} が格納されている
    # inv[i] には i^{-1} が格納されている
    fac = [1] + [1]
    finv = [1] + [1]
    inv = [0] + [1]

    for i in range(2, MAX):
        fac += [fac[-1] * i % MOD]
        inv += [MOD - inv[MOD % i] * (MOD // i) % MOD]
        finv += [finv[-1] * inv[i] % MOD]

    class ModInt:
        def __init__(self, x):
            self.x = int(x) % MOD

        def __str__(self):
            return str(self.x)

        __repr__ = __str__

        def __add__(self, other):
            return (
                ModInt(self.x + other.x)
                if isinstance(other, ModInt)
                else ModInt(self.x + other)
            )

        def __sub__(self, other):
            return (
                ModInt(self.x - other.x)
                if isinstance(other, ModInt)
                else ModInt(self.x - other)
            )

        def __mul__(self, other):
            return (
                ModInt(self.x * other.x)
                if isinstance(other, ModInt)
                else ModInt(self.x * other)
            )

        def __truediv__(self, other):
            return (
                ModInt(self.x * inv[other.x])
                if isinstance(other, ModInt)
                else ModInt(self.x * inv[other])
            )

        def __pow__(self, other):
            return (
                ModInt(pow(self.x, other.x, MOD))
                if isinstance(other, ModInt)
                else ModInt(pow(self.x, other, MOD))
            )

        def __radd__(self, other):
            return ModInt(self.x + other)

        def __rsub__(self, other):
            return (
                ModInt(other.x - self.x)
                if isinstance(other, ModInt)
                else ModInt(other - self.x)
            )

        def __rmul__(self, other):
            return ModInt(self.x * other)

        def __rtruediv__(self, other):
            return (
                ModInt(other.x * inv[self.x])
                if isinstance(other, ModInt)
                else ModInt(other * inv[self.x])
            )

        def __rpow__(self, other):
            return (
                ModInt(pow(other.x, self.x, MOD))
                if isinstance(other, ModInt)
                else ModInt(pow(other, self.x, MOD))
            )

        def __int__(self):
            return self.x

        def __index__(self):
            return self.x

        def __lt__(self, other):
            return (
                self.x < other.x
                if isinstance(other, ModInt)
                else self.x < ModInt(other).x
            )

        def __gt__(self, other):
            return (
                self.x > other.x
                if isinstance(other, ModInt)
                else self.x > ModInt(other).x
            )

        def __le__(self, other):
            return (
                self.x <= other.x
                if isinstance(other, ModInt)
                else self.x <= ModInt(other).x
            )

        def __ge__(self, other):
            return (
                self.x >= other.x
                if isinstance(other, ModInt)
                else self.x >= ModInt(other).x
            )

        def __eq__(self, other):
            return (
                self.x == other.x
                if isinstance(other, ModInt)
                else self.x == ModInt(other).x
            )

        def __ne__(self, other):
            return (
                self.x != other.x
                if isinstance(other, ModInt)
                else self.x != ModInt(other).x
            )

    class ModMath:
        def __init__(self):
            pass

        def cmb(self, n, k):
            if isinstance(n, ModInt):
                n = n.x
            if isinstance(k, ModInt):
                k = k.x
            if n < 0 or k < 0 or n < k:
                return 0
            return ModInt(fac[n] * finv[k] * finv[n - k])

        def factorial(self, x):
            if isinstance(x, ModInt):
                x = x.x
            return ModInt(fac[x])

else:

    class ModInt:
        def __init__(self, x):
            self.x = int(x) % MOD

        def __str__(self):
            return str(self.x)

        __repr__ = __str__

        def __add__(self, other):
            return (
                ModInt(self.x + other.x)
                if isinstance(other, ModInt)
                else ModInt(self.x + other)
            )

        def __sub__(self, other):
            return (
                ModInt(self.x - other.x)
                if isinstance(other, ModInt)
                else ModInt(self.x - other)
            )

        def __mul__(self, other):
            return (
                ModInt(self.x * other.x)
                if isinstance(other, ModInt)
                else ModInt(self.x * other)
            )

        # def __truediv__(self, other):
        #     return (
        #         ModInt(self.x * inv[other.x])
        #         if isinstance(other, ModInt)
        #         else ModInt(self.x * inv[other])
        #     )

        def __pow__(self, other):
            return (
                ModInt(pow(self.x, other.x, MOD))
                if isinstance(other, ModInt)
                else ModInt(pow(self.x, other, MOD))
            )

        def __radd__(self, other):
            return ModInt(self.x + other)

        def __rsub__(self, other):
            return (
                ModInt(other.x - self.x)
                if isinstance(other, ModInt)
                else ModInt(other - self.x)
            )

        def __rmul__(self, other):
            return ModInt(self.x * other)

        # def __rtruediv__(self, other):
        #     return (
        #         ModInt(other.x * inv[self.x])
        #         if isinstance(other, ModInt)
        #         else ModInt(other * inv[self.x])
        #     )

        def __rpow__(self, other):
            return (
                ModInt(pow(other.x, self.x, MOD))
                if isinstance(other, ModInt)
                else ModInt(pow(other, self.x, MOD))
            )

        def __int__(self):
            return self.x

        def __index__(self):
            return self.x

        def __lt__(self, other):
            return (
                self.x < other.x
                if isinstance(other, ModInt)
                else self.x < ModInt(other).x
            )

        def __gt__(self, other):
            return (
                self.x > other.x
                if isinstance(other, ModInt)
                else self.x > ModInt(other).x
            )

        def __le__(self, other):
            return (
                self.x <= other.x
                if isinstance(other, ModInt)
                else self.x <= ModInt(other).x
            )

        def __ge__(self, other):
            return (
                self.x >= other.x
                if isinstance(other, ModInt)
                else self.x >= ModInt(other).x
            )

        def __eq__(self, other):
            return (
                self.x == other.x
                if isinstance(other, ModInt)
                else self.x == ModInt(other).x
            )

        def __ne__(self, other):
            return (
                self.x != other.x
                if isinstance(other, ModInt)
                else self.x != ModInt(other).x
            )


mmath = ModMath()

A, B, C, D = list(map(ModInt, input().split()))

ans = mmath.cmb(A + B, A) * mmath.cmb(C + D - 1, D - 1)
for c in range(C):
    ans += mmath.cmb(A + B + c + 1, B) * mmath.cmb(C + D - c - 2, D - 1)

print(ans)
