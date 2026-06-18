# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n, find the XOR of all numbers in this range. The range is inclusive, meaning it includes both 0 and n. For example, if n = 3, the XOR of all numbers in the range would be 0 ^ 1 ^ 2 ^ 3 = 4, but if n = 4, the XOR would be 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4, because 4 is not included in the first case, but included in the second. The input n will be a non-negative integer.

## Approach
The approach to solve this problem involves recognizing patterns in the XOR operation for consecutive numbers. Specifically, for every 4 consecutive numbers (0, 1, 2, 3), their XOR is 0. Thus, the problem can be simplified by finding the remainder when n is divided by 4, which determines the last number in the sequence that needs to be XORed.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int xorOperation(int n) {
        // If n is a multiple of 4, the XOR is 0 because each set of 4 numbers has an XOR of 0
        if (n % 4 == 0) return n;
        // If n is 1 more than a multiple of 4, the XOR is n because n is the last number in the sequence
        else if (n % 4 == 1) return 1;
        // If n is 2 more than a multiple of 4, the XOR is n + 1 because the last two numbers are n - 1 and n
        else if (n % 4 == 2) return n + 1;
        // If n is 3 more than a multiple of 4, the XOR is 0 because n - 2, n - 1, and n will have an XOR of 0
        else return 0;
    }
};

int main() {
    Solution solution;
    cout << solution.xorOperation(3) << endl;  // Output: 4
    cout << solution.xorOperation(4) << endl;  // Output: 4
    return 0;
}
```

## Test Cases
```
Input: n = 3
Output: 4
Input: n = 4
Output: 4
Input: n = 5
Output: 1
```

## Key Takeaways
- The XOR operation has a cyclic pattern for consecutive numbers, specifically every 4 numbers have an XOR of 0.
- The solution leverages this pattern to simplify the calculation based on the remainder when n is divided by 4.