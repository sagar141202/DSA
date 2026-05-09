# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers (each between 0 and 255) separated by dots. The numbers cannot have leading zeros unless they are zero. For example, "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
The solution uses recursion and backtracking to generate all possible combinations of four numbers from the given string. It checks each combination to ensure it forms a valid IP address.

## Complexity
- Time: O(2^n * n) where n is the length of the string, as we are generating all possible combinations
- Space: O(n) for the recursion stack and storing the result

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        backtrack(result, "", s, 0, 0);
        return result;
    }
    
    void backtrack(vector<string>& result, string current, string& s, int start, int count) {
        if (count == 4) {
            if (start == s.size()) {
                result.push_back(current.substr(0, current.size() - 1));
            }
            return;
        }
        
        for (int i = 1; i <= 3; i++) {
            if (start + i > s.size()) break;
            string section = s.substr(start, i);
            if ((section.size() > 1 && section[0] == '0') || stoi(section) > 255) continue;
            backtrack(result, current + section + ".", s, start + i, count + 1);
        }
    }
};

## Test Cases
```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations of IP addresses
- Check each section of the IP address to ensure it is valid (between 0 and 255, no leading zeros unless zero)
- Use a helper function to perform the backtracking and validate each section of the IP address