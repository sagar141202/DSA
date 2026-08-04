# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n, calculate the XOR of all numbers in this range. The range is defined by a single integer n, where n is a non-negative integer. For example, if n = 4, the XOR of all numbers in the range would be 0 XOR 1 XOR 2 XOR 3 XOR 4.

## Approach
The approach involves using the properties of XOR operation to simplify the calculation. We can use the fact that XOR of all numbers from 0 to n can be calculated by finding the XOR of all numbers from 0 to n-1 and then XORing it with n.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int xorOfRange(int n) {
        // If n is a multiple of 4, then the XOR of all numbers from 0 to n is n
        if (n % 4 == 0) return n;
        // If n is one more than a multiple of 4, then the XOR of all numbers from 0 to n is 1
        if (n % 4 == 1) return 1;
        // If n is two more than a multiple of 4, then the XOR of all numbers from 0 to n is n+1
        if (n % 4 == 2) return n+1;
        // If n is three more than a multiple of 4, then the XOR of all numbers from 0 to n is 0
        return 0;
    }
};

int main() {
    Solution solution;
    cout << solution.xorOfRange(4) << endl;  // Output: 4
    cout << solution.xorOfRange(5) << endl;  // Output: 1
    cout << solution.xorOfRange(6) << endl;  // Output: 7
    cout << solution.xorOfRange(7) << endl;  // Output: 0
    return 0;
}
```

## Test Cases
```
Input: 4
Output: 4
Input: 5
Output: 1
Input: 6
Output: 7
Input: 7
Output: 0
```

## Key Takeaways
- The XOR operation has a cyclical pattern of length 4: 0, 1, n+1, 0.
- We can use this pattern to calculate the XOR of all numbers in a range in constant time.
- The solution involves finding the remainder of n when divided by 4 and using it to determine the XOR of all numbers in the range.