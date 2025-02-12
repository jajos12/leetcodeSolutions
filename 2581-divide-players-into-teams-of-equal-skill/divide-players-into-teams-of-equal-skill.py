class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) - 1
        grp_skill = skill[left] + skill[right]
        answer = 0
        while left < right:
            if skill[right] + skill[left] != grp_skill:
                return -1
            answer += skill[left]*skill[right]
            left += 1
            right -= 1
        return answer