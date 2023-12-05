# link : https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        strs={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        if(len(digits)==1):
            return strs[digits[0]]
        res=""
        for i in range(0,len(digits)):
            for j in range(i+1,len(digits)):
                if(len(digits)==3):
                    for l in range(j+1,len(digits)):
                            res = [ x+y+z for x in strs[digits[i]] for y in strs[digits[j]] for z in strs[digits[l]]]
                elif(len(digits)==4):
                    for l in range(j+1,len(digits)):
                        for k in range(l+1,len(digits)):
                                res = [ x+y+z+a for x in strs[digits[i]] for y in strs[digits[j]] for z in strs[digits[l]] for a in strs[digits[k]]]
                else:
                        res = [ x+y for x in strs[digits[i]] for y in strs[digits[j]]] 
        return res
    
                  
