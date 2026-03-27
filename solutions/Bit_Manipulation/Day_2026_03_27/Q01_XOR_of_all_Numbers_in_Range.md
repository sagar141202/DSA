# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n, find the XOR of all numbers in this range. The XOR operation has a property that a ^ a = 0 and a ^ 0 = a. We can use this property to simplify the problem. For example, if n is even, then the XOR of all numbers from 0 to n can be calculated by XORing the XOR of all numbers from 0 to n/2 with the XOR of all numbers from n/2 to n, but because of the properties of XOR, this simplifies to just the XOR of all numbers from 0 to n/2, repeated. However, for odd n, the middle number does not have a pair to cancel it out, so it remains. The range of n is from 0 to 10^6.

## Approach
The XOR of all numbers in a range can be calculated by using the properties of XOR operation. We can observe a pattern where the XOR of all numbers up to a certain point repeats every 4 numbers (0, 1, 3, 0). This pattern can be used to simplify the calculation. By using this pattern, we can calculate the XOR of all numbers in the range in constant time.

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
        // If n is even, the XOR is the same as the XOR of numbers up to n-1
        if (n % 4 == 0) return n;
        // If n is odd and of the form 4k+1, the XOR is the same as the XOR of numbers up to 1
        if (n % 4 == 1) return 1;
        // If n is odd and of the form 4k+2, the XOR is the same as the XOR of numbers up to 2 (which is 3)
        if (n % 4 == 2) return n + 1;
        // If n is odd and of the form 4k+3, the XOR is the same as the XOR of numbers up to 3 (which is 0)
        return 0;
    }
};
```

## Test Cases
```
Input: n = 5
Output: 1
Input: n = 10
Output: 10
```

## Key Takeaways
- The XOR operation has a repeating pattern every 4 numbers (0, 1, 3, 0).
- By using this pattern, we can calculate the XOR of all numbers in a range in constant time.
- The solution has a time complexity of O(1) and space complexity of O(1), making it efficient for large inputs.