# Happy Number

## Problem Statement
A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Given a positive integer n, write a function to determine if it's a happy number. The input will be an integer between 1 and 2^31 - 1.

## Approach
We use a HashSet to store the numbers we have seen so far to detect the cycle. We calculate the sum of squares of digits of the current number and update the current number. We repeat this process until the current number becomes 1 or we detect a cycle.

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
- Use a HashSet to detect cycles in the sequence of numbers.
- The time complexity is O(log n) because the number of digits in a number is proportional to the logarithm of the number.
- The space complexity is O(log n) because in the worst case, we might have to store all the numbers in the sequence, and the maximum length of the sequence is proportional to the logarithm of the input number.