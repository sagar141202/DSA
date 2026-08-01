# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is not possible to reorganize the string, return an empty string. The string consists of lowercase English letters and the length of the string is in the range [1, 50000]. For example, given the string "aab", the function should return "aba" because no two adjacent characters are the same. However, given the string "aaab", the function should return an empty string because it is not possible to reorganize the string.

## Approach
We can use a max heap to store the frequency of each character in the string. The max heap will allow us to always choose the character with the highest frequency to add to the result string. By using a max heap, we can ensure that no two adjacent characters are the same.

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
        for (auto& it : freq) {
            maxHeap.push({it.second, it.first});
        }

        // Initialize the result string
        string result;
        while (!maxHeap.empty()) {
            // Get the character with the highest frequency
            pair<int, char> first = maxHeap.top();
            maxHeap.pop();

            // If the result string is not empty and the last character is the same as the current character
            if (!result.empty() && result.back() == first.second) {
                // If the max heap is empty, return an empty string
                if (maxHeap.empty()) {
                    return "";
                }

                // Get the character with the next highest frequency
                pair<int, char> second = maxHeap.top();
                maxHeap.pop();

                // Add the character with the next highest frequency to the result string
                result += second.second;

                // Decrement the frequency of the character with the next highest frequency
                second.first--;

                // If the frequency of the character with the next highest frequency is greater than 0, push it back to the max heap
                if (second.first > 0) {
                    maxHeap.push(second);
                }

                // Push the character with the highest frequency back to the max heap
                maxHeap.push(first);
            } else {
                // Add the character with the highest frequency to the result string
                result += first.second;

                // Decrement the frequency of the character with the highest frequency
                first.first--;

                // If the frequency of the character with the highest frequency is greater than 0, push it back to the max heap
                if (first.first > 0) {
                    maxHeap.push(first);
                }
            }
        }

        return result;
    }
};

int main() {
    Solution solution;
    string s = "aab";
    cout << solution.reorganizeString(s) << endl;
    return 0;
}
```

## Test Cases
```
Input: "aab"
Output: "aba"

Input: "aaab"
Output: ""
```

## Key Takeaways
- Use a max heap to store the frequency of each character in the string.
- Always choose the character with the highest frequency to add to the result string.
- If the last character in the result string is the same as the current character, choose the character with the next highest frequency to add to the result string.