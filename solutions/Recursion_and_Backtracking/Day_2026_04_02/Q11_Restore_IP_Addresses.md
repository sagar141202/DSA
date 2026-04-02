# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255. The input string must not have any leading zeros, unless the number is 0 itself. For example, "25525511135" can be restored as ["255.255.11.135", "255.255.111.35"].

## Approach
We will use backtracking to generate all possible combinations of IP addresses. The algorithm will iterate through the string, creating substrings of lengths 1 to 3, and checking if they can be valid IP address parts. If a valid combination is found, it will be added to the result list.

## Complexity
- Time: O(2^n * 4) where n is the length of the input string, as we are generating all possible combinations and checking each part of the IP address.
- Space: O(2^n * 4) for storing the result and the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        backtrack(result, s, 0, "");
        return result;
    }
    
    void backtrack(vector<string>& result, string s, int start, string current) {
        if (current.count('.') == 3) {
            if (start == s.size()) {
                result.push_back(current.substr(0, current.size() - 1));
            }
            return;
        }
        
        for (int i = 1; i <= 3; i++) {
            if (start + i > s.size()) break;
            string substr = s.substr(start, i);
            if ((substr.size() > 1 && substr[0] == '0') || stoi(substr) > 255) continue;
            backtrack(result, s, start + i, current + substr + ".");
        }
    }
};

int main() {
    Solution solution;
    string input = "25525511135";
    vector<string> result = solution.restoreIpAddresses(input);
    for (string ip : result) {
        cout << ip << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
Input: "0000"
Output: ["0.0.0.0"]
Input: "101023"
Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
```

## Key Takeaways
- Use backtracking to generate all possible combinations of IP addresses.
- Check each part of the IP address to ensure it is valid (between 0 and 255, no leading zeros unless the number is 0).
- Use recursion to explore all possible combinations of IP addresses.