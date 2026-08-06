# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. You may assume the length of `nums` is at least 2. The solution should be efficient and use a reasonable amount of extra space.

## Approach
The approach involves first sorting the array, then rearranging the elements to satisfy the wiggle sort condition. This can be achieved by iterating over the sorted array and swapping elements at even and odd indices.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        // Create a copy of the input array and sort it
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        
        // Initialize two pointers, one at the beginning and one at the end of the sorted array
        int small = 0, large = nums.size() - 1;
        
        // Iterate over the input array and rearrange the elements
        for (int i = 0; i < nums.size(); i++) {
            // If the index is even, assign the smaller element
            if (i % 2 == 0) {
                nums[i] = sortedNums[small++];
            }
            // If the index is odd, assign the larger element
            else {
                nums[i] = sortedNums[large--];
            }
        }
    }
};

// Example usage
int main() {
    Solution solution;
    vector<int> nums = {1, 5, 1, 1, 6, 4};
    solution.wiggleSort(nums);
    for (int num : nums) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4]
```

## Key Takeaways
- The wiggle sort problem requires rearranging the elements of an array to satisfy a specific condition.
- Sorting the array first and then rearranging the elements is an efficient approach to solve this problem.
- Using two pointers, one at the beginning and one at the end of the sorted array, helps to assign the smaller and larger elements to the correct positions in the input array.