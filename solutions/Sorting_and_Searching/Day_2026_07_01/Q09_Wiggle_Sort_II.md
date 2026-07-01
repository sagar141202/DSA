# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, sort it in-place such that the smaller number will be on the even index and the larger number will be on the odd index. The array should be sorted in a way that the first element is the smallest, the second element is the largest, the third element is the second smallest, the fourth element is the second largest, and so on. If there are multiple possible solutions, return any one of them. For example, if the input array is `[1, 5, 1, 1, 6, 4]`, one possible output is `[1, 6, 1, 5, 1, 4]`.

## Approach
The approach is to first sort the array in ascending order, then create a new array where elements are placed in a zigzag pattern. This is achieved by using two pointers, one starting from the beginning and one from the end of the sorted array.

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
        int n = nums.size();
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        
        int small = 0, large = n - 1;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                nums[i] = sortedNums[small++];
            } else {
                nums[i] = sortedNums[large--];
            }
        }
    }
};
```

## Test Cases
```
Input: [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4]
```

## Key Takeaways
- First, sort the input array in ascending order.
- Create a new array where elements are placed in a zigzag pattern.
- Use two pointers to keep track of the smallest and largest elements in the sorted array.