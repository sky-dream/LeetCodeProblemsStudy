# -*- coding: utf-8 -*-
# leetcode time     cost : 1800 ms
# leetcode memory   cost : 51.1 MB
# Time  Complexity: O(M * 2**N), M is the people number, N is the req skills number
# Space Complexity: O(M * 2**N)
# solution 1，dp，
from typing import List
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]):
        # 为skills建立字典
        n = len(req_skills)
        d = dict()
        for i in range(n):
            d[req_skills[i]] = i
        # 所有状态,起始设置最少人数为当前已遍历人数，即人数最大值，dp[skills_binary][i] = [0:i],
        dp = [list(range(len(people))) for _ in range(1 << n)]
        # 需求技能为0时，不需要人员
        dp[0] = []
        # 遍历所有人
        for i in range(len(people)):
            # 求这个人的可以满足需求技能的二进制整数skills_binary
            skill = 0
            for s in people[i]:
                skill |= (1 << d[s])
            # 遍历所有技能组合 k 对应的人员组合列表 v = [.......],人数即len(v)
            for k, v in enumerate(dp):
                # 把这个人的技能skill加入进当前组合k以后的团队技能
                new_skills = k | skill
                # 如果团队技能因此而增加 并且增加后的人数比新技能原来的人数少 则更新答案
                if new_skills != k and len(dp[new_skills]) > len(v) + 1:
                    dp[new_skills] = v + [i]
        return dp[(1 << n) - 1]


def main():
    req_skills = ["algorithms", "math", "java",
                  "reactjs", "csharp", "aws"]
    people = [["algorithms", "math", "java"], ["algorithms", "math", "reactjs"], [
        "java", "csharp", "aws"], ["reactjs", "csharp"], ["csharp", "math"], ["aws", "java"]]
    # expect is [1,2]
    obj = Solution()
    res = obj.smallestSufficientTeam(req_skills, people)
    print("return value is ", res)


if __name__ == '__main__':
    main()
