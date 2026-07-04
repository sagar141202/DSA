# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The integer can be negative and the array will not be empty. The constraint is that the solution should have a linear runtime complexity and use a constant amount of extra space. For example, given the array [2,2,1], the function should return 1, and given the array [4,1,2,1,2], the function should return 4.

## Approach
The algorithm uses bitwise XOR operation to find the single number. The XOR operation has a property that a ^ a = 0 and a ^ 0 = a. Therefore, when we XOR all the numbers in the array, the numbers that appear twice will cancel out and the single number will remain.

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
        // XOR all the numbers in the array
        for (int num : nums) {
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
- The XOR operation can be used to find the single number in an array where every element appears twice except for one.
- The XOR operation has a property that a ^ a = 0 and a ^ 0 = a, which makes it suitable for this problem.
- The solution has a linear runtime complexity and uses a constant amount of extra space, making it efficient.