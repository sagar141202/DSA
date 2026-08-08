# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order to form the largest number. For example, if the input is [3, 30, 34, 5, 9], the output should be "9534330". The integers are in the range [0, 10^9] and the length of the input list is between 1 and 100.

## Approach
The approach is to use a custom comparator to sort the numbers based on their concatenated values. The idea is to compare two numbers a and b by concatenating them in both orders (ab and ba) and comparing the results. The algorithm sorts the numbers in descending order based on this comparison.

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
        
        // Custom comparator to sort the numbers based on their concatenated values
        sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
            return a + b > b + a;
        });
        
        // If the largest number is 0, return "0"
        if (strNums[0] == "0") {
            return "0";
        }
        
        // Concatenate the sorted numbers to form the largest possible number
        string largestNum;
        for (const string& num : strNums) {
            largestNum += num;
        }
        
        return largestNum;
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
- Use a custom comparator to sort the numbers based on their concatenated values.
- Handle the case where the largest number is 0 by checking if the first number in the sorted list is "0".
- Concatenate the sorted numbers to form the largest possible number.