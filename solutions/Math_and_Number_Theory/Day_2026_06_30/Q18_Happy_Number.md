# Happy Number

## Problem Statement
A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Given a positive integer n, write a function to determine if it is a happy number. The input will be a positive integer, and the output should be a boolean indicating whether the number is happy or not. For example, 19 is a happy number because the process goes as follows: 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100, 1^2 + 0^2 + 0^2 = 1.

## Approach
The approach to solve this problem is to continuously calculate the sum of squares of digits until we reach 1 or a cycle is detected. We can use a set to store the numbers we have seen so far to detect the cycle. If the number becomes 1, we return true; otherwise, we return false.

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
        // Create a set to store seen numbers
        unordered_set<int> seen;
        
        // Continue the process until n becomes 1 or a cycle is detected
        while (n != 1 && seen.find(n) == seen.end()) {
            seen.insert(n);
            int sum = 0;
            // Calculate the sum of squares of digits
            while (n > 0) {
                int digit = n % 10;
                sum += digit * digit;
                n /= 10;
            }
            n = sum;
        }
        // Return true if n is 1, false otherwise
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
- Use a set to store seen numbers to detect cycles efficiently.
- The time complexity is O(log n) because the number of digits in n decreases by a factor of 10 in each iteration.
- The space complexity is O(log n) due to the storage of seen numbers.