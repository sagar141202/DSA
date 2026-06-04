# Sum of Two Integers

## Problem Statement
The problem requires finding the sum of two integers without using the arithmetic operators + and -. The function should take two integers as input and return their sum. The integers can be positive, negative, or zero. For example, given the integers 1 and 2, the function should return 3. Given the integers -1 and 1, the function should return 0.

## Approach
The approach to solve this problem involves using bitwise operators to perform the addition. We can use the XOR operator (^) to find the sum of two bits and the AND operator (&) to find the carry. We will then shift the carry to the left and repeat the process until there is no carry left.

## Complexity
- Time: O(log max(a, b))
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
        
        // Calculate the sum of a and b using XOR
        int sum = a ^ b;
        
        // Calculate the carry using AND and left shift
        int carry = (a & b) << 1;
        
        // Recursive call to add the carry to the sum
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
- Bitwise operators can be used to perform arithmetic operations without using the traditional arithmetic operators.
- The XOR operator (^) can be used to find the sum of two bits, and the AND operator (&) can be used to find the carry.
- The recursive approach can be used to add the carry to the sum until there is no carry left.