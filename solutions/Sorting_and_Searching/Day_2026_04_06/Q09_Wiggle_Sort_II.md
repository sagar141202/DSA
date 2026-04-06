# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, sort it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. This is known as wiggle sorting. The length of the array will be at least 1, and the array may contain duplicates. For example, if the input is `[1, 5, 1, 1, 6, 4]`, one possible answer is `[1, 4, 1, 5, 1, 6]`.

## Approach
The approach to solve this problem involves first sorting the array in ascending order, then rearranging the elements to satisfy the wiggle sort condition. We can achieve this by placing the smallest element at the first position, the next smallest element at the third position, the next smallest element at the second position, and so on.

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
        // Create a copy of the array and sort it
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        
        int small = 0, large = nums.size() - 1;
        // Traverse the array and rearrange the elements
        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 0) {
                nums[i] = sortedNums[small++];
            } else {
                nums[i] = sortedNums[large--];
            }
        }
    }
};

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
Output: [1, 4, 1, 5, 1, 6]
```

## Key Takeaways
- First, sort the array in ascending order.
- Then, rearrange the elements to satisfy the wiggle sort condition by placing the smallest element at the first position, the next smallest element at the third position, and so on.
- The time complexity is O(n log n) due to the sorting operation, and the space complexity is O(n) for storing the sorted array.