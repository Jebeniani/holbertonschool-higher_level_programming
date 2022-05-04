#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newl = my_list.copy()
    for idx, i in enumerate(my_list):
        if i == search:
            newl[idx] = replace
    return newl
