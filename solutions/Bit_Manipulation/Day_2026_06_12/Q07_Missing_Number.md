# Missing Number

## Problem Statement
Given an array of integers from 0 to n, where n is the length of the array, find the missing number in the array. The missing number is the number that is not present in the array. The array contains all unique integers from 0 to n, except for one number which is missing. The problem can be solved using bit manipulation. For example, if the input array is [0, 1, 3], the output should be 2.

## Approach
The approach is to use bitwise XOR operation to find the missing number. We XOR all numbers from 0 to n and all numbers in the array, the result will be the missing number. This works because XOR of a number with itself is 0, and XOR of a number with 0 is the number itself.

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
            // XOR all numbers from 0 to n
            res ^= i;
            // XOR all numbers in the array
            res ^= nums[i];
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
- The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, which makes it useful for finding the missing number.
- The time complexity of the solution is O(n), where n is the length of the input array.
- The space complexity of the solution is O(1), which means the space required does not change with the size of the input array.