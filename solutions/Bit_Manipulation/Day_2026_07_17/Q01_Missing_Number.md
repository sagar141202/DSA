# Missing Number
## Problem Statement
Given an array of integers from 0 to n, where n is the length of the array, find the missing number in the array. The array is guaranteed to have one and only one missing number. The array may contain duplicates. The missing number is in the range [0, n]. For example, given the array [0, 1, 2, 4], the missing number is 3. Given the array [0, 2, 2, 3], the missing number is 1.

## Approach
The approach is to use bitwise XOR operation to find the missing number. The XOR of all numbers from 0 to n and the XOR of all numbers in the array will give the missing number. This is because XOR of a number with itself is 0 and XOR of a number with 0 is the number itself.

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
        int missing = n;
        for (int i = 0; i < n; i++) {
            // XOR of all numbers from 0 to n and all numbers in the array
            missing ^= i;
            missing ^= nums[i];
        }
        return missing;
    }
};
```

## Test Cases
```
Input: [0, 1, 2, 4]
Output: 3
Input: [0, 2, 2, 3]
Output: 1
```

## Key Takeaways
- The XOR operation can be used to find the missing number in an array.
- The XOR operation has a time complexity of O(n) and a space complexity of O(1).
- The XOR operation can handle duplicates in the array.