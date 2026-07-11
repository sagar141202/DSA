# Missing Number
## Problem Statement
The problem "Missing Number" involves finding a missing number in a sequence of numbers from 0 to n. The sequence is represented as an array of integers, and one number is missing. The task is to find the missing number. The array has n numbers, and the numbers range from 0 to n. The missing number can be any number between 0 and n. For example, if the input array is [0, 1, 3], the missing number is 2. The array has distinct numbers, and there is only one missing number.

## Approach
The approach to solve this problem is to use bitwise XOR operation to find the missing number. The XOR operation has a property that a ^ a = 0 and a ^ 0 = a. We can XOR all numbers from 0 to n and all numbers in the array, and the result will be the missing number.

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
        int result = n;
        for (int i = 0; i < n; i++) {
            // XOR all numbers from 0 to n
            result = result ^ i;
            // XOR all numbers in the array
            result = result ^ nums[i];
        }
        return result;
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
- The XOR operation can be used to find the missing number in a sequence.
- The XOR operation has a property that a ^ a = 0 and a ^ 0 = a, which makes it useful for this problem.
- The time complexity of the solution is O(n), where n is the size of the input array.