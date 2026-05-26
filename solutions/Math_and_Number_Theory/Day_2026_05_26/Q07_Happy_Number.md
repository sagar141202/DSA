# Happy Number

## Problem Statement
A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Given a number, determine if it is a happy number. Constraints: 1 <= n <= 2^31 - 1. Examples: Input: 19, Output: true; Input: 20, Output: false.

## Approach
The algorithm involves repeatedly replacing the number with the sum of the squares of its digits until it reaches 1 or a cycle is detected. We use a hash set to store the numbers we've seen so far to detect cycles. If we encounter a number we've seen before, we know it's not a happy number.

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
- Use a hash set to store the numbers we've seen to detect cycles.
- The time complexity is O(log n) because the number of digits in a number is proportional to the logarithm of the number.
- The space complexity is O(log n) because in the worst case, we might have to store all the numbers from n to 1 in the hash set.