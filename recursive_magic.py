"""
    @file: recursive_magic.py
    @author: Spencer j Potts
    @Date: 4/18/2019 : 3:00am
    @Description: recursive example of guess your number game.

"""

def sortItems(items, iteration=1):
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

    # display the columns 
    print("\t1\t2\t3\n\t_\t_\t_\n")
    for x in range(1, 8):
        for y in range(1, 4):
            print("\t{0}\t{1}\t{2}".format(items[(3*x - 2)], items[(3*x - 1)], items[(3*x)]))
            break
    
    # accept user input for column selection.
    column = int(input("Column 'Attempt {0}': ".format(iteration)))
    if column == 1:
        stack.extend(col_3)
        stack.extend(col_1)
        stack.extend(col_2)
    elif column == 2:
        stack.extend(col_1)
        stack.extend(col_2)
        stack.extend(col_3)
    elif column == 3:
        stack.extend(col_2)
        stack.extend(col_3)
        stack.extend(col_1)
    

    # base case
    if iteration == 1:
        return sortItems(stack, iteration=iteration + 1)
    elif iteration == 2:
        return sortItems(stack, iteration=iteration + 1)
    elif iteration == 3:
        return stack[11]


cards = [None, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']
print("Select a letter then tell me the column it's in.")
print("Your letter: ", sortItems(cards))