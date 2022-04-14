from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    nums.sort()
    for i, _ in enumerate(nums):
        if i+1<len(nums):
            if nums[i]==nums[i+1]:
                return True
    return False

if __name__ == "__main__":
    nums1 = [1,2,3,1]
    nums2 = [1,2,3,4]
    nums3 = [1,1,1,3,3,4,3,2,4,2]
    print(containsDuplicate(nums1))
    print(containsDuplicate(nums2))
    print(containsDuplicate(nums3))