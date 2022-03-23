import random

money = 1500

start = input("Start Game?")
if start == "yes":
    roll_want = input("Roll Dice?")
    if roll_want == "yes":
        roll = 0

        value = random.randint(0, 0)

        board = ["Collect Go", "Old Kent Road", "Community Chest", "White Chapel Road", "Income Tax",
                 "Kings Cross Station", "The Angel Islington", "Chance", "Euston Road", "Pentoville Road"]
        print(board[roll + value])
        if board == "Collect Go":
            buy == input("Buy or leave")
        money + 200
        print(money)
