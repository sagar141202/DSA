# Top K Frequent Elements

## Problem Statement
Given a non-empty array of integers, return the k most frequent elements. The answer should be sorted in descending order of frequency, and if two elements have the same frequency, they should be sorted in ascending order of value. For example, given the array [1,1,1,2,2,3] and k = 2, the output should be [1,2]. If k = 3, the output should be [1,2,3]. The constraints are 1 <= nums.length <= 10^5 and k is in the range [1, Number of unique elements in the array].

## Approach
We can use an unordered_map to store the frequency of each element, then use a priority_queue to store the top k frequent elements. The priority_queue will be sorted based on the frequency of the elements and their values.

## Complexity
- Time: O(N log k)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Store the frequency of each element
        unordered_map<int, int> frequency;
        for (int num : nums) {
            frequency[num]++;
        }

        // Use a priority_queue to store the top k frequent elements
        priority_queue<pair<int, int>> maxHeap;
        for (auto& pair : frequency) {
            maxHeap.push({pair.second, pair.first});
        }

        // Get the top k frequent elements
        vector<int> result;
        while (k-- > 0) {
            result.push_back(maxHeap.top().second);
            maxHeap.pop();
        }

        return result;
    }
};
```

## Test Cases
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Input: nums = [1,1,1,2,2,3], k = 3
Output: [1,2,3]
```

## Key Takeaways
- Use an unordered_map to store the frequency of each element for efficient lookup and update.
- Use a priority_queue to store the top k frequent elements, sorted based on frequency and value.
- The time complexity is O(N log k) due to the use of the priority_queue, where N is the number of unique elements.