# Happy Number

## Problem Statement
A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Given a number, determine if it is a happy number. The input will be an integer in the range [1, 2^31 - 1]. For example, 19 is a happy number because the process goes as follows: 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100, 1^2 + 0^2 + 0^2 = 1.

## Approach
The algorithm involves repeatedly replacing the number with the sum of the squares of its digits until it reaches 1 or a cycle is detected. We can use a hash set to keep track of the numbers we have seen so far to detect cycles. The process is repeated until the number becomes 1 or a cycle is detected.

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
Output: true
Input: 20
Output: false
```

## Key Takeaways
- Happy numbers are defined by a process of replacing the number with the sum of the squares of its digits.
- The process can be repeated until the number reaches 1 or a cycle is detected.
- Using a hash set to keep track of the numbers we have seen so far can help detect cycles efficiently.