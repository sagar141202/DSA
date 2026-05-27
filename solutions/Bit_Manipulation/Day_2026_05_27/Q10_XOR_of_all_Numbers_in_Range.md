# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n, find the XOR of all numbers in this range. The range is inclusive, meaning it includes both 0 and n. For example, if n = 3, the XOR of all numbers in the range would be 0 ^ 1 ^ 2 ^ 3 = 4, but if n = 4, the XOR would be 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4. The goal is to write an efficient algorithm to compute this XOR.

## Approach
The approach is to use the properties of XOR operation and bit manipulation to find the XOR of all numbers in the range. We can observe that the XOR of all numbers from 0 to n can be calculated by finding the XOR of all numbers from 0 to n-1 and then XORing the result with n.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int xorRange(int n) {
        // If n is a multiple of 4, the XOR is n
        if (n % 4 == 0) return n;
        
        // If n is 1 more than a multiple of 4, the XOR is 1
        if (n % 4 == 1) return 1;
        
        // If n is 2 more than a multiple of 4, the XOR is n + 1
        if (n % 4 == 2) return n + 1;
        
        // If n is 3 more than a multiple of 4, the XOR is 0
        return 0;
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
- The XOR operation has a periodic nature with a period of 4.
- By using this periodicity, we can calculate the XOR of all numbers in the range in constant time.
- This problem is a classic example of using bit manipulation and properties of XOR operation to solve a problem efficiently.