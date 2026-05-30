# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single number. The integer can be negative, and the array is not sorted. The input array will have at least one element, and all elements will be in the range [-2^31, 2^31 - 1]. For example, if the input array is [2, 2, 1], the function should return 1 because 1 appears only once in the array. If the input array is [4, 1, 2, 1, 2], the function should return 4 because 4 appears only once in the array.

## Approach
The algorithm uses bitwise XOR operation to find the single number. XOR of a number with itself is 0, and XOR of a number with 0 is the number itself. This property can be utilized to find the single number in the array. The XOR of all numbers in the array will give the single number.

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
- The XOR operation has a property that `a ^ a = 0` and `a ^ 0 = a`, which can be used to find the single number in the array.
- The time complexity of the solution is O(n) because we need to iterate over all elements in the array.
- The space complexity of the solution is O(1) because we only use a constant amount of space to store the result.