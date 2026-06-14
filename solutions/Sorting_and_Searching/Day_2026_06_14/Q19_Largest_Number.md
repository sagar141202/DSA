# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers may have varying numbers of digits and may contain leading zeros. The goal is to find the largest number that can be formed by concatenating the given integers. For example, if the input is [3, 30, 34, 5, 9], the output should be "9534330".

## Approach
The approach involves sorting the numbers as strings in descending order, but with a custom comparison function that considers the concatenation of two numbers. This function compares the concatenation of two numbers in both orders and returns the order that produces the larger result. The sorted numbers are then concatenated to form the largest possible number.

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
        // Convert integers to strings for easy concatenation
        vector<string> strNums;
        for (int num : nums) {
            strNums.push_back(to_string(num));
        }
        
        // Sort the strings using a custom comparison function
        sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        
        // Concatenate the sorted strings to form the largest number
        string result;
        for (const string& str : strNums) {
            result += str;
        }
        
        // Remove leading zeros if present
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
- Custom sorting is necessary to achieve the desired order of concatenation.
- The comparison function should consider both orders of concatenation to determine the correct order.
- Removing leading zeros is essential to handle cases where the input contains only zeros.