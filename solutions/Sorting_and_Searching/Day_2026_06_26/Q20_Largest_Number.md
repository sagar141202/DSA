# Largest Number

## Problem Statement
Given a list of non-negative integers, arrange them such that they form the largest possible number. The integers can be concatenated together to form a single number. For example, if the input is [3, 30, 34, 5, 9], the output should be "9534330". The input list will contain at least one element and at most 100 elements, and each element will be between 0 and 1000.

## Approach
The approach to solve this problem is to use a custom comparator to sort the list of numbers. The comparator will compare two numbers based on which one will result in a larger number when concatenated with the other. This way, the numbers that will result in the largest possible number will be placed first in the sorted list.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool compare(string a, string b) {
    // compare a + b and b + a to determine which one is larger
    return (a + b) > (b + a);
}

string largestNumber(vector<int>& nums) {
    vector<string> strNums;
    // convert all numbers to strings
    for (int num : nums) {
        strNums.push_back(to_string(num));
    }
    // sort the list of strings using the custom comparator
    sort(strNums.begin(), strNums.end(), compare);
    // concatenate all the strings to form the largest possible number
    string result;
    for (string str : strNums) {
        result += str;
    }
    // if the result starts with 0, return "0"
    if (result[0] == '0') {
        return "0";
    }
    return result;
}

int main() {
    vector<int> nums = {3, 30, 34, 5, 9};
    cout << largestNumber(nums) << endl;
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
- Use a custom comparator to sort the list of numbers based on which one will result in a larger number when concatenated with the other.
- Convert all numbers to strings to easily concatenate them.
- Check if the result starts with 0 to handle the case where the input list contains only zeros.