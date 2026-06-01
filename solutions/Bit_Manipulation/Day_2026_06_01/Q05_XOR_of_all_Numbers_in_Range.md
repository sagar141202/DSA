# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n (inclusive), find the XOR of all numbers in this range. For example, if n = 3, the XOR of all numbers in the range would be 0 ^ 1 ^ 2 ^ 3 = 4, but if n = 4, the XOR would be 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4, because 0 ^ 1 ^ 2 ^ 3 ^ 4 = (0 ^ 2 ^ 4) ^ (1 ^ 3) = (0 ^ 4) ^ (1 ^ 3) = 4 ^ 0 = 4. Constraints: 0 <= n <= 10^6.

## Approach
The XOR operation has a property that a ^ a = 0 and a ^ 0 = a. We can use this property to simplify the calculation by pairing up numbers in the range. If n is even, all numbers can be paired up, resulting in an XOR of 0, except for the case where n is a power of 2 minus 1 (n = 2^k - 1) or n is a power of 2 (n = 2^k), in which case the result is n + 1.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int xor_of_range(int n) {
    // If n is a power of 2 minus 1, the XOR is n + 1
    if ((n + 1) % 4 == 0) return n + 1;
    // If n is a power of 2, the XOR is n
    if (n % 4 == 0) return n;
    // For other cases, the XOR alternates between n + 1 and 0
    if (n % 4 == 1) return 1;
    // If none of the above conditions are met, the XOR is 0
    return 0;
}

int main() {
    int n;
    cin >> n;
    cout << xor_of_range(n);
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
Input: 7
Output: 0
```

## Key Takeaways
- The XOR operation can be simplified using its properties.
- The result of XOR of all numbers in a range from 0 to n depends on the value of n modulo 4.
- For large ranges, the result can be calculated in constant time using the properties of XOR.