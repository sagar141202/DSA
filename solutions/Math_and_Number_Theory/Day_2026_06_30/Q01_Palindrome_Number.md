# Palindrome Number

## Problem Statement
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise. A palindrome is a number or a text phrase that reads the same backwards as forwards. For example, "12321" is a palindrome number. The input will be a 32-bit signed integer, and we need to determine whether this integer is a palindrome or not. Constraints: `-2^31 <= x <= 2^31 - 1`.

## Approach
The approach is to convert the integer into a string and then compare it with its reverse. If they are the same, the number is a palindrome. Alternatively, we can also solve this problem mathematically by reversing the integer and comparing it with the original number.

## Complexity
- Time: O(log(n))
- Space: O(log(n))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        // If x is negative, it's not a palindrome
        if (x < 0) return false;
        
        // Convert integer to string
        string str = to_string(x);
        
        // Initialize two pointers
        int left = 0;
        int right = str.size() - 1;
        
        // Compare characters from both ends
        while (left < right) {
            if (str[left] != str[right]) return false;
            left++;
            right--;
        }
        
        return true;
    }
};
```

## Test Cases
```
Input: 121
Output: true
Input: -121
Output: false
Input: 10
Output: false
```

## Key Takeaways
- We can solve this problem by converting the integer to a string and comparing it with its reverse.
- Alternatively, we can reverse the integer mathematically and compare it with the original number.
- The time complexity of the solution is O(log(n)) because the number of digits in the integer is logarithmic in the size of the input.