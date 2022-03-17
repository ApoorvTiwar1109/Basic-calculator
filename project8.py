list1 = [1, 5, "Microsoft", 17, 14, 21, "Tesla", 28, 5, 6, 3, "Facebook", 12, 9, 0]
for items in list1:
    if str(items).isnumeric() and items>6:
        print(items)