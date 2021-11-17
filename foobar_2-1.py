from itertools import combinations
def solution(l):
    # Your code here
    # divisibility rule of 3?
    # reverse sort the list check if sum % 3 == 0
    # if no then just remove first digit in list
    # reaLized no permutations, because sum is all that's needed
    # apparently len() is O(1)
    # learned that pop() is O(1) and pop(0) is O(n)
    # using itertools.combinations, this solution is probably slow
    list.sort(l, reverse=True)
    for n in range(len(l), 0, -1):
        perms = list(combinations(l, n))
        perms = [sorted(list(perm), reverse=True) for perm in perms]
        for perm in perms:
            if sum(perm) % 3 == 0:
                return int(''.join(map(str, perm)))
    return 0
# solution for when I didn't account for permutations and only popping from l  
#    list.sort(l, reverse=True)
#    def solution_aux(l, n):
#        if sum(l) % 3 == 0:
#            return int(''.join(map(str, l)))
#        elif n != 0:
#            l.pop()
#            solution_aux(l, n - 1)
#        else:
#            return 0
#    return solution_aux(l)
