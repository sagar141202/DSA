# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The integer can be negative, and the input array is not sorted. The constraints are: 1 <= nums.length <= 3 * 10^4, and -3 * 10^4 <= nums[i] <= 3 * 10^4 for each integer i in the array nums. For example, if the input is [2, 2, 1], the output should be 1, and if the input is [4, 1, 2, 1, 2], the output should be 4.

## Approach
The algorithm uses bit manipulation, specifically the XOR operation, to find the single number. The XOR operation has a property where a ^ a = 0 and a ^ 0 = a. So, when we XOR all numbers in the array, the numbers that appear twice will cancel out, and the single number will remain.

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
        // Initialize result as 0
        int result = 0;
        
        // XOR all numbers in the array
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
- The XOR operation can be used to find the single number in an array where every element appears twice except for one.
- The time complexity of the solution is O(n), where n is the number of elements in the array, because we are scanning the array once.
- The space complexity of the solution is O(1), which means the space required does not change with the size of the input array, making it very efficient.