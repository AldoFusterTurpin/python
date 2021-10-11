# ALDO FUSTER TURPIN

# Input 1
# 1 x
# 1 y
# 1 z
# 2 n
# Expected output
#[[0, 0, 0], 
#[0, 0, 1], 
#[0, 1, 0], 
#[1, 0, 0], 
#[1, 1, 1]]

def perform_permutations_no_list_comprehensions(x, y, z, n):
    permutations = []
    for i in range(x+1):
        for j in range(y+1):          
            for k in range(z+1):
                if i + j + k != n:
                    permutations.append([i,j,k])
    return permutations

def perform_permutations(x, y, z, n):
    return [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
    
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(perform_permutations(x, y, z, n))
