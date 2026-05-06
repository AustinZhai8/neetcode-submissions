class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = {}

        for word in strs:
            clean = "".join(sorted(word))

            if clean in output:
                output[clean].append(word)
            else:
                output[clean] = [word]
        
        return list(output.values())