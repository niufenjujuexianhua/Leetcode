class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        import collections
        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)
        return r & m == r

class Solution2(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        import collections
        return not collections.Counter(ransomNote) - collections.Counter(magazine)


class Solution3(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True


class Solution4(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_dict = dict((i, magazine.count(i)) for i in magazine)

        for i in ransomNote:
            mag_dict[i] -= 1
            if mag_dict[i] < 0:
                return False
        return True

if __name__ == '__main__':
    result = Solution().canConstruct("a", "b")
    print(result)