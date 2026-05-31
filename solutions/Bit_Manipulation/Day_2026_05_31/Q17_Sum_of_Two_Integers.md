# Sum of Two Integers

## Problem Statement
The problem requires finding the sum of two integers without using the arithmetic operators + and -. The function should take two integers as input and return their sum. The integers can be positive, negative, or zero. For example, given the integers 1 and 2, the function should return 3. Given the integers -1 and 1, the function should return 0.

## Approach
We can use bitwise operations to achieve this. The idea is to use the XOR operation to find the sum of two numbers without considering the carry, and then use the AND operation to find the carry. We then shift the carry to the left and repeat the process until there is no carry left.

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
        
        // Calculate the sum without considering the carry using XOR
        int sum = a ^ b;
        
        // Calculate the carry using AND and left shift
        int carry = (a & b) << 1;
        
        // Recursively call the function with the sum and carry
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
- We can use bitwise operations to solve arithmetic problems without using arithmetic operators.
- The XOR operation can be used to find the sum of two numbers without considering the carry.
- The AND operation can be used to find the carry, and left shift can be used to shift the carry to the left.