#  Мы можем создавать деревья по мере того, как появляются ссылки на них
#   (т.е. по мере создания переменных)
white = []
black = [white, white, white]
white.append(black)
white.append(black)
#  Корень - черный, т.е. фактически, черное "дерево"
wb_tree = black
