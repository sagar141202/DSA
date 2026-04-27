# Sum of Two Integers

## Problem Statement
The problem requires finding the sum of two integers without using the arithmetic operators + and -. The integers can be positive, negative, or zero. The solution should handle overflow cases. For example, given two integers a = 1 and b = 2, the output should be 3. If a = -2 and b = 3, the output should be 1.

## Approach
The approach involves using bitwise operators to achieve the addition of two integers. We can use the XOR operator (^) to add two numbers without considering the carry, and the AND operator (&) along with left shift (<<) to calculate the carry. Then, we can recursively add the carry to the result until there is no carry left.

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
        // If b is 0, return a (base case)
        if (b == 0) return a;
        
        // Calculate the sum without considering the carry using XOR
        int sum = a ^ b;
        
        // Calculate the carry using AND and left shift
        int carry = (a & b) << 1;
        
        // Recursively add the carry to the sum
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
- Use bitwise operators to perform arithmetic operations without using + and -.
- The XOR operator (^) can be used to add two numbers without considering the carry.
- The AND operator (&) along with left shift (<<) can be used to calculate the carry.