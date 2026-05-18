# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single number. The integer could be negative, and the array will not be empty. The solution should have a linear time complexity, and the space complexity should be constant. For example, if the input array is [2, 2, 1], the function should return 1, and if the input array is [4, 1, 2, 1, 2], the function should return 4.

## Approach
The approach to solve this problem is to use the XOR operation, which has the property that a ^ a = 0 and a ^ 0 = a. We can iterate over the array and XOR all the elements. The elements that appear twice will cancel each other out, and the single number will remain.

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
        // XOR all the elements in the array
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
- The XOR operation can be used to find the single number in an array where every element appears twice except for one.
- The XOR operation has a time complexity of O(n) and a space complexity of O(1), making it an efficient solution for this problem.
- This solution works because the XOR operation has the property that a ^ a = 0 and a ^ 0 = a, which means that the elements that appear twice will cancel each other out, and the single number will remain.