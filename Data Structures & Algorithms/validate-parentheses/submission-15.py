class Solution:
    def isValid(self, s: str) -> bool:
        valid = True
        stringArr = [] 
        
        brackets = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }
        
        for letter in s:
            if letter in brackets:
                if len(stringArr) != 0 and stringArr[-1] == brackets[letter]:
                    stringArr.pop()
                else:
                    valid = False
                    break
            else:
                stringArr.append(letter)
        
        if len(stringArr) != 0:
            valid = False
            
        return valid