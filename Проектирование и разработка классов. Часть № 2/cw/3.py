from math import sqrt

# Конечно, проще воспользоваться функциями, но мы пока
# не проходили, что их можно класть в свойства.


class Identity:
    def call(self, x):
        return x


class SqrtFun:
    def call(self, x):
        return sqrt(x)


class Const:
    def __init__(self, value):
        self.value = value

    def call(self, x):
        return self.value


class Expression:
    def __init__(self, f1, op, f2):
        self.f1 = f1
        self.f2 = f2
        self.op = op

    def call(self, x):
        a = self.f1.call(x)
        b = self.f2.call(x)
        if self.op == '+':
            return a + b
        elif self.op == '-':
            return a - b
        elif self.op == '*':
            return a * b
        elif self.op == '/':
            return a / b


def main():
    functions = {'x': Identity(), 'sqrt_fun': SqrtFun()}
    n = int(input())
    for _ in range(n):
        command, *args = input().split()
        if command == "define":
            name, f1, op, f2 = args
            if f1.isdigit() or (f1[0] == '-' and f1[1:].isdigit()):
                f1 = Const(int(f1))
            else:
                f1 = functions[f1]
            if f2.isdigit() or (f2[0] == '-' and f2[1:].isdigit()):
                f2 = Const(int(f2))
            else:
                f2 = functions[f2]
            functions[name] = Expression(f1, op, f2)
        elif command == "calculate":
            name, *x_values = args
            print(' '.join(str(functions[name].call(int(x))) for x in x_values))


if __name__ == "__main__":
    main()

