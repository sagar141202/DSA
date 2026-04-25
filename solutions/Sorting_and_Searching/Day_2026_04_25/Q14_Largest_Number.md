# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The numbers can be concatenated in any order, but each number must be used exactly once. For example, if the input is [3, 6, 9], the output should be "963". If the input is [10, 7, 76, 415], the output should be "77641510". The input list will have at most 100 elements, and each element will be at most 10 digits long.

## Approach
The algorithm involves sorting the list of numbers as strings in descending order, but with a custom comparison function that compares two numbers based on which one would result in a larger number when concatenated. This ensures that the numbers are ordered in a way that maximizes the resulting concatenated number.

## Complexity
- Time: O(N log N)
- Space: O(N)

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
        
        // Custom comparison function for sorting
        sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        
        // Handle the case where all numbers are 0
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
- Custom comparison functions can be used with the `sort` function in C++ to sort objects based on specific criteria.
- When dealing with numbers as strings, concatenation can be used to compare them in a way that takes into account their numerical value.
- Handling edge cases, such as when all numbers are 0, is crucial to ensure the correctness of the solution.