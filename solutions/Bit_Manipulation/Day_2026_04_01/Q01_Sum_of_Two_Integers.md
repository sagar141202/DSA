# Sum of Two Integers

## Problem Statement
The problem requires finding the sum of two integers without using the arithmetic operators + and -. The function should take two integers as input and return their sum. The integers can be positive, negative, or zero. For example, given the integers 1 and 2, the function should return 3. Given the integers -1 and 1, the function should return 0.

## Approach
The approach is to use bitwise operators to add the two integers. The XOR operator (^) can be used to add the two integers without considering the carry. The AND operator (&) can be used to calculate the carry. The left shift operator (<<) can be used to shift the carry to the left.

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
        
        // Recursively call the function with the sum and the carry
        return getSum(sum, carry);
    }
};
```

## Test Cases
```
Input: a = 1, b = 2
Output: 3
Input: a = -1, b = 1
Output: 0
```

## Key Takeaways
- The XOR operator (^) can be used to add two integers without considering the carry.
- The AND operator (&) can be used to calculate the carry.
- The left shift operator (<<) can be used to shift the carry to the left, effectively multiplying it by 2.