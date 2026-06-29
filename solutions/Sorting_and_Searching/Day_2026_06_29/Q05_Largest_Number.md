# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order to form the largest number. For example, if the input is [3, 30, 34, 5, 9], the output should be "9534330". The input list will contain at most 100 integers, and each integer will be at most 10 digits long.

## Approach
The approach is to sort the list of numbers based on a custom comparison function that compares two numbers as if they were concatenated. This custom comparison function will ensure that the numbers are arranged in the order that will produce the largest possible number. The sorted list is then concatenated to form the largest number.

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
        // Convert integers to strings for easy concatenation
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
Output: "9534330"
Input: [10, 7, 76, 415]
Output: "77641510"
```

## Key Takeaways
- The custom comparison function is the key to solving this problem, as it ensures that the numbers are arranged in the order that will produce the largest possible number.
- The use of strings for representing numbers allows for easy concatenation and comparison.
- The solution has a time complexity of O(N log N) due to the sorting operation, where N is the number of input integers.