# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order to form the largest number. For example, if the input is [3, 6, 9], the output should be "963" because 963 is the largest number that can be formed by concatenating these integers. The input list will contain at least one integer and at most 100 integers, each of which is at most 10 digits long.

## Approach
The problem can be solved by sorting the integers based on a custom comparison function that compares two integers as if they were concatenated. This comparison function should return true if the concatenation of the first integer with the second is larger than the concatenation of the second with the first. The sorted integers can then be concatenated to form the largest possible number.

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
        
        // Concatenate the sorted strings
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
Input: [3, 6, 9]
Output: "963"
Input: [10, 7, 76, 415]
Output: "77641510"
```

## Key Takeaways
- The custom comparison function is crucial for sorting the integers based on their concatenated values.
- The solution handles the case where the input list contains only zeros by returning "0" as the largest possible number.