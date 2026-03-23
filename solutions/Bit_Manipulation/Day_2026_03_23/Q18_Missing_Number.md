# Missing Number

## Problem Statement
Given an array of integers from 1 to n, where one number is missing, find the missing number. The array is of size n-1, and all numbers are unique. For example, if the input array is [1, 2, 4], the missing number is 3. The array does not contain any duplicates, and all numbers are within the range of 1 to n.

## Approach
The approach to solve this problem is to use bitwise XOR operation. We can XOR all numbers from 1 to n and then XOR all numbers in the array. The result will be the missing number. This works because XOR of a number with itself is 0, and XOR of 0 with any number is the number itself.

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
        return xor_all;
    }
};
```

## Test Cases
```
Input: [1, 2, 4]
Output: 3
Input: [3, 0, 1]
Output: 2
```

## Key Takeaways
- The XOR operation can be used to find the missing number in an array.
- The time complexity of this solution is O(n), where n is the size of the array.
- The space complexity of this solution is O(1), as it only uses a constant amount of space.