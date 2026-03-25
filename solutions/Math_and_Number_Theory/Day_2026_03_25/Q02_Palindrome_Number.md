# Palindrome Number

## Problem Statement
Given a non-negative integer, determine whether it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, while 123 is not. The input will be a single integer, and the output should be a boolean value indicating whether the number is a palindrome.

## Approach
To determine if a number is a palindrome, we can compare the number with its reverse. We can reverse the number by taking the last digit, then the second last digit, and so on, and append them to form the reversed number. If the original number is equal to its reverse, then the number is a palindrome.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        // If the number is negative, it cannot be a palindrome
        if (x < 0) return false;
        
        // Initialize variables to store the reversed number
        int reversed = 0;
        int original = x;
        
        // Reverse the number
        while (x != 0) {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        
        // Compare the original number with its reverse
        return original == reversed;
    }
};
```

## Test Cases
```
Input: 121
Output: true

Input: 123
Output: false

Input: -121
Output: false
```

## Key Takeaways
- We can reverse a number by taking its last digit and appending it to the reversed number, then moving to the second last digit, and so on.
- A negative number cannot be a palindrome because of the negative sign.
- The time complexity of this solution is O(log n) because we are processing each digit of the number once.