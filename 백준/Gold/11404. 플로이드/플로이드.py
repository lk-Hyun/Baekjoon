import sys
import math
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
dist = [[0 if i == j else math.inf for j in range(n)] for i in range(n)]

for _ in range(m):
  x, y, z = map(int, input().rstrip().split())
  dist[x-1][y-1] = min(dist[x-1][y-1], z)

for k in range(n):
  for i in range(n):
    for j in range(n):
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

[print(' '.join(map(lambda x: str(x) if x != math.inf else '0', row))) for row in dist]
