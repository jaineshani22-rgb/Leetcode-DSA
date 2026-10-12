class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
       if valueDiff < 0:
            return False
            
       bucket = {}
       w = valueDiff + 1
        
       for i, num in enumerate(nums):
            # Python's integer division naturally floors towards negative infinity
            bucket_id = num // w
            
            # Check if bucket already contains a number (difference <= valueDiff)
            if bucket_id in bucket:
                return True
                
            # Check the adjacent left bucket
            if bucket_id - 1 in bucket and abs(num - bucket[bucket_id - 1]) <= valueDiff:
                return True
                
            # Check the adjacent right bucket
            if bucket_id + 1 in bucket and abs(num - bucket[bucket_id + 1]) <= valueDiff:
                return True
                
            # Place current number into its bucket
            bucket[bucket_id] = num
            
            # Remove the element that falls out of the indexDiff window
            if i >= indexDiff:
                old_num = nums[i - indexDiff]
                old_bucket_id = old_num // w
                del bucket[old_bucket_id]
                
       return False