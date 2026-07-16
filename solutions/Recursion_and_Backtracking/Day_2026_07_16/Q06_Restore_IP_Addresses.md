# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string must not have any leading zeros, unless the number is zero itself. For example, given the string "25525511135", the output should be ["255.255.11.135", "255.255.111.35"].

## Approach
We will use a backtracking approach to solve this problem, generating all possible combinations of four numbers and checking if they form a valid IP address. We will iterate over the string, creating all possible substrings that could represent a valid IP segment.

## Complexity
- Time: O(2^n * 4) where n is the length of the input string, as we are generating all possible combinations
- Space: O(n) for the recursion stack and storing the result

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
    
    void backtrack(vector<string>& result, string& s, int start, string current) {
        if (current.count('.') == 3) {
            if (start == s.size()) {
                result.push_back(current.substr(0, current.size() - 1)); // remove the extra dot
            }
            return;
        }
        
        for (int i = 1; i <= 3; i++) {
            if (start + i > s.size()) break;
            string segment = s.substr(start, i);
            if ((segment.size() > 1 && segment[0] == '0') || stoi(segment) > 255) continue;
            backtrack(result, s, start + i, current + segment + ".");
        }
    }
};

int main() {
    Solution solution;
    string input = "25525511135";
    vector<string> result = solution.restoreIpAddresses(input);
    for (const auto& ip : result) {
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
- We use backtracking to generate all possible IP address combinations.
- We check each segment to ensure it's a valid IP segment (between 0 and 255, no leading zeros unless it's zero itself).
- We use recursion to explore all possible combinations of four numbers.