# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated together to form a new number. For example, given the list [3, 6, 9], the largest possible number that can be formed is 963. The list can contain duplicate integers and can be empty. If the list is empty, return an empty string. If the list contains only zeros, return "0".

## Approach
The problem can be solved by using a custom comparator to sort the list of integers. The comparator compares two integers based on their concatenated values. If the concatenated value of the first integer with the second integer is greater than the concatenated value of the second integer with the first integer, then the first integer is considered larger.

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
        vector<string> strNums;
        for (int num : nums) {
            strNums.push_back(to_string(num));
        }
        
        // Custom comparator to sort the list of integers
        sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        
        // If the list contains only zeros, return "0"
        if (strNums[0] == "0") {
            return "0";
        }
        
        string result;
        for (const string& str : strNums) {
            result += str;
        }
        
        return result;
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
- Use a custom comparator to sort the list of integers based on their concatenated values.
- Handle the edge case where the list contains only zeros.
- Use the `to_string` function to convert integers to strings for concatenation.