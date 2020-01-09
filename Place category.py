import pandas as pd
import regex
import itertools


def walk_through(data, dictionary, j):
    for i, line in enumerate(data):
        for d in dictionary.keys():
            c = len(line)
            a = set(line)
            b = set(d)
            if type(d) == str:
                g = set(line).difference({d})
            else:
                g = set(line).difference(set(d))
            e = len(g)
            if len(line) - len(g) == j:
                dictionary[d].append(i)

    return dictionary


def delete_not_important_ones(itemset, minsup):
    pop_list = []
    for k, v in itemset.items():
        if len(v) < minsup:
            pop_list.append(k)
    for k in pop_list:
        itemset.pop(k)
    return itemset


def apriori_alg(data, itemset, min_sup, final_itemset, i):
    new_itemset = list(itertools.combinations(final_itemset, i))
    values = [[] for _ in range(len(new_itemset))]
    new_itemset = {key: value for (key, value) in zip(new_itemset, values)}
    # itemset.update({key: len(value) for (key, value) in itemset.items()})
    dict = walk_through(data, new_itemset, i)
    itemset = delete_not_important_ones(dict, min_sup)
    final_itemset.update({key: len(value) for (key, value) in itemset.items()})
    if len(itemset) == 0 or len(itemset) == 1:
        return final_itemset

    i = + 1
    apriori_alg(data, new_itemset, min_sup, final_itemset, i)


if __name__ == "__main__":
    f = open('categories_lite.txt')
    g = open('categories_lite.txt', 'r')
    # with  open('categories.txt', 'r') as a:
    #     b = a.read()
    #     print(b)
    data_processed = [line for line in g]
    data_processed = [s.strip('\n') for s in data_processed]
    data_processed = [s.split(',') for s in data_processed]
    new_data = []
    for el in data_processed:
        new_data.append(list(dict.fromkeys(el[0].split(';'))))
    print(new_data)
    data = f.read()

    # print(data)
    itemset_categories = data.replace('\n', ';').split(';')
    itemset_categories = list(dict.fromkeys(itemset_categories))
    print(itemset_categories)
    values = [[] for _ in range(len(itemset_categories))]
    itemset_cat_dict = {key: value for (key, value) in zip(itemset_categories, values)}
    lel = walk_through(new_data, itemset_cat_dict, 1)
    f_itemset = delete_not_important_ones(itemset_cat_dict, 5)
    f_itemsett = {key: len(value) for (key, value) in f_itemset.items()}
    # new_itemset = itertools.combinations(itemset_cat_dict, 2)
    # for i in new_itemset:
    #     print(i)
    min_sup = int(len(data_processed) * 0.001)
    a = apriori_alg(new_data, itemset_cat_dict, min_sup, f_itemsett, 2)
    print(a)
    # a = ['Breakfast & Brunch']
    # b = set(new_data[0])
    # print(len(b.difference(a)))
    # print(len(b))
