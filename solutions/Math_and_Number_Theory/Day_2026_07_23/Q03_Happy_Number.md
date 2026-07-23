# Happy Number

## Problem Statement
A happy number is defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Given a positive integer n, write a function to determine if it's a happy number.

## Approach
The approach is to continuously calculate the sum of squares of digits until we reach 1 or a cycle is detected. We can use a HashSet to store the numbers we've seen so far to detect cycles. The algorithm will terminate when we reach 1 (happy number) or when we encounter a number we've seen before (not a happy number).

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
- Happy numbers are defined by a simple iterative process that can be implemented using a loop and a HashSet to detect cycles.
- The time complexity is O(log n) because the number of digits in n decreases by at least one in each iteration, and the space complexity is also O(log n) due to the storage of seen numbers.