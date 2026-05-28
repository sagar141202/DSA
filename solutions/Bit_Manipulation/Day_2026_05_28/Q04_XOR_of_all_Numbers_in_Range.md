# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n (inclusive), find the XOR of all numbers in this range. The range is defined by a single integer n. For example, if n = 5, the range is [0, 1, 2, 3, 4, 5] and the XOR of all numbers in this range is 1 (0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 = 1). The input range is 0 <= n <= 10^6.

## Approach
The algorithm uses the properties of XOR operation to simplify the calculation. We can observe a pattern where the XOR of all numbers up to a certain point repeats every 4 numbers. This pattern can be used to calculate the XOR of all numbers in the range efficiently.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int xorOfAllNumbersInRange(int n) {
        // The pattern repeats every 4 numbers: 0 ^ 1 ^ 2 ^ 3 = 0, 4 ^ 5 ^ 6 ^ 7 = 0, and so on
        // So, we can find the remainder of n when divided by 4 to determine the last number in the pattern
        int remainder = n % 4;
        
        // If the remainder is 0, the XOR is the same as the XOR of all numbers up to the previous multiple of 4
        if (remainder == 0) {
            return n;
        }
        // If the remainder is 1, the XOR is the same as the XOR of all numbers up to the previous multiple of 4 plus 1
        else if (remainder == 1) {
            return 1;
        }
        // If the remainder is 2, the XOR is the same as the XOR of all numbers up to the previous multiple of 4 plus 3
        else if (remainder == 2) {
            return n + 1;
        }
        // If the remainder is 3, the XOR is the same as the XOR of all numbers up to the previous multiple of 4 plus 2
        else {
            return 0;
        }
    }
};
```

## Test Cases
```
Input: n = 5
Output: 1
Input: n = 10
Output: 7
Input: n = 17
Output: 10
```

## Key Takeaways
- The XOR operation has a repeating pattern every 4 numbers.
- We can use the remainder of n when divided by 4 to determine the last number in the pattern and calculate the XOR efficiently.
- This solution has a time complexity of O(1) and space complexity of O(1), making it efficient for large inputs.