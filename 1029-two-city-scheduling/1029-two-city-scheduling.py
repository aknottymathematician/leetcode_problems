class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        firstCity = [i for i, j in costs]
        diffCost = [j-i for i, j in costs]
        return sum(firstCity) + sum(sorted(diffCost)[:len(costs)//2])