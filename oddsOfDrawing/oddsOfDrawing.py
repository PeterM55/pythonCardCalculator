def cardProb(drawn, available, total):
    runningOdds = 1
    for i in range(drawn):
        runningOdds *= (available/total)
        available -= 1
        total -= 1

    print("The odds of drawing it every time: %.5f percent" % (runningOdds*100))

while True:
    numDraw = int(input("number of times drawn: "))
    ava = int(input("number of the specific card: "))
    total = int(input("total number of cards: "))
    cardProb(numDraw, ava, total)
    print("\n")
