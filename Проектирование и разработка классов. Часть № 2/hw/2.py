class MakeNegative:
    def condition(self, x):
        return x > 0

    def transition(self, x):
        return -x


class Square:
    def condition(self, x):
        return True

    def transition(self, x):
        return x * x


class StrangeCommand:
    def condition(self, x):
        return x % 5 == 0

    def transition(self, x):
        return x + 1


def main():
    commands = {
        'make_negative': MakeNegative(),
        'square': Square(),
        'strange_command': StrangeCommand()
    }

    numbers = [int(s) for s in input().split()]
    n = int(input())
    for _ in range(n):
        com = input()
        command = commands[com]
        for i in range(len(numbers)):
            if command.condition(numbers[i]):
                numbers[i] = command.transition(numbers[i])
    print(' '.join(map(str, numbers)))


if __name__ == "__main__":
    main()

