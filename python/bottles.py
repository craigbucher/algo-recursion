def bottles(num):
    # num_orig = num
    # print(num_orig)
    # if num == 1:
    #     print(f"{num} bottle of beer on the wall, {num} bottle of beer.")
    #     print("Take one down and pass it around, no more bottles of beer on the wall.")
    #     print("No more bottles of beer on the wall, no more bottles of beer.")
    #     print(f"Go to the store and buy some more, {num_orig} bottles of beer on the wall.")

    # print(f"{num} bottles of beer on the wall, {num} bottles of beer.")
    # print(f"Take one down and pass it around, {num - 1} bottles of beer on the wall.")
    # #bottles(num - 1)

    if num == 1:
        return print("Take one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the " \
                       "wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the " \
                       "wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy " \
                       "some more, 99 bottles of beer on the wall.")
        
    print(f"{num} Bottles of beer on the wall, {num} bottles of beer on the wall.\nTake one " \
             f"down pass it around, {num - 1} more on the wall. ")
 
    bottles(num - 1)

print(bottles(99))