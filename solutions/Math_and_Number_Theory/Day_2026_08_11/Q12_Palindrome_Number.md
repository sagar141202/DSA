# Palindrome Number

## Problem Statement
Given a non-negative integer, determine whether it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The input will be an integer, and the output will be a boolean indicating whether the number is a palindrome or not. The constraints are that the input integer will be between 0 and 2^31 - 1.

## Approach
The algorithm to solve this problem is to reverse the input number and compare it with the original number. If they are the same, then the number is a palindrome. We can reverse the number by taking the last digit of the number using the modulus operator and appending it to the reversed number.

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
        // if the number is negative, it's not a palindrome
        if (x < 0) return false;
        
        // initialize the reversed number
        int reversed = 0;
        
        // store the original number
        int original = x;
        
        // reverse the number
        while (x != 0) {
            // get the last digit of the number
            int digit = x % 10;
            
            // append the digit to the reversed number
            reversed = reversed * 10 + digit;
            
            // remove the last digit from the number
            x /= 10;
        }
        
        // check if the reversed number is the same as the original number
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
```

## Key Takeaways
- To check if a number is a palindrome, we need to reverse the number and compare it with the original number.
- We can reverse a number by taking the last digit of the number using the modulus operator and appending it to the reversed number.
- The time complexity of this solution is O(log n) because we are iterating over the digits of the number, and the number of digits in a number is proportional to the logarithm of the number.