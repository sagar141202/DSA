# Task Scheduler

## Problem Statement
Given a list of tasks and a cool-down period `n`, schedule the tasks such that no two same tasks are executed within `n` time units of each other. The task scheduler should execute the tasks as soon as possible. The function should return the least number of time units required to execute all tasks. For example, given tasks `["A","A","A","B","B","B"]` and `n = 2`, the function should return `8` because the optimal schedule is `"A" -> "B" -> idle -> "A" -> "B" -> idle -> "A" -> "B"`.

## Approach
We use a max-heap to store the frequency of each task and a queue to store the tasks that are cooling down. The max-heap ensures that the task with the highest frequency is executed first. The queue ensures that the tasks that are cooling down are executed after the cool-down period.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        // Create a frequency map
        unordered_map<char, int> freq;
        for (char task : tasks) {
            freq[task]++;
        }
        
        // Create a max-heap
        priority_queue<int> maxHeap;
        for (auto& it : freq) {
            maxHeap.push(it.second);
        }
        
        int time = 0;
        while (!maxHeap.empty()) {
            // Dequeue n+1 tasks
            vector<int> temp;
            for (int i = 0; i <= n; i++) {
                if (!maxHeap.empty()) {
                    temp.push_back(maxHeap.top() - 1);
                    maxHeap.pop();
                }
            }
            
            // Add the tasks back to the max-heap if their frequency is greater than 0
            for (int i : temp) {
                if (i > 0) {
                    maxHeap.push(i);
                }
            }
            
            // Increment the time by n+1 if the max-heap is not empty, otherwise increment by the number of tasks in the temp vector
            time += maxHeap.empty() ? temp.size() : n + 1;
        }
        
        return time;
    }
};
```

## Test Cases
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
```

## Key Takeaways
- Use a max-heap to store the frequency of each task to ensure that the task with the highest frequency is executed first.
- Use a queue to store the tasks that are cooling down to ensure that the tasks are executed after the cool-down period.
- The time complexity is O(n log k) where n is the number of tasks and k is the number of unique tasks.