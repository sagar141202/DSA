# Happy Number

## Problem Statement
A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Given a positive integer, determine if it's a happy number. Constraints: 1 <= n <= 2^31 - 1. Example: Input: 19 - Output: True, Explanation: 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100, 1^2 + 0^2 + 0^2 = 1.

## Approach
The algorithm involves continuously replacing the number with the sum of squares of its digits until it reaches 1 or a cycle is detected. We use a set to keep track of the numbers we've seen to detect cycles. The process repeats until the number becomes 1 or a cycle is found.

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
        unordered_set<int> seen;
        while (n != 1 && seen.find(n) == seen.end()) {
            seen.insert(n);
            int sum = 0;
            while (n > 0) {
                int digit = n % 10;
                sum += digit * digit;
                n /= 10;
            }
            n = sum;
        }
        return n == 1;
    }
};
```

## Test Cases
```
Input: 19
Output: True
Input: 20
Output: False
```

## Key Takeaways
- Happy numbers are defined by a process that replaces the number with the sum of squares of its digits.
- The process repeats until the number equals 1 or enters a cycle.
- Using a set to keep track of seen numbers helps detect cycles efficiently.