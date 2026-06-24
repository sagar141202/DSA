# Happy Number

## Problem Statement
A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Given a positive integer, determine if it's a happy number. Constraints: 1 <= n <= 2^31 - 1. Examples: Input: 19, Output: True; Input: 20, Output: False.

## Approach
To solve this problem, we will use a simple iterative approach where we keep replacing the number with the sum of the squares of its digits until we reach 1 or detect a cycle. We can detect a cycle by storing the numbers we have seen so far.

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
- We use an unordered_set to store the numbers we have seen to detect cycles efficiently.
- The time complexity is O(log n) because the number of digits in a number is logarithmic in its value.
- The space complexity is also O(log n) because in the worst case, we might store all the numbers in the cycle, which can be logarithmic in the input value.