# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated in any order, and the goal is to find the arrangement that yields the maximum possible number. For example, given the list [3, 30, 34, 5, 9], the largest possible number is 9534330. The list can contain up to 100 integers, each with up to 10 digits.

## Approach
The problem is solved by using a custom comparator to sort the numbers. The comparator compares two numbers based on their concatenated values. If the concatenation of a with b is larger than the concatenation of b with a, then a should come before b in the sorted list. This approach ensures that the largest possible number is formed.

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
        
        sort(strNums.begin(), strNums.end(), [](string a, string b) {
            return a + b > b + a;
        });
        
        string result = "";
        for (string str : strNums) {
            result += str;
        }
        
        // Remove leading zeros if any
        while (result.size() > 1 && result[0] == '0') {
            result.erase(0, 1);
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
- The custom comparator is the key to solving this problem, as it allows us to sort the numbers based on their concatenated values.
- The use of string concatenation to compare numbers is an efficient way to solve the problem, as it avoids the need for explicit numerical comparisons.
- The solution has a time complexity of O(n log n) due to the sorting operation, where n is the number of integers in the input list.