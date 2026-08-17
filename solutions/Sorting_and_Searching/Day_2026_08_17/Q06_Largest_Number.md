# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order, and the goal is to find the arrangement that results in the maximum possible number. For example, given the list [3, 30, 34, 5, 9], the largest possible number that can be formed is 9534330. The list can contain up to 100 integers, each with a maximum value of 10^9.

## Approach
The approach involves sorting the list of numbers based on a custom comparator that compares the concatenation of two numbers in both orders. This ensures that the numbers are arranged in a way that maximizes the resulting number. The sorted list is then concatenated to form the largest possible number.

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
        
        // Custom comparator for sorting
        sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        
        // Concatenate the sorted strings
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

int main() {
    Solution solution;
    vector<int> nums = {3, 30, 34, 5, 9};
    cout << solution.largestNumber(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: [3, 30, 34, 5, 9]
Output: 9534330
Input: [10, 7, 76, 415]
Output: 77641510
```

## Key Takeaways
- Custom comparators can be used to sort objects based on specific conditions.
- Concatenating strings in different orders can result in different outcomes, and the correct order can be determined using a custom comparator.
- Leading zeros should be handled separately to avoid incorrect results.