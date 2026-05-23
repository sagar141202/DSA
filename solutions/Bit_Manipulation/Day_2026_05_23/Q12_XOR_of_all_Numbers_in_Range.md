# XOR of all Numbers in Range

## Problem Statement
Given a range of integers from 0 to n (inclusive), find the XOR of all numbers in this range. The range is defined by a single integer n, where 0 ≤ n ≤ 10^9. For example, if n = 5, the XOR of all numbers in the range [0, 5] is 1 ^ 2 ^ 3 ^ 4 ^ 5 = 1.

## Approach
The algorithm uses the properties of bitwise XOR operation to find the XOR of all numbers in the range. We can observe that XOR of all numbers from 0 to n can be calculated by finding the XOR of all numbers from 0 to the most significant bit of n, and then adjusting for the remaining bits.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int xorOfRange(int n) {
        // Calculate the XOR of all numbers from 0 to n
        if (n % 4 == 0) {
            // If n is a multiple of 4, the XOR is equal to n
            return n;
        } else if (n % 4 == 1) {
            // If n is 1 more than a multiple of 4, the XOR is equal to 1
            return 1;
        } else if (n % 4 == 2) {
            // If n is 2 more than a multiple of 4, the XOR is equal to n + 1
            return n + 1;
        } else {
            // If n is 3 more than a multiple of 4, the XOR is equal to 0
            return 0;
        }
    }
};

int main() {
    Solution solution;
    int n = 5; // example input
    int result = solution.xorOfRange(n);
    cout << "XOR of all numbers in range [0, " << n << "] is: " << result << endl;
    return 0;
}
```

## Test Cases
```
Input: n = 5
Output: 1
Input: n = 10
Output: 11
Input: n = 7
Output: 7
```

## Key Takeaways
- The XOR operation has a periodic pattern of length 4: 0, 1, 3, 0.
- We can use this pattern to calculate the XOR of all numbers in a range efficiently.
- The solution has a time complexity of O(log n) due to the bitwise operations involved.