# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The input array will not be empty, and all elements will be between 1 and 1000. The array can contain duplicate values, but one value will appear only once. For example, given the array [2, 2, 1], the function should return 1, because 1 appears only once in the array. Another example is [4, 1, 2, 1, 2], the function should return 4.

## Approach
The algorithm uses bit manipulation to find the single number. It iterates over the array and uses the XOR operation to find the number that appears only once. The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, so all numbers that appear twice will cancel each other out.

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
        // Iterate over the array and use XOR operation to find the single number
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
- The XOR operation can be used to find the single number in an array where all other numbers appear twice.
- The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, which makes it useful for this problem.
- The time complexity of this solution is O(n) and the space complexity is O(1), making it efficient for large inputs.