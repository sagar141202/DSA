# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single number. The integer could be negative, and the array will have at least one element but not more than 1000 elements. For example, if the input is [2,2,1], the output should be 1, and if the input is [4,1,2,1,2], the output should be 4.

## Approach
The algorithm uses bit manipulation to find the single number. It initializes a variable to 0 and XORs it with every number in the array. Since XOR of a number with itself is 0 and XOR of a number with 0 is the number itself, all numbers that appear twice will cancel out, leaving the single number.

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
- The XOR operation has a property that `a ^ a = 0` and `a ^ 0 = a`, which makes it suitable for finding the single number in the array.
- This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.