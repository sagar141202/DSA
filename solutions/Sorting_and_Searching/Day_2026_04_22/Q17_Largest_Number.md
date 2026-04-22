# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order, and the goal is to find the arrangement that yields the maximum possible number. For example, given the list [3, 30, 34, 5, 9], the largest possible number is 9534330. The list can contain up to 100 integers, each ranging from 0 to 10^9.

## Approach
The algorithm involves using a custom comparator to sort the list of integers. This comparator compares two numbers based on their concatenated values. If the concatenation of a with b is greater than the concatenation of b with a, then a should come before b in the sorted list. This approach ensures that the largest possible number is formed.

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
        
        // Custom comparator for sorting
        sort(strNums.begin(), strNums.end(), [](string a, string b) {
            return a + b > b + a;
        });
        
        // Handle the case where the largest number is 0
        if (strNums[0] == "0") {
            return "0";
        }
        
        string result;
        for (string str : strNums) {
            result += str;
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
- The custom comparator is crucial in sorting the integers to form the largest possible number.
- Handling the edge case where the largest number is 0 is essential to avoid incorrect results.
- The time complexity of O(n log n) is due to the sorting operation, where n is the number of integers in the input list.