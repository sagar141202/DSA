# Palindrome Number

## Problem Statement
Given a non-negative integer, determine if it is a palindrome. A palindrome is a number that remains the same when its digits are reversed. For example, 121 is a palindrome, but 123 is not. The input will be a single integer, and the output should be a boolean value indicating whether the number is a palindrome or not. The constraints are: the input integer will be in the range [0, 2^31 - 1].

## Approach
We will use a simple iterative approach to reverse the number and compare it with the original number. This approach involves reversing the number by taking the last digit and appending it to the reversed number, and then removing the last digit from the original number.

## Complexity
- Time: O(log(n))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        // if the number is negative, it cannot be a palindrome
        if (x < 0) return false;
        
        // store the original number
        int original = x;
        
        // initialize the reversed number
        int reversed = 0;
        
        // reverse the number
        while (x != 0) {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
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
- A palindrome number reads the same backward as forward.
- The time complexity of this solution is O(log(n)) because we are iterating over the digits of the number, and the number of digits in a number is proportional to the logarithm of the number.
- The space complexity of this solution is O(1) because we are using a constant amount of space to store the original and reversed numbers.