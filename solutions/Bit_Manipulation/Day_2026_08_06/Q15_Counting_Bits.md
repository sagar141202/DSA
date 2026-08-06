# Counting Bits

## Problem Statement
Given a non-negative integer `n`, count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. The function should return an array where the `i-th` index contains the number of bits set in the binary representation of `i`. For example, given `n = 5`, the binary representations are `0` (0), `1` (1), `10` (2), `11` (3), `100` (4), and `101` (5). The number of bits set in each representation is `0`, `1`, `1`, `2`, `1`, and `2` respectively. The function should return the array `[0, 1, 1, 2, 1, 2]`.

## Approach
The approach is to use dynamic programming to store the number of bits set for each number up to `n`. We can use the fact that the number of bits set in `i` is equal to the number of bits set in `i / 2` plus the least significant bit of `i`. This allows us to build up the solution iteratively.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> countBits(int n) {
    vector<int> res(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        // for each i, the number of bits set is the number of bits set in i / 2 plus the least significant bit of i
        res[i] = res[i >> 1] + (i & 1);
    }
    return res;
}
```

## Test Cases
```
Input: n = 5
Output: [0, 1, 1, 2, 1, 2]
Input: n = 10
Output: [0, 1, 1, 2, 1, 2, 2, 1, 2, 2, 3]
```

## Key Takeaways
- The number of bits set in `i` can be calculated using the number of bits set in `i / 2` and the least significant bit of `i`.
- Dynamic programming can be used to store the number of bits set for each number up to `n`.
- The time complexity of the solution is O(n) and the space complexity is O(n).