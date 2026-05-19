# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order, and each integer can only be used once. For example, given the integers [3, 30, 34, 5, 9], the largest possible number that can be formed is 9534330. The input list will contain at most 100 integers, each of which is at most 10 digits long.

## Approach
The solution involves sorting the list of integers based on a custom comparison function that compares two integers concatenated in both possible orders. This comparison function determines which integer should come first in the sorted list to form the largest possible number. The sorted list is then concatenated to form the largest possible number.

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

        // Sort the list of strings based on a custom comparison function
        sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });

        // Concatenate the sorted list of strings to form the largest possible number
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
- Custom comparison functions can be used to sort lists of objects based on specific criteria.
- Concatenating strings in both possible orders and comparing them can help determine the correct order for forming the largest possible number.
- Leading zeros should be removed from the result if present, as they do not contribute to the value of the number.