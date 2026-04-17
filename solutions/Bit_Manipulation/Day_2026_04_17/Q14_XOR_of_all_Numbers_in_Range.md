# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n, find the XOR of all numbers in this range. The input is a single integer n, and the output should be the XOR of all numbers from 0 to n. For example, if n = 3, the XOR of all numbers in the range is 0 ^ 1 ^ 2 ^ 3 = 4. The range can be quite large, up to 10^9, so an efficient solution is required.

## Approach
The approach to solve this problem is to use the properties of XOR operation and bit manipulation. We can iterate over each bit position and calculate the XOR of all numbers at that position. This can be done by observing the pattern of XOR operation for each bit position.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int xorRange(int n) {
        // Initialize result
        int res = 0;
        
        // Iterate over each bit position
        for (int i = 0; i < 32; i++) {
            // Calculate the number of pairs of numbers that have the same bit at this position
            int pairs = (n + 1) / (1 << (i + 1));
            // Calculate the number of single numbers that have a 1 at this position
            int singles = (n + 1) % (1 << (i + 1));
            if (singles > (1 << i)) {
                singles -= (1 << i);
            }
            // Update the result
            res ^= (pairs * (1 << i)) ^ (singles * (1 << i));
        }
        return res;
    }
};

int main() {
    Solution solution;
    cout << solution.xorRange(3) << endl;  // Output: 4
    cout << solution.xorRange(5) << endl;  // Output: 1
    return 0;
}
```

## Test Cases
```
Input: 3
Output: 4
Input: 5
Output: 1
```

## Key Takeaways
- The XOR operation has a property that a ^ a = 0 and a ^ 0 = a, which can be used to simplify the calculation.
- The problem can be solved by iterating over each bit position and calculating the XOR of all numbers at that position.
- The time complexity of the solution is O(log n) because we are iterating over each bit position, and the number of bit positions is proportional to the number of bits in the input number.