# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n (inclusive), find the XOR of all numbers in this range. The input is a single integer n, and the output should be the XOR of all numbers from 0 to n. For example, if n = 3, the output should be 0 ^ 1 ^ 2 ^ 3 = 4, but if n = 4, the output should be 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4.

## Approach
The XOR operation has a property that a ^ a = 0 and a ^ 0 = a. We can utilize this property to find the XOR of all numbers in the range. By observing the pattern of XOR of numbers from 0 to n, we can derive a formula to calculate the result directly.

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
        // If n is a multiple of 4, then the XOR will be n
        if (n % 4 == 0) return n;
        // If n is 1 more than a multiple of 4, then the XOR will be 1
        if (n % 4 == 1) return 1;
        // If n is 2 more than a multiple of 4, then the XOR will be n + 1
        if (n % 4 == 2) return n + 1;
        // If n is 3 more than a multiple of 4, then the XOR will be 0
        return 0;
    }
};

int main() {
    Solution solution;
    cout << solution.xorOfRange(3) << endl;  // Output: 4
    cout << solution.xorOfRange(4) << endl;  // Output: 4
    return 0;
}
```

## Test Cases
```
Input: 3
Output: 4
Input: 4
Output: 4
Input: 5
Output: 1
Input: 6
Output: 7
```

## Key Takeaways
- The XOR operation follows a pattern when applied to a range of numbers.
- We can use the properties of XOR to derive a formula for the XOR of a range of numbers.
- This solution has a constant time complexity, making it efficient for large inputs.