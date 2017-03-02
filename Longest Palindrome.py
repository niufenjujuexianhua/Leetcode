class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        res = 0
        single = 0

        for i in s:
            dict[i] = dict.get(i, 0) + 1

        for i in dict:
            if dict[i] % 2 == 0:
                res += dict[i]
            else:
                single = 1
                res += dict[i] - 1
        return res + single


class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = []
        count = 0
        for i in s:
            if i not in ls:
                ls.append(i)
            else:
                count += 1
                ls.remove(i)
        if len(ls) != 0:
            return count*2 + 1
        else:
            return count*2


class Solution3(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = []
        for i in s:
            if i not in ls:
                ls.append(i)
            else:
                ls.remove(i)
        if len(ls) != 0:
            return len(s) - len(ls) + 1
        else:
            return len(s) - len(ls)

        
if __name__ == '__main__':
    result = Solution3().longestPalindrome("bb")
    print(result)