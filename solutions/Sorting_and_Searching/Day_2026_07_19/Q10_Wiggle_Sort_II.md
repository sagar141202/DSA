# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, sort the array in a way that all elements at even indices are in ascending order, and all elements at odd indices are in descending order. The first element should be the smallest, and the second element should be the largest, the third element should be the second smallest, and so on. If the length of the array is odd, the last element should be the remaining largest element. For example, if the input array is `[1, 5, 1, 1, 6, 4]`, the output array should be `[1, 6, 1, 5, 1, 4]`. The array should be sorted in-place.

## Approach
The approach to solve this problem is to first sort the array in ascending order, and then rearrange the elements to satisfy the wiggle sort condition. This can be achieved by using two pointers, one at the beginning and one at the end of the sorted array, and swapping the elements at even and odd indices.

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
        
        int small = 0, large = nums.size() - 1;
        for (int i = 0; i < nums.size(); i++) {
            // If the index is even, assign the smallest remaining element
            if (i % 2 == 0) {
                nums[i] = sortedNums[small++];
            } 
            // If the index is odd, assign the largest remaining element
            else {
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
Input: [1, 3, 2, 2, 3, 1]
Output: [1, 3, 1, 3, 2, 2]
```

## Key Takeaways
- First, sort the input array in ascending order to get the smallest and largest elements.
- Use two pointers, one at the beginning and one at the end of the sorted array, to assign the elements to the input array.
- The wiggle sort condition can be satisfied by alternating between the smallest and largest remaining elements.