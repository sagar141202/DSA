# Missing Number

## Problem Statement
Given an array of integers from 0 to n, where n is the length of the array, find the missing number in the array. The array contains all integers from 0 to n except one. For example, given the array [0, 1, 3], the missing number is 2. The array has a length of 3, but it only contains three numbers: 0, 1, and 3. The number 2 is missing.

## Approach
We can solve this problem using bitwise XOR operation. The XOR of all numbers from 0 to n and the XOR of all numbers in the array will give us the missing number. This is because XOR of all numbers from 0 to n will have all bits set, and XOR of all numbers in the array will have all bits set except for the missing number.

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
        int xor_array = 0;
        
        // Calculate XOR of all numbers from 0 to n
        for (int i = 0; i <= n; i++) {
            xor_all ^= i;
        }
        
        // Calculate XOR of all numbers in the array
        for (int num : nums) {
            xor_array ^= num;
        }
        
        // The missing number is the XOR of the two
        return xor_all ^ xor_array;
    }
};
```

## Test Cases
```
Input: [0, 1, 3]
Output: 2
Input: [4, 0, 3, 1]
Output: 2
```

## Key Takeaways
- The XOR operation has a property that `a ^ a = 0` and `a ^ 0 = a`, which makes it useful for finding the missing number.
- The XOR operation can be used to find the missing number in an array of integers from 0 to n.
- The time complexity of this solution is O(n) and the space complexity is O(1), making it efficient for large inputs.