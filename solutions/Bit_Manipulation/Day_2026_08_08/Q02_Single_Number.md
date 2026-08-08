# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single number. The input array will have a length of at least 1 but not more than 10000. The elements in the array will be between -10000 and 10000. For example, if the input array is [2, 2, 1], the output should be 1, and if the input array is [4, 1, 2, 1, 2], the output should be 4.

## Approach
The algorithm uses the XOR operation to find the single number. The XOR operation has the property that a ^ a = 0 and a ^ 0 = a. So, when we XOR all the numbers in the array, the numbers that appear twice will cancel out, and the single number will remain.

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
        // XOR all the numbers in the array
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
- The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, which makes it useful for this problem.
- The time complexity of the solution is O(n), where n is the length of the input array, and the space complexity is O(1), which means the space required does not change with the size of the input array.