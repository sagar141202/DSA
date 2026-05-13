# Sum of Two Integers

## Problem Statement
Given two integers a and b, find the sum of the two integers without using the + operator. The integers can be positive, negative, or zero. The sum should be calculated using bitwise operations. For example, if a = 1 and b = 2, the function should return 3.

## Approach
We will use bitwise operators to add the two integers. The XOR operator (^) will be used to calculate the sum of a and b without considering the carry. The AND operator (&) will be used to calculate the carry. We will then shift the carry to the left and add it to the sum until there is no carry left.

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
        
        // Calculate the sum of a and b without considering the carry
        int sum = a ^ b;
        
        // Calculate the carry
        int carry = (a & b) << 1;
        
        // Recursively add the carry to the sum
        return getSum(sum, carry);
    }
};

int main() {
    Solution solution;
    int a = 1;
    int b = 2;
    cout << "Sum: " << solution.getSum(a, b) << endl;
    return 0;
}
```

## Test Cases
```
Input: a = 1, b = 2
Output: 3
Input: a = -1, b = 2
Output: 1
Input: a = 0, b = 0
Output: 0
```

## Key Takeaways
- We can use bitwise operators to add two integers without using the + operator.
- The XOR operator (^) can be used to calculate the sum of two integers without considering the carry.
- The AND operator (&) can be used to calculate the carry.