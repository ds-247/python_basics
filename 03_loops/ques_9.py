items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set();

for item in items :
    if item in unique_items :
        print(item);
        break;
    else :
        unique_items.add(item)