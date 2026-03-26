# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order to form the largest number. For example, given the list [3, 6, 9], the largest possible number is 963. The list can contain duplicate numbers and can be empty. If the list is empty, return an empty string.

## Approach
The solution involves sorting the list of numbers as strings in descending order, but with a custom comparison function. This comparison function compares two numbers a and b by concatenating them in both orders (ab and ba) and checking which one is larger. The sorted list is then concatenated to form the largest possible number.

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
        
        // Sort the list of strings in descending order with custom comparison
        sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        
        // Concatenate the sorted list to form the largest number
        string largestNum;
        for (const string& str : strNums) {
            largestNum += str;
        }
        
        // If the largest number starts with 0, return "0"
        if (largestNum[0] == '0') {
            return "0";
        }
        
        return largestNum;
    }
};
```

## Test Cases
```
Input: [3, 6, 9]
Output: "963"
Input: [10, 7, 76, 415]
Output: "77641510"
Input: [0, 0, 0]
Output: "0"
```

## Key Takeaways
- Custom comparison function is used for sorting the list of numbers as strings.
- The comparison function checks which concatenation of two numbers is larger.
- The solution handles the case when the input list is empty or contains only zeros.