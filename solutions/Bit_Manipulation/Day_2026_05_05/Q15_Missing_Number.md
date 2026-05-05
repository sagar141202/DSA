# Missing Number

## Problem Statement
Given an array of integers from 0 to n, where n is the length of the array, find the missing number in the array. The array contains all integers from 0 to n, except one. For example, if the input array is [0, 1, 3], the missing number is 2. The input array will not contain duplicates, and all integers will be within the range of 0 to n.

## Approach
The algorithm uses bit manipulation to find the missing number. It calculates the XOR of all numbers from 0 to n and the XOR of all numbers in the array. The missing number is then the XOR of these two results.

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
            // XOR of all numbers from 0 to n
            result = result ^ i;
            // XOR of all numbers in the array
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
- Use XOR operation to find the missing number in an array.
- The XOR operation has the property that `a ^ a = 0` and `a ^ 0 = a`, which makes it suitable for finding the missing number.
- This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.