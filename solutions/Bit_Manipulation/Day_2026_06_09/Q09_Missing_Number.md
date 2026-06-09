# Missing Number

## Problem Statement
Given an array of integers from 1 to n, where one number is missing, find the missing number. The array has n-1 elements, and all elements are unique. The missing number can be any integer between 1 and n (inclusive). For example, if the input array is [1, 2, 4], the missing number is 3. If the input array is [1, 3, 4], the missing number is 2.

## Approach
We can use the XOR operation to find the missing number. The XOR of all numbers from 1 to n and the XOR of all numbers in the array will give us the missing number. This works because XOR of a number with itself is 0, and XOR of a number with 0 is the number itself.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int xor_all = 0;
        // XOR of all numbers from 1 to n
        for (int i = 1; i <= n; i++) {
            xor_all ^= i;
        }
        // XOR of all numbers in the array
        for (int num : nums) {
            xor_all ^= num;
        }
        return xor_all;
    }
};
```

## Test Cases
```
Input: [1, 2, 4]
Output: 3
Input: [1, 3, 4]
Output: 2
Input: [0, 1]
Output: 2
```

## Key Takeaways
- The XOR operation has a property that `a ^ a = 0` and `a ^ 0 = a`, which makes it useful for finding the missing number.
- The time complexity is O(n) because we need to iterate over all numbers from 1 to n and all numbers in the array.
- The space complexity is O(1) because we only use a constant amount of space to store the XOR result.