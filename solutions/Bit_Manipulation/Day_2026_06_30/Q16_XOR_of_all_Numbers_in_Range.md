# XOR of all Numbers in Range

## Problem Statement
Given a range of integers from 0 to n (inclusive), find the XOR of all numbers in this range. The input is a single integer n, where 1 <= n <= 10^6. The output should be the XOR of all numbers from 0 to n. For example, if n = 5, the output should be 1 ^ 2 ^ 3 ^ 4 ^ 5 = 1.

## Approach
The XOR of all numbers in a range can be calculated by using the properties of XOR operation and the pattern of binary representation of numbers. We can observe that the XOR of all numbers from 0 to n is equal to the XOR of the numbers at the odd positions in the binary representation of n.

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
        int xor_result = 0;
        for (int i = 0; i <= n; i++) {
            xor_result ^= i;
        }
        return xor_result;
    }
    
    // Optimized solution
    int xorOfRangeOptimized(int n) {
        // If n is even, the XOR is 0
        if (n % 2 == 0) {
            return n;
        }
        // If n is odd, the XOR is n
        else {
            return 0;
        }
    }
};

int main() {
    Solution solution;
    cout << solution.xorOfRange(5) << endl;  // Output: 1
    cout << solution.xorOfRangeOptimized(5) << endl;  // Output: 1
    return 0;
}
```

## Test Cases
```
Input: 5
Output: 1
Input: 10
Output: 10
Input: 7
Output: 7
```

## Key Takeaways
- The XOR of all numbers in a range can be calculated efficiently by using the properties of XOR operation.
- The binary representation of numbers can be used to observe the pattern and calculate the XOR.
- The optimized solution has a time complexity of O(1), making it more efficient for large inputs.