# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, sort the array in a way that all elements at even indices are in ascending order and all elements at odd indices are in descending order. The first element should be the smallest, the second element should be the largest of the remaining elements, the third element should be the second smallest of the remaining elements, and so on. For example, if the input array is `[1, 5, 1, 1, 6, 4]`, one possible output is `[1, 6, 1, 5, 1, 4]`.

## Approach
To solve this problem, we can first sort the array in ascending order. Then, we can create a new array where the elements at even indices are taken from the start of the sorted array and the elements at odd indices are taken from the end of the sorted array.

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
        // Create a copy of the input array and sort it in ascending order
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        
        // Initialize two pointers, one at the start and one at the end of the sorted array
        int small = 0, large = nums.size() - 1;
        
        // Iterate over the input array and fill it with the sorted elements
        for (int i = 0; i < nums.size(); i++) {
            // If the index is even, take the next smallest element
            if (i % 2 == 0) {
                nums[i] = sortedNums[small++];
            }
            // If the index is odd, take the next largest element
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
- The problem requires a custom sorting order, where elements at even indices are in ascending order and elements at odd indices are in descending order.
- We can solve this problem by first sorting the array in ascending order and then rearranging the elements to meet the custom sorting order.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) for the auxiliary array.