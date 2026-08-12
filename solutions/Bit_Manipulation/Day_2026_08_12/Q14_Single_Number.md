# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The input array will not be empty, and the single element will always exist. For example, given the array `[2, 2, 1]`, the single number is `1`. Given the array `[4, 1, 2, 1, 2]`, the single number is `4`.

## Approach
The algorithm uses bitwise XOR operation to find the single number. The XOR of a number with itself is 0, and the XOR of a number with 0 is the number itself. Therefore, all numbers that appear twice will cancel out, leaving the single number.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        for (int num : nums) {
            // XOR operation to find the single number
            result ^= num;
        }
        return result;
    }
};
```

## Test Cases
```
Input: [2, 2, 1]
Output: 1
Input: [4, 1, 2, 1, 2]
Output: 4
```

## Key Takeaways
- The XOR operation has a property that `a ^ a = 0` and `a ^ 0 = a`, which is useful in finding the single number.
- The algorithm has a linear time complexity because it only needs to iterate through the array once.
- The space complexity is constant because it only uses a single variable to store the result.