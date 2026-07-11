# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single number. The input array will have at least one element, but not more than 10^4 elements. Each element will be between -10^4 and 10^4. For example, given the array [2, 2, 1], the function should return 1, because 1 appears only once in the array. Given the array [4, 1, 2, 1, 2], the function should return 4, because 4 appears only once in the array.

## Approach
The algorithm uses bit manipulation to find the single number. It iterates over each element in the array and performs a bitwise XOR operation with the current result. Since XOR of a number with itself is 0 and XOR of a number with 0 is the number itself, all numbers that appear twice will cancel out, leaving the single number.

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
        // Initialize result as 0
        int result = 0;
        
        // Iterate over each element in the array
        for (int num : nums) {
            // Perform bitwise XOR operation with the current result
            result ^= num;
        }
        
        // Return the single number
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
- The XOR operation has the property that `a ^ a = 0` and `a ^ 0 = a`, which makes it suitable for finding the single number in the array.
- The algorithm has a time complexity of O(n) because it iterates over each element in the array once.
- The algorithm has a space complexity of O(1) because it uses a constant amount of space to store the result.