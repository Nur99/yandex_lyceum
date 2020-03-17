import sys

print(not all(int(i) for i in sys.stdin.read().split()))

