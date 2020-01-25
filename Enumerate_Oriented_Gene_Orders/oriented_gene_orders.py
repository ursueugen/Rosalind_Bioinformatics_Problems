"""
.
"""

n = 5

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

    return permutations


def generate_masks(n: int):
    """Generates lisks of all posible binary masks of length n."""
    alph = [0, 1]
    
    masks = [[0], [1]]
    
    for _ in range(n-1):
        new_masks = []
        for mask in masks:
            for char in alph:
                new_masks.append(mask + [char])
        masks = new_masks[:]

    return masks


def signed_permutations(n: int):
    """Derives all possible signed permutations for n."""

    perms = all_permutations(n)

    masks = generate_masks(n)

    signed_perms = []
    for perm in perms:
        for mask in masks:
            
            characters = []
            for i in range(n):
                if mask[i] == 1:
                    characters.append('-' + perm[i]) 
                else:
                    characters.append(perm[i])
            signed_perm = " ".join(characters)
            signed_perms.append(signed_perm)
    
    return signed_perms


sg_perms = signed_permutations(n)
print(len(sg_perms))
print("\n".join(sg_perms))