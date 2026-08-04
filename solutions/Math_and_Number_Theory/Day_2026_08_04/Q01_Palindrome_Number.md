# Palindrome Number

## Problem Statement
Given a non-negative integer, determine whether it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The input will be a 32-bit signed integer, and the output will be a boolean value indicating whether the number is a palindrome or not. The constraints are: -2^31 <= x <= 2^31 - 1.

## Approach
The algorithm involves converting the integer into a string and comparing it with its reverse. Alternatively, we can also reverse the integer mathematically without converting it to a string. We will use the latter approach to avoid string operations.

## Complexity
- Time: O(log(n))
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        // handle negative numbers
        if (x < 0) return false;
        
        int original = x;
        int reversed = 0;
        
        // reverse the number
        while (x != 0) {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        
        // compare the original and reversed numbers
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
- We can reverse an integer without converting it to a string by using the modulo operator to extract the last digit and integer division to remove the last digit.
- We should handle negative numbers separately because they cannot be palindromes due to the negative sign.
- The time complexity of the solution is O(log(n)) because we are essentially counting the number of digits in the input number.