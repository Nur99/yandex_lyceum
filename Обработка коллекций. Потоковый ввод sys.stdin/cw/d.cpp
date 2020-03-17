import sys
comments = filter(lambda line: line.lstrip().startswith('#'), sys.stdin)
print(len(list(comments)))
