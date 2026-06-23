# Missing Number

## Problem Statement
Given an array of integers from 0 to n, where n is the length of the array, find the missing number in the array. The array contains all integers from 0 to n, except one. For example, if the array is [0, 1, 3], the missing number is 2. The array may contain duplicates, but the missing number is unique.

## Approach
The approach to solve this problem is to use bitwise XOR operation. We XOR all the numbers in the array with all the numbers from 0 to n. The result will be the missing number.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int res = n;
        for (int i = 0; i < n; i++) {
            // XOR all the numbers in the array with all the numbers from 0 to n
            res = res ^ i ^ nums[i];
        }
        return res;
    }
};
```

## Test Cases
```
Input: [0, 1, 3]
Output: 2
Input: [4, 0, 3, 1]
Output: 2
```

## Key Takeaways
- The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, which makes it suitable for finding the missing number.
- The time complexity is O(n) because we need to iterate over the array once.
- The space complexity is O(1) because we only use a constant amount of space to store the result.