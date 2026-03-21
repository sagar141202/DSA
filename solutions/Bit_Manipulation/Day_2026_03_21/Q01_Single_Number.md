# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single number. The integer could be negative and the array is not sorted. The array can contain duplicate values and the single number can be at any position in the array. For example, if the input array is [2, 2, 1], the output should be 1 because 1 is the only number that appears once. If the input array is [4, 1, 2, 1, 2], the output should be 4 because 4 is the only number that appears once.

## Approach
The solution uses bit manipulation, specifically the XOR operation, to find the single number. The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, so when we XOR all numbers in the array, the numbers that appear twice will cancel out and the single number will remain.

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
        // XOR all numbers in the array
        for (int num : nums) {
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
- The XOR operation can be used to find the single number in an array where every element appears twice except for one.
- The time complexity of the solution is O(n) where n is the number of elements in the array.
- The space complexity of the solution is O(1) because we only use a constant amount of space to store the result.