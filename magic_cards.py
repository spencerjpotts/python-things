"""
    @file: magic_cards.py
    @author: Spencer j Potts
    @Date: 4/11/2019
    @Description: turn based guess your number game.


    ##CREATE EACH COLUMN
    COLUMN 1
    # 1*1 = 1, (3*1)+1 = 4, (3*2)+1=7, (3*3)+1=10, (3*4)+1=13, (3*5)+1=16, (3*6)+1=19
    # 3 * (1*i) + 1 = 4 
    
    COLUMN 2
    # 2*1 = 2, 2*2=4, 2*3=6, 2*4=8,  2*5=10, 2*6=12, 2*7=14
    # (3*i) - 1

    COLUMN 3
    # 3*1 = 3, 3*2=6, 3*3=9, 3*4=12, 3*5=15, 3*6=18, 3*7=21
    # (3*i)

    
    ##SORTING CARDS
    # 3 * (1*i) + 1       |  ((3*(1*1)) + 1) = 4 
    #(3*i) - 1            |  3*2 = 5
    # 3*i                 |  3*2 = 6

    _ _ _ _ _ _ _ | _ _  _  _  _  _  _ |  _  _  _  _  _  _  _ 
    1 2 3 4 5 6 7   8 9 10 11 12 13 14   15 16 17 18 19 20 21

    PICK: 1
    COLUMN: 1

    _ _ _ _ _ _ _ 
    1 2 3 4 5 6 7 = COLUMN 1

    _ _  _  _  _  _  _ | _ _ _ _ _ _ _ | _  _  _  _  _  _  _ 
    8 9 10 11 12 13 14 | 1 2 3 4 5 6 7 | 15 16 17 18 19 20 21

    REVERSED
     _  _  _  _  _  _  _ | _ _ _ _ _ _ _ | _  _  _  _  _  _  _ 
    21 20 19 18 17 16 15   7 6 5 4 3 2 1  14 13 12 11 10  9  8

    ∑
    3*1   21 20 19
    3*2   18 17 16
    3*3   15 7  6
    3*4   5  4  3
    3*5   2  1  14
    3*6   13 12 11
    3*7   10 9  8

    3*1   pointer = [1][1 - 3] : 21 20 19
    3*2   pointer = [2][1 - 3] : 18 17 16
    3*3   pointer = [3][1 - 3] : 15 7  6
    3*4   pointer = [4][1 - 3] : 5  4  3
    3*5   pointer = [5][1 - 3] : 2  1  14
    3*6   pointer = [6][1 - 3] : 13 12 11
    3*7   pointer = [7][1 - 3] : 10 9  8

    
    SORTING CARDS INTO STACK
    stack=[]
    cards=[21]
    for card in cards:
        if 3 * index == 3:
            stack=cards[i - 2]
            stack=cards[i - 1]
            stack=cards[i]



    1) .display set of 21 cards in rows of 7 with 3 columns. 3*7
    1) .user selects a card and types in the column number column.
    1) .columns then get put in to the stack with the users columns choice placed into the middle.
    3) .items from the stack are then poped off the top of the stack back on to the field.


    template:
    |\t{0}\t|\t{1}\t|\t{2}\t|
    |\t{3}\t|\t{4}\t|\t{5}\t|
    |\t{6}\t|\t{7}\t|\t{8}\t| 
    |\t{9}\t|\t{10}\t|\t{11}\t| 
    |\t{12}\t|\t{13}\t|\t{14}\t| 
    |\t{15}\t|\t{16}\t|\t{17}\t| 
    |\t{18}\t|\t{19}\t|\t{20}\t| 

    
    ∑
    3*1   21 20 19
    3*2   18 17 16
    3*3   15 7  6
    3*4   5  4  3
    3*5   2  1  14
    3*6   13 12 11
    3*7   10 9  8

"""
# cards = [None, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
cards = [None, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'J', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']


def sortItems(items, col):
    col_1 = []
    col_2 = []
    col_3 = []

    stack = []
    stack.append(None)
    for x in range(1, 8):
        for y in range(1, 4):
            col_1.append(items[(3*x - 2)])
            col_2.append(items[(3*x - 1)])
            col_3.append(items[(3*x)])
            break
    if col == 1:
        stack.extend(col_3)
        stack.extend(col_1)
        stack.extend(col_2)
    elif col == 2:
        stack.extend(col_1)
        stack.extend(col_2)
        stack.extend(col_3)
    elif col == 3:
        stack.extend(col_2)
        stack.extend(col_3)
        stack.extend(col_1)

    return stack


def showColumns(cards):
    for x in range(1, 8):
        for y in range(1, 4):
            print("\t{0}\t{1}\t{2}".format(cards[(3*x - 2)], cards[(3*x - 1)], cards[(3*x)]))
            break


# initial card and column selection.
showColumns(cards)
column = int(input("Column 'Attempt {0}': ".format(1)))
stack = sortItems(cards, column)
showColumns(stack)

for i in range(2, 4):
    # print("Attempt: ", i)
    column = int(input("Column 'Attempt {0}': ".format(i)))
    stack = sortItems(stack, column)
    showColumns(stack)
    # print(stack)
    if i == 3:
        print("YOUR CARD: ", stack[11])
