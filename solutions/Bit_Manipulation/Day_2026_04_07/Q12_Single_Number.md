# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The integer could appear only once or more than once but the other numbers appear exactly twice. The array is not empty and only one number appears only once. For example, if the input array is [2, 2, 1], the single number is 1. If the input array is [4, 1, 2, 1, 2], the single number is 4.

## Approach
The solution uses bitwise XOR operation to find the single number. XOR of all elements in the array will give the single number because XOR of a number with itself is 0 and XOR of 0 with any number is the number itself.

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
        // XOR of all elements in the array
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
- The XOR operation has the property that `a ^ a = 0` and `a ^ 0 = a`, which makes it useful for finding the single number in the array.
- This solution has a time complexity of O(n) because it needs to iterate over the entire array, and a space complexity of O(1) because it only uses a constant amount of space to store the result.