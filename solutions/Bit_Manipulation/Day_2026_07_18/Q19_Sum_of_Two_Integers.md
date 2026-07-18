# Sum of Two Integers

## Problem Statement
The problem requires finding the sum of two integers without using the arithmetic operators + and -. The function should take two integers as input and return their sum. The integers can be positive, negative, or zero. For example, given the integers 3 and 5, the function should return 8.

## Approach
The approach is to use bitwise operations to add the two integers. This can be achieved by using the XOR operator (^) to add the numbers without considering the carry, and the AND operator (&) along with left shift (<<) to consider the carry.

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
        if (b == 0)
            return a;
        
        // Calculate the sum without considering the carry
        int sumWithoutCarry = a ^ b;
        
        // Calculate the carry
        int carry = (a & b) << 1;
        
        // Recursively call the function with the sum without carry and the carry
        return getSum(sumWithoutCarry, carry);
    }
};

int main() {
    Solution solution;
    int a = 3;
    int b = 5;
    cout << "Sum: " << solution.getSum(a, b) << endl;
    return 0;
}
```

## Test Cases
```
Input: a = 3, b = 5
Output: 8
Input: a = -2, b = 3
Output: 1
Input: a = 0, b = 0
Output: 0
```

## Key Takeaways
- Bitwise operations can be used to perform arithmetic operations without using the arithmetic operators.
- The XOR operator (^) can be used to add two numbers without considering the carry.
- The AND operator (&) along with left shift (<<) can be used to consider the carry.