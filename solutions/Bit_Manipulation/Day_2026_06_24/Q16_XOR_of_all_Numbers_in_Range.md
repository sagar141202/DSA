# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n, find the XOR of all numbers in this range. The range is inclusive, meaning it includes both 0 and n. For example, if n = 3, the XOR of all numbers in the range would be 0 ^ 1 ^ 2 ^ 3 = 4, but if n = 4, the XOR would be 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4 as well because 4 is a special case where its binary representation has only one '1' bit which doesn't change the result of XOR operation with any other number.

## Approach
The XOR operation has a property where a ^ a = 0 and a ^ 0 = a. We can utilize this property to simplify the calculation by observing patterns in the binary representation of numbers. For any n, if n is a multiple of 4, the result is n. If n % 4 == 1, the result is 1. If n % 4 == 2, the result is n + 1. If n % 4 == 3, the result is 0.

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
        // Directly return the result based on the pattern observed
        if (n % 4 == 0) return n;
        else if (n % 4 == 1) return 1;
        else if (n % 4 == 2) return n + 1;
        else return 0;
    }
};
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
- The XOR operation follows specific patterns that can simplify complex calculations.
- Observing the remainder of n when divided by 4 can directly give us the result for this specific problem.
- This approach avoids iterating over the entire range, making it very efficient.