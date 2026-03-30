# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order, and the goal is to find the maximum possible number that can be formed. For example, if the input is [3, 30, 34, 5, 9], the output should be "9534330". The integers are non-negative and can be zero. The length of the input list can be up to 100.

## Approach
The approach is to use a custom comparator to sort the numbers based on their string representation. This comparator compares two numbers a and b by concatenating them in both orders (ab and ba) and checking which one is larger. The sorted list is then concatenated to form the largest possible number.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> str_nums;
        for (int num : nums) {
            str_nums.push_back(to_string(num));
        }
        
        // Custom comparator to sort the numbers
        sort(str_nums.begin(), str_nums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        
        // Concatenate the sorted numbers
        string result;
        for (const string& str : str_nums) {
            result += str;
        }
        
        // Remove leading zeros if any
        if (result[0] == '0') {
            return "0";
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [3, 30, 34, 5, 9]
Output: "9534330"
Input: [10, 7, 76, 415]
Output: "77641510"
```

## Key Takeaways
- Use a custom comparator to sort the numbers based on their string representation.
- Concatenate the sorted numbers to form the largest possible number.
- Handle the case where the largest possible number starts with zero.