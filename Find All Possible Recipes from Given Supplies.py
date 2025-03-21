# link L: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        done = []
        supplies = set(supplies)
        reciepies = dict(zip(recipes,ingredients))

        while True:
            new = False
            for r,i in [*reciepies.items()]:
                if not all(x in supplies for x in i):
                    continue
                done.append(r)
                supplies.add(r)
                del reciepies[r]
                new = True
            if not new:
                break
        return done


