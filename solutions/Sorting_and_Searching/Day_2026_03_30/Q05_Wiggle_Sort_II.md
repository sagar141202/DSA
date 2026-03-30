# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, sort it in-place such that all even-indexed elements are less than all odd-indexed elements. The output should be in a specific order, where the first element is the smallest, the second element is the next smallest, and so on, but with the constraint that even-indexed elements are less than odd-indexed elements. For example, if the input is `[1, 5, 1, 1, 6, 4]`, the output should be `[1, 3, 1, 4, 1, 6]`. The length of the input array is in the range `[1, 5000]`, and all elements are in the range `[-5000, 5000]`.

## Approach
The algorithm sorts the array first and then rearranges the elements to satisfy the wiggle sort condition. It uses a temporary array to store the sorted elements and then places them at the correct positions in the original array. The key idea is to place the smallest elements at the even indices and the largest elements at the odd indices.

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
        vector<int> temp = nums;
        sort(temp.begin(), temp.end());
        
        int small = 0, large = n - 1;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                nums[i] = temp[small++];
            } else {
                nums[i] = temp[large--];
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
- First, sort the input array to get the elements in ascending order.
- Then, use two pointers, one at the start and one at the end of the sorted array, to place the elements at the correct positions in the original array.
- The even-indexed elements should be less than the odd-indexed elements, so place the smallest elements at the even indices and the largest elements at the odd indices.