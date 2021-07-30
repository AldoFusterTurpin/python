# ALDO FUSTER TURPIN

import sys
 
def main():
    n_elements_in_set = input()
    # print(f"n_elements_in_set: {n_elements_in_set}")

    my_set = input().split()
    my_set = set([int(x) for x in my_set])

    # print(f"my_set: {my_set}")

    n_other_sets = int(input())
    # print(f"n_other_sets: {n_other_sets}")

    for i in range(n_other_sets):
        treat_case(my_set)
    
    print(sum(my_set))
    
def treat_case(my_set: set[int]):
    action, n_elements = input().split()
    # print(f"action: {action}")
    # print(f"n_elements: {n_elements}")
    
    other_set = input().split()
    other_set = set([int(x) for x in other_set])
    # print(f"other_set: {other_set}")
    # print(f"type of other_set: {type(other_set)}")

    
    if action == "update":
        my_set.update(other_set)
        # print(f"my_set: {my_set}")
    if action == "intersection_update":
        my_set.intersection_update(other_set)
        # print(f"my_set: {my_set}")
    if action == "difference_update":
        my_set.difference_update(other_set)
        # print(f"my_set: {my_set}")
    if action == "symmetric_difference_update":
        my_set.symmetric_difference_update(other_set)
        # print(f"my_set: {my_set}")
    
if __name__ == "__main__":
    main()
