# Count of Smaller Numbers After Self

## Problem Statement
Given an array of integers, return an array where each element at index i represents the number of smaller elements to the right of i in the given array. The constraints are 1 <= arr.length <= 10^5 and 1 <= arr[i] <= 10^5. For example, if the input array is [5, 2, 6, 1], the output should be [2, 1, 1, 0] because to the right of 5 there are 2 smaller numbers (2 and 1), to the right of 2 there is 1 smaller number (1), to the right of 6 there is 1 smaller number (1), and to the right of 1 there are no smaller numbers.

## Approach
We can use a Binary Indexed Tree (BIT) to solve this problem efficiently. The idea is to iterate over the array from right to left and for each element, count the number of smaller elements to its right using the BIT. We update the BIT after processing each element.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> result(nums.size());
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        for (int i = nums.size() - 1; i >= 0; --i) {
            int index = lower_bound(sortedNums.begin(), sortedNums.end(), nums[i]) - sortedNums.begin();
            result[i] = index;
            sortedNums.erase(sortedNums.begin() + index);
        }
        return result;
    }
};
```

## Test Cases
```
Input: [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Input: [1, 2, 3, 4, 5]
Output: [0, 0, 0, 0, 0]
```

## Key Takeaways
- We can use a Binary Indexed Tree (BIT) or a similar data structure to efficiently count the number of smaller elements to the right of each element in the array.
- The problem can be solved by iterating over the array from right to left and updating the BIT after processing each element.
- The time complexity of the solution is O(n log n) due to the sorting and binary search operations.