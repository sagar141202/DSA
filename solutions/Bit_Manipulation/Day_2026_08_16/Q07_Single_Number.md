# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single number. The integer could be negative, and the array will not be empty. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array. For example, given the array `[2, 2, 1]`, the function should return `1`, and given the array `[-2, -2, 1, 1, -3, -4, -4]`, the function should return `-3`.

## Approach
The approach to solve this problem is to use bit manipulation, specifically the XOR operation. The XOR operation has the property that `a ^ a = 0` and `a ^ 0 = a`. This means that if we XOR all the elements in the array, the elements that appear twice will cancel each other out, leaving only the single number.

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
        // Initialize the result to 0
        int result = 0;
        
        // XOR all the elements in the array
        for (int num : nums) {
            // The XOR operation will cancel out the elements that appear twice
            result ^= num;
        }
        
        // The result will be the single number
        return result;
    }
};
```

## Test Cases
```
Input: [2, 2, 1]
Output: 1
Input: [-2, -2, 1, 1, -3, -4, -4]
Output: -3
```

## Key Takeaways
- The XOR operation can be used to find the single number in an array where every element appears twice except for one.
- The time complexity of the solution is O(n) and the space complexity is O(1), making it efficient for large inputs.
- The solution works for both positive and negative integers.