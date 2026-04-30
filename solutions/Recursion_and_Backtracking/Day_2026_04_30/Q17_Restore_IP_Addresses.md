# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255. The input string must not have any leading zeros, unless the number is zero itself. For example, the input "25525511135" can be restored as ["255.255.11.135", "255.255.111.35"].

## Approach
The solution uses backtracking to generate all possible combinations of four numbers from the input string. It checks each combination to ensure that it forms a valid IP address. The algorithm iterates over the string, creating substrings of lengths 1 to 3, and checks if they can be part of a valid IP address.

## Complexity
- Time: O(2^n * 4) where n is the length of the input string, as in the worst case, we might have to explore all possible substrings.
- Space: O(n) for storing the recursion stack and the current combination of numbers.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        vector<string> current;
        backtrack(s, 0, current, result);
        return result;
    }
    
    void backtrack(string& s, int start, vector<string>& current, vector<string>& result) {
        if (current.size() == 4) {
            if (start == s.size()) {
                string ip = current[0] + "." + current[1] + "." + current[2] + "." + current[3];
                result.push_back(ip);
            }
            return;
        }
        
        for (int i = 1; i <= 3; i++) {
            if (start + i > s.size()) break;
            string substr = s.substr(start, i);
            if ((substr.size() > 1 && substr[0] == '0') || stoi(substr) > 255) continue;
            current.push_back(substr);
            backtrack(s, start + i, current, result);
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
- The use of backtracking allows for efficient exploration of all possible combinations of IP addresses.
- The validation of each substring ensures that only valid IP addresses are included in the result.
- The algorithm's time complexity is dominated by the number of possible combinations, which can be large for long input strings.