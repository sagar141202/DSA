# Happy Number

## Problem Statement
A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Given a number, determine if it is a happy number. Constraints: 1 <= n <= 2^31 - 1. Examples: Input: 19, Output: True; Input: 20, Output: False.

## Approach
The algorithm involves repeatedly replacing the number with the sum of the squares of its digits until it reaches 1 or a cycle is detected. We can use a set to store the numbers we have seen to detect cycles. The process continues until the number becomes 1 or a cycle is detected.

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
            while (n) {
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
- Happy numbers are defined by a process of summing the squares of digits.
- A set can be used to detect cycles in the process.
- The time complexity is O(log n) due to the number of digits in the input number.