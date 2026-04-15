# Happy Number

## Problem Statement
A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Given a positive integer n, write a function to determine if it's a happy number. The input will be in the range [1, 2^31 - 1]. For example, 19 is a happy number because the process goes as follows: 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100, 1^2 + 0^2 + 0^2 = 1.

## Approach
The algorithm involves repeatedly replacing the number by the sum of the squares of its digits until it reaches 1 or a cycle is detected. We can use a set to store the numbers we have seen to detect cycles. The process is repeated until the number becomes 1 or a cycle is detected.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isHappy(int n) {
    // Store the numbers we have seen to detect cycles
    unordered_set<int> seen;
    
    while (n != 1 && seen.find(n) == seen.end()) {
        seen.insert(n);
        
        // Calculate the sum of the squares of the digits
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
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
- Use a set to store the numbers we have seen to detect cycles.
- Repeatedly replace the number by the sum of the squares of its digits until it reaches 1 or a cycle is detected.
- The time complexity is O(log n) because the number of digits in the number decreases by a factor of 10 in each iteration.