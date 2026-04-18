# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string must not have any leading zeros, unless the number is zero itself. For example, "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
The solution uses backtracking to generate all possible combinations of four numbers from the input string. It checks each combination to ensure it forms a valid IP address. The algorithm iterates over the string, creating substrings of lengths 1 to 3, and checks if they can be part of a valid IP address.

## Complexity
- Time: O(3^N * 4) where N is the length of the string, as in the worst case, we might have to consider all possible substrings of lengths 1 to 3 for each of the four parts of the IP address.
- Space: O(N) for storing the current combination and the result.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        backtrack(result, s, 0, {});
        return result;
    }
    
    void backtrack(vector<string>& result, string& s, int start, vector<string>& current) {
        if (current.size() == 4) {
            if (start == s.size()) {
                string ip = current[0];
                for (int i = 1; i < 4; i++) {
                    ip += "." + current[i];
                }
                result.push_back(ip);
            }
            return;
        }
        
        for (int i = 1; i <= 3; i++) {
            if (start + i > s.size()) break;
            string substr = s.substr(start, i);
            if ((substr[0] == '0' && substr.size() > 1) || stoi(substr) > 255) continue;
            current.push_back(substr);
            backtrack(result, s, start + i, current);
            current.pop_back();
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
- Use backtracking to generate all possible combinations of four numbers from the input string.
- Ensure each combination forms a valid IP address by checking for leading zeros and number range.
- Use recursion to explore all possible combinations efficiently.