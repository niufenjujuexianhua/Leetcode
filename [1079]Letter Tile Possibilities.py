# You have n tiles, where each tile has one letter tiles[i] printed on it. 
# 
#  Return the number of possible non-empty sequences of letters you can make usi
# ng the letters printed on those tiles. 
# 
#  
#  Example 1: 
# 
#  
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "AB
# A", "BAA".
#  
# 
#  Example 2: 
# 
#  
# Input: tiles = "AAABBC"
# Output: 188
#  
# 
#  Example 3: 
# 
#  
# Input: tiles = "V"
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= tiles.length <= 7 
#  tiles consists of uppercase English letters. 
#  
#  Related Topics Backtracking 
#  👍 845 👎 32


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        freq = [0] * 26
        for t in tiles:
            freq[ord(t) - ord('A')] += 1

        return self.dfs(freq, {})

    def dfs(self, freq, memo):
        hash = ''.join(map(str, freq))
        if hash in memo:
            return memo[hash]

        sum = 0
        for i in range(26):
            if freq[i] > 0:
                sum += 1
                freq[i] -= 1
                sum += self.dfs(freq, memo)
                freq[i] += 1

        memo[hash] = sum
        return sum



# print(Solution().numTilePossibilities('AAB'))
# leetcode submit region end(Prohibit modification and deletion)
