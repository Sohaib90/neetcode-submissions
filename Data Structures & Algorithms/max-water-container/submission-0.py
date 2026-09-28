class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxContainer = 0

        lefth = 0
        righth = len(heights) - 1

        while lefth < righth:
            r_h = heights[righth]
            l_h = heights[lefth]
            area = ( righth - lefth ) * min(r_h, l_h)
            maxContainer = max(maxContainer, area)

            if l_h < r_h:
                lefth += 1
            else:
                righth -=1

        return maxContainer