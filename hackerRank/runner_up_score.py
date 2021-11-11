# ALDO FUSTER TURPIN

def getRunnerUpScore(scores):
    the_set = set(scores)
    the_list = sorted(the_set, reverse=True)
    if len(the_list) > 1:
        return the_list[1]
    return the_list[0]
    

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(getRunnerUpScore(list(arr)))
