# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The integer could appear only once or more than twice but one number will always appear only once. For example, in the array [2,2,1], 1 is the single number. In the array [4,1,2,1,2], 4 is the single number. You can only use constant space and the solution should run in linear time.

## Approach
The algorithm uses bit manipulation to find the single number. It initializes a variable to 0 and XORs it with every number in the array. Since XOR of a number with itself is 0 and XOR of a number with 0 is the number itself, all numbers that appear twice will cancel out each other, leaving the single number.

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
- The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, which makes it useful for finding the single number in the array.
- The solution runs in linear time and uses constant space, making it efficient for large inputs.