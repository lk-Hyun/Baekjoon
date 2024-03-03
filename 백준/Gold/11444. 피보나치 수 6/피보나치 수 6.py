import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7

class Matrix:
    def __init__(self, data):
        self.data = data

    def __mul__(self, other):
        n = len(self.data)
        
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += self.data[i][k] * other.data[k][j]
                    result[i][j] %= MOD
        
        return Matrix(result)

    def __mod__(self, other):
        n = len(self.data)

        for i in range(n):
            for j in range(n):
                self.data[i][j] %= other

        return Matrix(self.data)


    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    
    def get_fibo(self):
        return self.data[0][1]

def power(x, n):
    if n == 0: return Matrix([1, 0], [0, 1])
    if n == 1: return x % MOD
    half = power(x, n // 2)

    if n & 1: return half * half * x
    else: return half * half

a = Matrix([[1, 1], [1, 0]])

n = int(input().rstrip())
print(power(a, n).get_fibo())