# Missing Number

## Problem Statement
Given an array of integers from 1 to n, where one number is missing, find the missing number. The array is of size n-1 and contains distinct integers in the range [1, n]. The integers are not sorted. For example, if the input array is [1, 2, 4], the output should be 3.

## Approach
The approach to solve this problem is to use the XOR operation, which has a property that a ^ a = 0 and a ^ 0 = a. We can XOR all numbers from 1 to n and then XOR all numbers in the array. The result will be the missing number.

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
        int xorAll = 0;
        // XOR all numbers from 1 to n
        for (int i = 1; i <= n + 1; i++) {
            xorAll ^= i;
        }
        // XOR all numbers in the array
        for (int num : nums) {
            xorAll ^= num;
        }
        return xorAll;
    }
};
```

## Test Cases
```
Input: [1, 2, 4]
Output: 3
Input: [3, 0, 1]
Output: 2
```

## Key Takeaways
- The XOR operation can be used to find the missing number in an array.
- The XOR operation has a property that a ^ a = 0 and a ^ 0 = a, which makes it useful for this problem.
- The time complexity of this solution is O(n), where n is the size of the array.