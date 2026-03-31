# Happy Number

## Problem Statement
A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Given a number, determine if it is a happy number. The input number will be in the range [1, 2^31 - 1]. For example, 19 is a happy number because the process goes as follows: 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100, 1^2 + 0^2 + 0^2 = 1.

## Approach
The algorithm uses a hash set to keep track of the numbers that have been seen so far to detect a cycle. It then repeatedly replaces the number with the sum of the squares of its digits until it reaches 1 or a cycle is detected. The process involves converting the number to a string to easily access each digit, squaring each digit, and summing them up.

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
- To determine if a number is happy, we need to keep track of the numbers we have seen so far to avoid an infinite loop.
- We use a hash set for efficient lookups of previously seen numbers.
- The process of replacing a number with the sum of the squares of its digits is repeated until we reach 1 or detect a cycle.