# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The input array will have at least one element, but not more than 10,000 elements. The elements will be in the range of 32-bit signed integers. For example, if the input array is [2, 2, 1], the function should return 1, because 1 appears only once in the array. If the input array is [4, 1, 2, 1, 2], the function should return 4, because 4 appears only once in the array.

## Approach
The algorithm uses bit manipulation to find the single number. It initializes a variable to 0 and then XORs it with every number in the array. The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, so all numbers that appear twice will cancel each other out, leaving only the single number.

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
- The XOR operation can be used to find the single number in an array where every other number appears twice.
- The algorithm has a time complexity of O(n) because it needs to iterate over the entire array.
- The algorithm has a space complexity of O(1) because it only uses a constant amount of space to store the result.