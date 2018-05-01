def insert_val_at(index, my_list, value):
    if index < 0 or index >= len(my_list):
        return False
    my_list.append(value)
    for i in range(len(my_list)-1, index, -1):
        my_list[i], my_list[i-1] = my_list[i-1], my_list[i]
    return my_list

