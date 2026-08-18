class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      
        count = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 1
                
            else:
                count[s[i]] += 1

        for i in range(len(t)):
            if t[i] in count:
                count[t[i]] -=1
            else:
                count[t[i]] = 1

        print(count)
        return all(value == 0 for value in count.values())

