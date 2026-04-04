# Happy Number

## Problem Statement
A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Given an integer, determine if it is a happy number.

## Approach
The algorithm uses a HashSet to store the numbers we've seen so far. We keep replacing the number with the sum of the squares of its digits until we reach 1 or a cycle is detected. If we reach 1, the number is happy; otherwise, it's not.

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
- Use a HashSet to detect cycles in the sequence of numbers.
- The time complexity is O(log n) because the number of digits in n is roughly log(n).
- The space complexity is O(log n) due to the storage of the HashSet.