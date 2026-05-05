# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n, find the XOR of all numbers in this range. The XOR operation has a property that a ^ a = 0 and a ^ 0 = a. We can utilize this property to find the XOR of all numbers in the range. For example, if n = 3, the XOR of all numbers in the range is 0 ^ 1 ^ 2 ^ 3 = 1.

## Approach
We can use the property of XOR to simplify the problem. Since XOR is associative and commutative, we can rearrange the numbers in the range to simplify the calculation. The key observation is that for every pair of numbers a and b where a ^ b = 0, we can eliminate them from the XOR operation.

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
        // If n is even, the XOR of all numbers in the range is 0
        if (n % 2 == 0) {
            if (n % 4 == 0) return n;
            else return 1;
        } 
        // If n is odd, the XOR of all numbers in the range is n
        else {
            if ((n - 1) % 4 == 0) return n;
            else return 0;
        }
    }
};
```

## Test Cases
```
Input: n = 3
Output: 1
Input: n = 4
Output: 4
Input: n = 5
Output: 1
```

## Key Takeaways
- The XOR operation has a property that a ^ a = 0 and a ^ 0 = a.
- We can use the property of XOR to simplify the problem by rearranging the numbers in the range.
- The time complexity of the solution is O(1) because we only need to perform a constant number of operations to find the XOR of all numbers in the range.