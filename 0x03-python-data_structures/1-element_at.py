#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        print('{None}'.format(idx))
    elif idx > len(my_list):
        print('{None}'.format(idx))
    else:
        return(my_list[idx])
