# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The integer can be negative and the array is not sorted. The constraint is that the array has at least one element and at most 3 * 10^4 elements. For example, if the input array is [2, 2, 1], the output should be 1 because 1 appears only once. If the input array is [4, 1, 2, 1, 2], the output should be 4 because 4 appears only once.

## Approach
The approach is to use the XOR operation, which has the property that a ^ a = 0 and a ^ 0 = a. So, if we XOR all the numbers in the array, the numbers that appear twice will cancel out, and the number that appears once will remain. This is because XOR is commutative and associative.

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
- The time complexity of this solution is O(n) and the space complexity is O(1), making it efficient for large inputs.