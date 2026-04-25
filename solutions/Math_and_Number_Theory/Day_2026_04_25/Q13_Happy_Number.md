# Happy Number

## Problem Statement
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Given a number, determine if it is a happy number. The input number will be in the range [1, 2^31 - 1]. For example, 19 is a happy number because the process starts with 1^2 + 9^2 = 82, then 8^2 + 2^2 = 68, and then 6^2 + 8^2 = 100, followed by 1^2 + 0^2 + 0^2 = 1.

## Approach
The algorithm involves repeatedly replacing the number with the sum of the squares of its digits until it reaches 1 or a cycle is detected. We can use a set to keep track of the numbers we've seen to detect cycles. The process is repeated until the desired result is obtained.

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
Output: true
Input: 20
Output: false
```

## Key Takeaways
- Happy numbers are defined by a specific process that involves replacing the number with the sum of the squares of its digits.
- To determine if a number is happy, we can use a set to keep track of the numbers we've seen to detect cycles.
- The time complexity of this solution is O(log n) because we're effectively reducing the number of digits in each iteration.