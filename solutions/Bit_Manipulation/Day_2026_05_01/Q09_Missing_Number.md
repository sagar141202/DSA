# Missing Number

## Problem Statement
Given an array of integers from 1 to n, find the missing number in the array. The array is guaranteed to have a missing number, and all other numbers appear exactly once. The array is 0-indexed and can contain duplicate zeros. For example, given the array [0, 1, 3], the missing number is 2. The array can be unsorted.

## Approach
We can use the XOR operation to find the missing number, as XOR of all numbers from 1 to n and all numbers in the array will give us the missing number. This approach works because XOR of a number with itself is 0, and XOR of a number with 0 is the number itself.

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
        // XOR all numbers from 1 to n
        for (int i = 1; i <= n; i++) {
            xor_all ^= i;
        }
        // XOR all numbers in the array
        for (int num : nums) {
            xor_all ^= num;
        }
        // The result is the missing number
        return xor_all;
    }
};
```

## Test Cases
```
Input: [3,0,1]
Output: 2
Input: [0,1]
Output: 2
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
```

## Key Takeaways
- The XOR operation can be used to find the missing number in an array.
- The XOR operation has a time complexity of O(n) and a space complexity of O(1), making it efficient for large arrays.
- This approach works because XOR of a number with itself is 0, and XOR of a number with 0 is the number itself.