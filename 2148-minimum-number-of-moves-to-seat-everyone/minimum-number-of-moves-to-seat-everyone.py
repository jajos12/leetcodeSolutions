class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        sum_o = 0
        for i, j in zip(seats, students):
            sum_o += abs(i - j)
        return sum_o
