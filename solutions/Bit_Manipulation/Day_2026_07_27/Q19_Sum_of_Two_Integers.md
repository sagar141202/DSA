# Sum of Two Integers

## Problem Statement
The problem requires finding the sum of two integers without using the arithmetic operators + and -. The integers can be positive, negative, or zero. The solution should handle overflow cases. For example, given two integers a = 1 and b = 2, the function should return 3, which is the sum of a and b.

## Approach
The approach involves using bitwise operators to add the two integers. The XOR operator (^) is used to add the bits of the two numbers without considering the carry. The AND operator (&) is used to find the carry bits. The left shift operator (<<) is used to shift the carry bits to the left.

## Complexity
- Time: O(log(max(a, b)))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int getSum(int a, int b) {
        // If b is 0, return a
        if (b == 0) return a;
        
        // Calculate the sum without considering the carry
        int sum = a ^ b;
        
        // Calculate the carry
        int carry = (a & b) << 1;
        
        // Recursively call the function with the new sum and carry
        return getSum(sum, carry);
    }
};
```

## Test Cases
```
Input: a = 1, b = 2
Output: 3
Input: a = -2, b = 3
Output: 1
```

## Key Takeaways
- The bitwise XOR operator (^) is used to add the bits of two numbers without considering the carry.
- The bitwise AND operator (&) is used to find the carry bits.
- The left shift operator (<<) is used to shift the carry bits to the left.
- The recursive approach is used to handle the carry bits.