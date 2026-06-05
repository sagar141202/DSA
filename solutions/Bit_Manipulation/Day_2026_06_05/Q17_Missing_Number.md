# Missing Number

## Problem Statement
Given an array of integers from 0 to n, where n is the length of the array, find the missing number in the array. The array is guaranteed to have exactly one missing number. For example, if the input array is [0, 1, 2, 4], the output should be 3. The array can contain duplicates and the missing number can be anywhere in the range.

## Approach
The approach to solve this problem is to use bitwise XOR operation to find the missing number. We XOR all the numbers in the array with all the numbers from 0 to n, and the result will be the missing number. This works because XOR of a number with itself is 0, and XOR of a number with 0 is the number itself.

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
            res = res ^ i ^ nums[i];
        }
        return res;
    }
};
```

## Test Cases
```
Input: [0, 1, 2, 4]
Output: 3
Input: [0, 1, 3]
Output: 2
```

## Key Takeaways
- The XOR operation has a property that a ^ a = 0 and a ^ 0 = a, which makes it suitable for finding the missing number.
- The time complexity of this solution is O(n) because we are iterating over the array once.
- The space complexity of this solution is O(1) because we are not using any extra space that scales with the input size.