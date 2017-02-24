class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if len(s) == 0:
            return 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                return len(s) - i - 1
        return len(s)



class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = s.strip(" ").split(" ")
        return len(t[len(t) - 1])

if __name__ == '__main__':
    result = Solution().lengthOfLastWord(" a    ")
    print(result)