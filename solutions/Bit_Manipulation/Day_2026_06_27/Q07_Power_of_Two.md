# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. A power of two is a number that can be expressed as 2^x where x is an integer. The function should return `true` if `n` is a power of two, and `false` otherwise. The input `n` is a 32-bit signed integer, and `n` is in the range [0, 2^31 - 1]. For example, given `n = 16`, the function should return `true` because 16 can be expressed as 2^4.

## Approach
We can use bit manipulation to solve this problem by checking if the binary representation of `n` has exactly one '1' bit. If `n` is a power of two, then its binary representation will have exactly one '1' bit. We can use the bitwise AND operator to check this.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPowerOfTwo(int n) {
        // Check if n is less than or equal to 0
        if (n <= 0) {
            return false;
        }
        // Use bitwise AND operator to check if n is a power of two
        return (n & (n - 1)) == 0;
    }
};
```

## Test Cases
```
Input: n = 16
Output: true
Input: n = 20
Output: false
```

## Key Takeaways
- A power of two has exactly one '1' bit in its binary representation.
- The bitwise AND operator can be used to check if a number is a power of two.
- The time complexity of this solution is O(1) because it only involves a constant number of operations.