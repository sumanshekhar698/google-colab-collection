# Goals form a tree: each goal has at most one parent. Each goal has a score. 
# A goal's total is its own score plus the totals of all its children.
# When the score of one goal changes, write update_totals(goal, parent, totals, delta).
# It should update the totals of that goal and of every ancestor, walking up to the root.

parents = {1: None, 2: 1, 3: 1, 4: 3}
totals = {1: 100, 2: 30, 3: 60, 4: 20}

# Goal 4's score went from 20 to 25
# update_totals(4, parent, totals, delta=5)]
# Output 
# totals == {1: 105, 2: 30, 3: 65, 4: 25}

# ancestor_list = {}

def update_totals(goal, parent, totals, delta):
    totals[goal] += delta
  
# 
    # for key,_ in parents.items():
    #     ancestor_list[key] = set()
    #     temp = key

    #     while parents.get(temp):
    #         ancestor_list[key].add(parents.get(temp))
    #         temp = parents.get(temp)
    
    
    temp = goal
    while parents.get(temp):
        totals[parents.get(temp)] += delta
        temp = parents.get(temp)

    # print(ancestor_list)


    return totals
# update_totals(4, parents, totals, 5)
print(update_totals(4, parents, totals, 5))