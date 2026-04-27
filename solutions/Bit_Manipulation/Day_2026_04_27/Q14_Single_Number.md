# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The input array will not be empty and will contain at least one element. The array can contain duplicate values, but every value except one will appear an even number of times. For example, if the input array is [2,2,1], the single number is 1 because it appears only once, while the number 2 appears twice.

## Approach
The solution uses bit manipulation to find the single number. The XOR operation is used, which returns 1 if the two bits are different, and 0 if they are the same. By XORing all numbers in the array, the numbers that appear twice will cancel each other out, leaving only the single number.

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
Input: [2,2,1]
Output: 1
Input: [4,1,2,1,2]
Output: 4
```

## Key Takeaways
- The XOR operation can be used to find the single number in an array where every element appears twice except for one.
- The XOR operation has a property that a ^ a = 0 and a ^ 0 = a, which makes it useful for this problem.
- The time complexity of this solution is O(n) because we need to iterate over all elements in the array, and the space complexity is O(1) because we only use a constant amount of space.