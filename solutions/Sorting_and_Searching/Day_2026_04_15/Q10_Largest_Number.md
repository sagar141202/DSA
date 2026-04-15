# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order, and the goal is to find the arrangement that yields the maximum value. For example, given the list [3, 30, 34, 5, 9], the largest possible number is 9534330. The input list will contain at most 100 integers, each with a maximum value of 1000.

## Approach
The algorithm involves sorting the list of integers as strings in descending order, with a custom comparison function that compares the concatenation of two numbers in both orders. This approach ensures that the numbers are arranged to form the largest possible value. The sorted list is then concatenated to form the final result.

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
        
        // Custom comparison function for sorting
        sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        
        // Concatenate the sorted list to form the result
        string result;
        for (const string& str : strNums) {
            result += str;
        }
        
        // Handle the case where the result starts with 0
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
- The custom comparison function is used to sort the list of integers as strings in descending order.
- The sorting approach ensures that the numbers are arranged to form the largest possible value.
- The result is concatenated from the sorted list, and a special case is handled where the result starts with 0.