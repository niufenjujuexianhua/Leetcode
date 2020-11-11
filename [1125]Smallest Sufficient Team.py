# In a project, you have a list of required skills req_skills, and a list of peo
# ple. The i-th person people[i] contains a list of skills that person has. 
# 
#  Consider a sufficient team: a set of people such that for every required skil
# l in req_skills, there is at least one person in the team who has that skill. We
#  can represent these teams by the index of each person: for example, team = [0, 
# 1, 3] represents the people with skills people[0], people[1], and people[3]. 
# 
#  Return any sufficient team of the smallest possible size, represented by the 
# index of each person. 
# 
#  You may return the answer in any order. It is guaranteed an answer exists. 
# 
#  
#  Example 1: 
#  Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"
# ],["nodejs","reactjs"]]
# Output: [0,2]
#  Example 2: 
#  Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], pe
# ople = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","cs
# harp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
# Output: [1,2]
#  
#  
#  Constraints: 
# 
#  
#  1 <= req_skills.length <= 16 
#  1 <= people.length <= 60 
#  1 <= people[i].length, req_skills[i].length, people[i][j].length <= 16 
#  Elements of req_skills and people[i] are (respectively) distinct. 
#  req_skills[i][j], people[i][j][k] are lowercase English letters. 
#  Every skill in people[i] is a skill in req_skills. 
#  It is guaranteed a sufficient team exists. 
#  
#  Related Topics Dynamic Programming Bit Manipulation 
#  👍 413 👎 9


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        n, m = len(req_skills), len(people)
        key = {v : i for i, v in enumerate(req_skills)}
        dp = {0:[]}

        for i, p in enumerate(people):
            my_skill = 0
            for skill in p:
                my_skill |= 1 << key[skill]

            for skillset, ppl in dp.items():
                with_mine = skillset | my_skill
                if with_mine == skillset:
                    continue
                if with_mine not in dp or len(dp[with_mine]) > len(ppl) + 1:
                    dp[with_mine] = ppl + [i]
        return dp[(1 << n) - 1]


# leetcode submit region end(Prohibit modification and deletion)
