# Palindrome Number

## Problem Statement
Given a non-negative integer, determine whether it is a palindrome number. A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome number, but 123 is not. The input integer will be in the range [0, 2^31 - 1]. The function should return true if the number is a palindrome and false otherwise.

## Approach
We can solve this problem by converting the integer into a string and checking if the string is the same when reversed. Alternatively, we can also solve it mathematically by reversing the integer and comparing it with the original number.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        // if x is negative, it's not a palindrome
        if (x < 0) return false;
        
        // convert integer to string
        string str = to_string(x);
        
        // initialize two pointers
        int left = 0, right = str.size() - 1;
        
        // compare characters from both ends
        while (left < right) {
            if (str[left] != str[right]) return false;
            left++, right--;
        }
        
        return true;
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
- To determine if a number is a palindrome, we can convert it to a string and compare characters from both ends.
- We can also solve this problem mathematically by reversing the integer and comparing it with the original number.
- This problem requires handling edge cases such as negative numbers and single-digit numbers.