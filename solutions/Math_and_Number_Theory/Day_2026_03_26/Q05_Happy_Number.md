# Happy Number

## Problem Statement
A happy number is defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Given a number, determine if it is a happy number. Constraints: 1 <= n <= 2^31 - 1. Examples: Input: 19, Output: true; Input: 20, Output: false.

## Approach
The algorithm involves continuously replacing the number by the sum of the squares of its digits until it reaches 1 or a cycle is detected. We can use a set to store seen numbers to detect cycles. The process is repeated until the number becomes 1 or a cycle is found.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        // create a set to store seen numbers
        unordered_set<int> seen;
        
        // continue the process until n becomes 1 or a cycle is detected
        while (n != 1 && seen.find(n) == seen.end()) {
            seen.insert(n);
            int sum = 0;
            // calculate the sum of squares of digits
            while (n > 0) {
                int digit = n % 10;
                sum += digit * digit;
                n /= 10;
            }
            n = sum;
        }
        // return true if n is 1, false otherwise
        return n == 1;
    }
};
```

## Test Cases
```
Input: 19
Output: true
Input: 20
Output: false
```

## Key Takeaways
- Use a set to store seen numbers to detect cycles.
- The time complexity is O(log n) because the number of digits in a number n is logarithmic in n.
- The space complexity is O(log n) due to the set used to store seen numbers.