# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. The constraints are: `1 <= s.length <= 10^5`, `1 <= t.length <= 10^5`, and the strings only contain lowercase English letters.

## Approach
The solution uses the sliding window technique with the help of two pointers and a hashmap to track the frequency of characters in `t`. We maintain a window in `s` and expand it to the right until we cover all characters of `t`, then try to shrink the window from the left while still covering all characters of `t`. This approach allows us to find the minimum window efficiently.

## Complexity
- Time: O(|s| + |t|)
- Space: O(|t|)

## C++ Solution
```cpp
#include <iostream>
#include <string>
#include <unordered_map>

string minWindow(string s, string t) {
    if (s.length() < t.length()) return "";
    
    unordered_map<char, int> tCount;
    for (char c : t) tCount[c]++;
    
    int required = tCount.size();
    int formed = 0;
    
    unordered_map<char, int> windowCounts;
    int ans = INT_MAX, start = 0, end = 0;
    
    int left = 0;
    for (int right = 0; right < s.length(); right++) {
        char c = s[right];
        windowCounts[c]++;
        
        if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) formed++;
        
        while (left <= right && formed == required) {
            c = s[left];
            
            if (right - left + 1 < ans) {
                ans = right - left + 1;
                start = left;
                end = right;
            }
            
            windowCounts[c]--;
            if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) formed--;
            
            left++;
        }
    }
    
    return ans == INT_MAX ? "" : s.substr(start, end - start + 1);
}

int main() {
    string s = "ADOBECODEBANC";
    string t = "ABC";
    cout << minWindow(s, t) << endl;
    return 0;
}
```

## Test Cases
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Input: s = "a", t = "a"
Output: "a"
Input: s = "aa", t = "aa"
Output: "aa"
```

## Key Takeaways
- Use a hashmap to store the frequency of characters in `t`.
- Maintain a sliding window in `s` and expand it to the right until all characters of `t` are covered.
- Try to shrink the window from the left while still covering all characters of `t` to find the minimum window.