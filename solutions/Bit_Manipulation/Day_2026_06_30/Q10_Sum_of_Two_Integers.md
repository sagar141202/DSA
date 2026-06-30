# Sum of Two Integers

## Problem Statement
Given two integers a and b, find their sum without using the arithmetic operators + and -. The integers can be negative or positive, and the result should be within the range of 32-bit signed integers. For example, given a = 1 and b = 2, the function should return 3. Given a = -2 and b = 3, the function should return 1.

## Approach
The approach is to use bitwise operators to add the two integers. We can use the XOR operator (^) to add the bits of the two integers without considering the carry, and the AND operator (&) with left shift (<<) to consider the carry. We repeat this process until there is no carry left.

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
        // if b is 0, return a
        if (b == 0) return a;
        // calculate the sum without considering the carry
        int sum = a ^ b;
        // calculate the carry
        int carry = (a & b) << 1;
        // recursive call to add the carry
        return getSum(sum, carry);
    }
};

int main() {
    Solution solution;
    cout << solution.getSum(1, 2) << endl;  // Output: 3
    cout << solution.getSum(-2, 3) << endl;  // Output: 1
    return 0;
}
```

## Test Cases
```
Input: a = 1, b = 2
Output: 3
Input: a = -2, b = 3
Output: 1
```

## Key Takeaways
- Use bitwise operators to add two integers without using arithmetic operators + and -.
- The XOR operator (^) is used to add the bits of the two integers without considering the carry.
- The AND operator (&) with left shift (<<) is used to consider the carry.