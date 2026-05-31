# Happy Number

## Problem Statement
A happy number is defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Given a number, determine if it is a happy number. The input will be a positive integer, and the output should be true if the number is happy, false otherwise. For example, 19 is a happy number because the process goes as follows: 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100, 1^2 + 0^2 + 0^2 = 1.

## Approach
The algorithm involves continuously replacing the number with the sum of the squares of its digits until it reaches 1 or a cycle is detected. We can use a set to keep track of the numbers we've seen to detect cycles. The process repeats until the number becomes 1 or a cycle is found.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isHappy(int n) {
    // Create a set to store the numbers we've seen
    unordered_set<int> seen;
    while (n != 1 && seen.find(n) == seen.end()) {
        // Add the current number to the set
        seen.insert(n);
        int sum = 0;
        // Calculate the sum of the squares of the digits
        while (n) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        // Update the number for the next iteration
        n = sum;
    }
    // Return true if the number is happy, false otherwise
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
- Happy numbers are defined by a process that replaces the number with the sum of the squares of its digits.
- The process repeats until the number becomes 1 or a cycle is detected.
- Using a set to keep track of the numbers we've seen allows us to detect cycles efficiently.