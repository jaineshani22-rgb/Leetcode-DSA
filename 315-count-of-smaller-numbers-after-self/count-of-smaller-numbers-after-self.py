class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        counts = [0] * n
        # Store pairs of (value, original_index)
        indexed_nums = [(nums[i], i) for i in range(n)]
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
                
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            return merge(left, right)
            
        def merge(left, right):
            merged = []
            i = j = 0
            right_smaller_count = 0
            
            while i < len(left) and j < len(right):
                # If left element is greater/equal, elements shifted from right are smaller
                if left[i][0] <= right[j][0]:
                    counts[left[i][1]] += right_smaller_count
                    merged.append(left[i])
                    i += 1
                else:
                    right_smaller_count += 1
                    merged.append(right[j])
                    j += 1
                    
            # Collect remaining elements for left side
            while i < len(left):
                counts[left[i][1]] += right_smaller_count
                merged.append(left[i])
                i += 1
                
            # Collect remaining elements for right side
            while j < len(right):
                merged.append(right[j])
                j += 1
                
            return merged
            
        merge_sort(indexed_nums)
        return counts