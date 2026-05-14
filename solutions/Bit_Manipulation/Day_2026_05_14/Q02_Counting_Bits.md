# Counting Bits

## Problem Statement
Given an integer `n`, return an array of size `n + 1` where each index `i` represents the number of bits that are set to 1 in the binary representation of `i`. For example, given `n = 5`, the binary representations are: `0` (0), `1` (1), `10` (2), `11` (3), `100` (4), `101` (5). So the output should be `[0, 1, 1, 2, 1, 2]`. The constraints are `0 <= n <= 10^5`.

## Approach
We can use dynamic programming to solve this problem by building up the binary representation of each number and counting the number of set bits. Alternatively, we can use bitwise operations to directly calculate the number of set bits for each number.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            // use bitwise operation to count the number of set bits
            result[i] = result[i >> 1] + (i & 1);
        }
        return result;
    }
};
```

## Test Cases
```
Input: 5
Output: [0, 1, 1, 2, 1, 2]
Input: 10
Output: [0, 1, 1, 2, 1, 2, 2, 1, 2, 2, 3]
```

## Key Takeaways
- Use bitwise operations to directly calculate the number of set bits for each number.
- Dynamic programming can be used to build up the binary representation of each number and count the number of set bits.
- The time complexity is O(n) and the space complexity is O(n) for storing the result.