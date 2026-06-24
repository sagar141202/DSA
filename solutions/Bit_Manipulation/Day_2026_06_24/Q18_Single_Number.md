# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The input array can contain duplicate values and the single number can be anywhere in the array. For example, given the array [2, 2, 1], the function should return 1, because 1 appears only once in the array. Similarly, given the array [4, 1, 2, 1, 2], the function should return 4, because 4 appears only once in the array. The array will not be empty and will contain only integers.

## Approach
The algorithm uses bit manipulation to find the single number. It initializes a variable to 0 and then XORs it with every number in the array. Since XOR of a number with itself is 0 and XOR of 0 with any number is the number itself, the single number will be left after all operations.

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
        // Initialize result to 0
        int result = 0;
        // XOR result with every number in the array
        for (int num : nums) {
            result ^= num;
        }
        // Return the single number
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
- The XOR operation has the property that `a ^ a = 0` and `a ^ 0 = a`, which makes it suitable for finding the single number in the array.
- The algorithm has a time complexity of O(n) because it needs to iterate over the entire array, and a space complexity of O(1) because it only uses a constant amount of space.