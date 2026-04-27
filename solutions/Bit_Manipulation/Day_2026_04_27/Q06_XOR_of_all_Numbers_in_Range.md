# XOR of all Numbers in Range

## Problem Statement
Given a range of integers from 0 to n (inclusive), find the XOR of all numbers in this range. The range is defined by the integer n, where 0 <= n <= 10^6. For example, if n = 5, the XOR of all numbers in the range would be 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 = 1.

## Approach
The algorithm uses the properties of XOR operation and binary representation to find the XOR of all numbers in the given range. It observes the pattern of XOR results for different ranges and utilizes this pattern to calculate the final result. The pattern is based on the fact that XOR of all numbers from 0 to 2^k - 1 is 0, and XOR of all numbers from 0 to 2^k is 2^k.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int xorOperation(int n) {
        if (n % 4 == 0) return n;
        if (n % 4 == 1) return 1;
        if (n % 4 == 2) return n + 1;
        return 0;
    }
};

int main() {
    Solution solution;
    cout << solution.xorOperation(5) << endl;  // Output: 1
    cout << solution.xorOperation(10) << endl; // Output: 11
    return 0;
}
```

## Test Cases
```
Input: n = 5
Output: 1
Input: n = 10
Output: 11
```

## Key Takeaways
- The XOR operation has a cyclical pattern for ranges of numbers, which can be utilized to simplify the calculation.
- The pattern repeats every 4 numbers (0, 1, 2, 3), resulting in XOR values of 0, 1, 3, and 0 respectively.
- For larger ranges, the pattern can be extended by considering the number of complete cycles and the remaining numbers.