def take_large_banknotes(banknotes):
    wallet = []
    for banknote in banknotes:
        if banknote > 10:
            wallet.append(banknote)
    return wallet
