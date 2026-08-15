# Happy Number

## Problem Statement
A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Given a positive integer n, write a function to determine if it is a happy number. Constraints: 1 <= n <= 2^31 - 1. Examples: Input: 19, Output: true; Input: 20, Output: false.

## Approach
We can solve this problem by using a while loop to continuously calculate the sum of the squares of the digits of the number until it equals 1 or a cycle is detected. We use a set to store the numbers we have seen to detect the cycle.

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
- Happy numbers are defined by the process of replacing the number with the sum of the squares of its digits.
- We can use a set to detect cycles and determine if a number is happy.
- The time complexity is O(log n) because the number of digits in n is logarithmic in n.