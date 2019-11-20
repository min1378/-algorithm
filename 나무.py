import sys
from collections import defaultdict
input = sys.stdin.readline

tree_count = 0

def solve(board, nutritions, tree_dict, k):
    global tree_count
    num = 0
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]

    while num < k :

        for i in range(n*n):
            r = i // n
            c = i % n

            nutrition = board[r][c]
            add_nutrition = 0
            trees = tree_dict[(r,c)]

            if not trees:
                add_nutrition += nutritions[r][c]
                add_nutrition += nutrition
                board[r][c] = add_nutrition
                continue

            cnt = len(trees)
            temp_trees = []

            while 0 < cnt :
                tree = trees.pop()
                checked = nutrition - tree

                if 0 <= checked:
                    nutrition -= tree
                    temp_trees.append(tree+1)
                else:
                    add_nutrition += (tree//2)
                    tree_count -= 1
                cnt -=1
            
            tree.extend(temp_trees)

            if 1 < len(trees):
                trees.sort(reverse = True)

            
            add_nutrition += nutritions[r][c]
            add_nutrition += nutrition
            board[r][c] = add_nutrition

        
        for key, value in tree_dict.items():
            spread_tree_count = 0
            if len(value) == 0:
                continue
            
            for i in value:
                if i < 5 :
                    break
                if i % 5 == 0:
                    spread_tree_count += 1
            
            if spread_tree_count > 0:
                r, c = key
            
            for d in range(8) :
                temp_r = r + dr[d]
                temp_c = c + dc[d]
                if 0 <= temp_r < n and 0 <= temp_c < n:
                    tree_count += spread_tree_count
                    tree_dict[(temp_r, temp_c)].extend([1]*spread_tree_count)
        num += 1
    print(tree_count)
    return tree_count

if __name__ == "__main__"
    n, m, k = 
                