n = 5

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n-1) * n

def all_permutations(n):
    
    permutations = []

    # elements of list
    elements = list(map(str, range(1, n+1)))
    #permutations.append(elements)  # first, natural ordering

    # initialization
    for e in elements:
        permutations.append(e)

    # grow
    for _ in range(n-1):
        
        new_permutations = []
        for perm in permutations:
            
            for e in elements:
                
                if e not in perm:
                    new_permutations.append(perm+e)
                else:
                    pass
    
        permutations = new_permutations[:]

    assert len(permutations) == factorial(n)

    return permutations

permutations = all_permutations(n)

print(len(permutations))
for perm in permutations:
    print(" ".join(list(perm)))