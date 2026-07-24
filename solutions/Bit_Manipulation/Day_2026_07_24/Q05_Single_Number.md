# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The input array will have at least one element, and all elements will be in the range of 32-bit signed integers. For example, if the input array is [2, 2, 1], the function should return 1, and if the input array is [4, 1, 2, 1, 2], the function should return 4.

## Approach
The solution utilizes the XOR operation, which returns 1 if the two bits are different, and 0 if they are the same. By XORing all elements in the array, the elements that appear twice will cancel each other out, leaving the single number. This approach works because XOR is commutative, associative, and has an identity element of 0.

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
        // XOR all elements in the array
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
- This approach has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.
- The solution works because XOR is commutative, associative, and has an identity element of 0, allowing it to cancel out the elements that appear twice.