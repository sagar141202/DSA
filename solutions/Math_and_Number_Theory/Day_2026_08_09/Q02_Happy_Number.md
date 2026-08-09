# Happy Number

## Problem Statement
A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Given a positive integer n, write a function to determine if it is a happy number. The input will be an integer between 1 and 2^31 - 1. For example, 19 is a happy number because the process goes as follows: 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100, 1^2 + 0^2 + 0^2 = 1.

## Approach
To solve this problem, we will use a cycle detection approach, where we keep track of the numbers we have seen so far. If we encounter a number we have seen before, we know that the process will loop endlessly and the number is not happy. Otherwise, we continue the process until we reach 1.

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
        while (n > 0) {
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
Output: True
Input: 20
Output: False
```

## Key Takeaways
- We use an unordered_set to keep track of the numbers we have seen so far, allowing us to detect cycles efficiently.
- The time complexity is O(log n) because the number of digits in the input number is proportional to the logarithm of the number.
- The space complexity is also O(log n) because in the worst case, we need to store all the digits of the input number in the unordered_set.