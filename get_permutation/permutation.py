from itertools import permutations

def print_permutation(uniq_list, s, e):
    if s == e:
        print uniq_list
    else:
        for i in range(s, e):
            uniq_list[s], uniq_list[i] = uniq_list[i], uniq_list[s]
            print_permutation(uniq_list, s+1, e)
            uniq_list[s], uniq_list[i] = uniq_list[i], uniq_list[s]
        

if __name__ == "__main__":
    print_permutation([1, 2, 3], 0, 3)