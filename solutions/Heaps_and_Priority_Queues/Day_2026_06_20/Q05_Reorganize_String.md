# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is impossible to reorganize the string, return an empty string. The string consists of lowercase English letters and has a length of at most 100. For example, given the string "aab", the output should be "aba" because no two adjacent characters are the same. However, given the string "aaab", the output should be an empty string because it is impossible to reorganize the string.

## Approach
The approach to solve this problem is to use a max heap to store the frequency of each character. We then pop the two most frequent characters from the heap and append them to the result string. This process is repeated until the heap is empty or it is impossible to reorganize the string.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string reorganizeString(string s) {
        // Create a frequency map
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        // Create a max heap
        priority_queue<pair<int, char>> maxHeap;
        for (auto &it : freq) {
            maxHeap.push({it.second, it.first});
        }

        // Initialize the result string
        string result;
        while (!maxHeap.empty()) {
            // Pop the two most frequent characters from the heap
            pair<int, char> first = maxHeap.top();
            maxHeap.pop();
            if (result.size() > 0 && result.back() == first.second) {
                if (maxHeap.empty()) {
                    return "";
                }
                pair<int, char> second = maxHeap.top();
                maxHeap.pop();
                result.push_back(second.second);
                if (second.first > 1) {
                    maxHeap.push({second.first - 1, second.second});
                }
                maxHeap.push(first);
            } else {
                result.push_back(first.second);
                if (first.first > 1) {
                    maxHeap.push({first.first - 1, first.second});
                }
            }
        }

        return result;
    }
};
```

## Test Cases
```
Input: "aab"
Output: "aba"
Input: "aaab"
Output: ""
```

## Key Takeaways
- Use a max heap to store the frequency of each character.
- Pop the two most frequent characters from the heap and append them to the result string.
- Check if the last character in the result string is the same as the most frequent character, and if so, pop the next most frequent character from the heap.