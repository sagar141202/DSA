# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated to form a new number. For example, given the list [3, 30, 34, 5, 9], the largest possible number that can be formed is 9534330. The list can contain duplicate integers and can be empty. If the list is empty, return an empty string. If the list contains only zeros, return "0".

## Approach
The idea is to sort the list of integers based on a custom comparator that compares two integers concatenated in both orders. This comparator checks which order results in a larger number. The sorted list is then concatenated to form the largest possible number.

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
        
        // Sort the list based on a custom comparator
        sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        
        // Concatenate the sorted list to form the largest possible number
        string result;
        for (const string& str : strNums) {
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
Input: [0, 0, 0]
Output: "0"
Input: []
Output: ""
```

## Key Takeaways
- Custom comparator is used to compare two integers concatenated in both orders.
- Sorting the list based on this comparator ensures that the largest possible number is formed.
- Leading zeros are removed from the result if any.