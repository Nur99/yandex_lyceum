receiptIndex = 1
itemLines = []
totalCost = 0


def add_item(itemName, itemCost):
    global totalCost
    itemLines.append(itemName + " - " + str(itemCost))
    totalCost += itemCost


def print_receipt():
    global totalCost, receiptIndex
    if len(itemLines) > 0:
        print("Чек " + str(receiptIndex) + ". Всего предметов: " + str(len(itemLines)))
        for line in itemLines:
            print(line)
        print("Итого:", totalCost)
        print('-----')
        receiptIndex += 1
        totalCost = 0
        itemLines.clear()
