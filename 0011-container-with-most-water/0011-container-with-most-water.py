class Solution:
    def maxArea(self, height: List[int]) -> int:    
      left_pointer = 0
      right_pointer = len(height)-1
      max_water=0

      while left_pointer < right_pointer:
        width = right_pointer - left_pointer
        min_height = min(height[left_pointer], height[right_pointer]) 
        current_water_area = width * min_height
        max_water = max(current_water_area, max_water)

        if height[left_pointer] < height[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1
      return max_water            


