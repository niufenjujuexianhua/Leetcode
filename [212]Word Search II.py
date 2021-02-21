# Given an m x n board of characters and a list of strings words, return all wor
# ds on the board. 
# 
#  Each word must be constructed from letters of sequentially adjacent cells, wh
# ere adjacent cells are horizontally or vertically neighboring. The same letter c
# ell may not be used more than once in a word. 
# 
#  
#  Example 1: 
# 
#  
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f"
# ,"l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#  
# 
#  Example 2: 
# 
#  
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 12 
#  board[i][j] is a lowercase English letter. 
#  1 <= words.length <= 3 * 104 
#  1 <= words[i].length <= 10 
#  words[i] consists of lowercase English letters. 
#  All the strings of words are unique. 
#  
#  Related Topics Backtracking Trie 
#  👍 3437 👎 141


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # from collections import defaultdict
        trie = {}
        for word in words:
            p = trie
            for c in word:
                if c not in p:
                    p[c] = {}
                p = p[c]
            p['#'] = True

        m, n = len(board), len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                self.bt(i, j, board, trie, '', res)
        return res

    def bt(self, i, j, board, trie, path, res):
        if '#' in trie:
            res.append(path)
            del trie['#']
            # return
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] not in trie:
            return

        tmp = board[i][j]
        board[i][j] = '#'
        self.bt(i, j + 1, board, trie[tmp], path + tmp, res)
        self.bt(i + 1, j, board, trie[tmp], path + tmp, res)
        self.bt(i, j - 1, board, trie[tmp], path + tmp, res)
        self.bt(i - 1, j, board, trie[tmp], path + tmp, res)
        board[i][j] = tmp

# print(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
#                            ["oath","oathk"]))
# ls = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
# words = ["oath","oathk"]
# for i in range(len(words)):
#     print(Solution().findWords(
#     ls,
#     [words[0], words[i]]))
'''
a b c
a e d 
a f g
'''
# leetcode submit region end(Prohibit modification and deletion)
