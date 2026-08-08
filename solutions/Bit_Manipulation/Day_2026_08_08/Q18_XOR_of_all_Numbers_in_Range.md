# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n, find the XOR of all numbers in this range. The input will be an integer n, and the output should be the XOR of all numbers from 0 to n. For example, if n = 3, the XOR of all numbers in the range will be 0 ^ 1 ^ 2 ^ 3 = 4, but if n = 4, the XOR will be 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4 as well because 4 is not included in the XOR operation when n is odd, but when n is even, n is included in the XOR.

## Approach
The XOR of all numbers from 0 to n can be found by using the properties of XOR operation. We can observe that the XOR of all numbers from 0 to n follows a pattern: when n is a multiple of 4, the result is n; when n is 1 more than a multiple of 4, the result is 1; when n is 2 more than a multiple of 4, the result is n + 1; when n is 3 more than a multiple of 4, the result is 0.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int xorOfRange(int n) {
    // if n is a multiple of 4, return n
    if (n % 4 == 0) return n;
    // if n is 1 more than a multiple of 4, return 1
    if (n % 4 == 1) return 1;
    // if n is 2 more than a multiple of 4, return n + 1
    if (n % 4 == 2) return n + 1;
    // if n is 3 more than a multiple of 4, return 0
    return 0;
}

int main() {
    int n;
    cin >> n;
    cout << xorOfRange(n);
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
- The XOR operation has a pattern when applied to a range of numbers from 0 to n.
- The pattern can be used to find the XOR of all numbers in the range in constant time.
- The solution does not require iterating over all numbers in the range, making it efficient for large inputs.