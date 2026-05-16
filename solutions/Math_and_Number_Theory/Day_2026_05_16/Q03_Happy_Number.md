# Happy Number

## Problem Statement
A happy number is defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Given a positive integer, determine if it's a happy number.

## Approach
The algorithm involves continuously replacing the number with the sum of the squares of its digits until it reaches 1 or a cycle is detected. We can use a set to keep track of the numbers we've seen to detect cycles. The process is repeated until the number becomes 1 or a cycle is found.

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
- Happy numbers are defined by a process that replaces the number with the sum of the squares of its digits.
- We can use a set to keep track of the numbers we've seen to detect cycles and determine if a number is happy.
- The time complexity of this solution is O(log n) because the number of digits in a number is logarithmic in its value.