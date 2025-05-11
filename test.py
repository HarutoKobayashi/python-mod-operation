# 例（ABC405E）

from main import ModInt, ModMath

mmath = ModMath()

A, B, C, D = list(map(ModInt, input().split()))

ans = mmath.cmb(A + B, A) * mmath.cmb(C + D - 1, D - 1)
for c in range(C):
    ans += mmath.cmb(A + B + c + 1, B) * mmath.cmb(C + D - c - 2, D - 1)

print(ans)
