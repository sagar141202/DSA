# Happy Number

## Problem Statement
A happy number is defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Given a positive integer n, write a function to determine if it is a happy number. Constraints: 1 <= n <= 2^31 - 1. Examples: Input: 19 - Output: true, Input: 20 - Output: false.

## Approach
The algorithm involves continuously replacing the number with the sum of the squares of its digits until we reach 1 or a cycle. We use a set to keep track of seen numbers to detect cycles. The process is repeated until the number becomes 1 or a cycle is detected.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isHappy(int n) {
    unordered_set<int> seen;
    while (n != 1 && seen.find(n) == seen.end()) {
        seen.insert(n);
        int sum = 0;
        while (n) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        n = sum;
    }
    return n == 1;
}
```

## Test Cases
```
Input: 19
Output: true
Input: 20
Output: false
```

## Key Takeaways
- Happy numbers are defined by a specific iterative process that may result in 1 or a cycle.
- Using a set to keep track of seen numbers is crucial for detecting cycles efficiently.
- The time complexity is O(log n) because in the worst case, the number of digits in n is proportional to log(n).