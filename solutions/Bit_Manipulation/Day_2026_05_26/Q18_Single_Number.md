# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The input array will have at least one element, and all elements will be in the range of 32-bit signed integers. For example, given the array [2,2,1], the function should return 1, and given the array [4,1,2,1,2], the function should return 4.

## Approach
The algorithm uses bit manipulation, specifically the XOR operation, to find the single number. The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, so all numbers that appear twice will cancel each other out, leaving only the single number.

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
        // iterate over all elements in the array
        for (int num : nums) {
            // XOR the current number with the result
            result ^= num;
        }
        return result;
    }
};
```

## Test Cases
```
Input: [2,2,1]
Output: 1
Input: [4,1,2,1,2]
Output: 4
```

## Key Takeaways
- The XOR operation can be used to find the single number in an array where all other numbers appear twice.
- The XOR operation has a time complexity of O(1) and a space complexity of O(1), making it efficient for this problem.
- This solution assumes that the input array is non-empty and all elements are 32-bit signed integers.