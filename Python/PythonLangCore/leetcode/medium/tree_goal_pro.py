children = {"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": [], "E": []}
parents  = {"B": ["A"], "C": ["A"], "D": ["B", "C"], "E": ["C"], "A": []}
# score_original    = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}   # D was just changed from 4 to 10
score    = {"A": 1, "B": 2, "C": 3, "D": 10, "E": 5}   # D was just changed from 4 to 10
totals   = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 5}    # stale values, only E's is still valid

# TODO
def update_totals(goal, parents, children, score, totals):
    temp_scores = {}
    def calculate_score(current, goal):
        if parents.get(current):
            temp_scores
        # elif
        #     return
        temp_scores[current]+=score[current]


    for key,_ in parents:

        






print(update_totals("D", parents, children, score, totals))


#   Output

#   {"D": 10, "B": 12, "C": 18, "A": 31}

#   ┌──────┬─────────────────────────────────────────────────────────────────┬───────┐
#   │ Goal │                           Calculation                           │ Total │
#   ├──────┼─────────────────────────────────────────────────────────────────┼───────┤
#   │ D    │ leaf, so its own score                                          │ 10    │
#   ├──────┼─────────────────────────────────────────────────────────────────┼───────┤
#   │ B    │ 2 + D (10)                                                      │ 12    │
#   ├──────┼─────────────────────────────────────────────────────────────────┼───────┤
#   │ C    │ 3 + D (10) + E (5), with E read as-is because it isn't affected │ 18    │
#   ├──────┼─────────────────────────────────────────────────────────────────┼───────┤
#   │ A    │ 1 + B (12) + C (18)                                             │ 31    │
#   └──────┴─────────────────────────────────────────────────────────────────┴───────┘

#   E is not in the output because it isn't an ancestor of D. D's 10 is counted in both B and C, so it shows up twice in A.