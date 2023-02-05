def longest(tree):

    if tree == [] or tree==None:
        return 0
    
    depth,count=_longest(tree)
    return depth

def _longest(tree):
    # left_count=0
    # right_count=0
    # left_depth=0
    # right_depth=0
    # depth=0
    # count=0
    # if Arr==[]:
    #     return -1
    if tree == []:
        return 0,0
    else:
        # passing the left subtree 
        left_count,left_depth= _longest(tree[0]) 
        # passing the right subtree
        right_count,right_depth= _longest(tree[2])
        depth= max(left_depth,right_depth)+1
        count=max(left_count,right_count,left_depth+right_depth)
        return count,depth




# if __name__ == '__main__':
#     # k=int(input())
#     # Arr = list(map(int, input().rstrip().split()))
#     # k=2
#     # Arr=[3,1,2,4,7,6,5,9,8]
#     tree=[[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]
#     # Arr=[[[], 1, []], 2, [[], 3, []]]
#     # Arr=[[[], 1, [[], 2, []]], 3, [[], 4, [[[[], 5, []], 6, []], 7, [[[], 8, []], 9, []]]]]
#     # Arr=[1]
#     # res=sort(Arr)
#     print(longest(tree))
    # print(res)
