# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z. Each letter represents a different task. A task could be done one time in n time units, where n is the cooling time of the task. The tasks are scheduled such that the same tasks are at least n time units apart. We need to find the least number of time units to schedule all tasks. For example, if we have tasks = ["A","A","A","B","B","B"], n = 2, then the least time units required will be 8, which can be achieved as "ABABABAB" or other similar sequences.

## Approach
We use a max heap to store the frequency of each task and schedule the tasks with the highest frequency first. The max heap ensures that the tasks with the highest frequency are executed as soon as possible, thus minimizing the total time units required.

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
        // Create a frequency map for tasks
        unordered_map<char, int> freq;
        for (char task : tasks) {
            freq[task]++;
        }

        // Create a max heap to store task frequencies
        priority_queue<int> maxHeap;
        for (auto& pair : freq) {
            maxHeap.push(pair.second);
        }

        int time = 0;
        while (!maxHeap.empty()) {
            // Store the tasks to be executed in the current cycle
            vector<int> temp;
            for (int i = 0; i <= n; i++) {
                if (!maxHeap.empty()) {
                    if (maxHeap.top() > 1) {
                        temp.push_back(maxHeap.top() - 1);
                    }
                    maxHeap.pop();
                }
                time++;
                if (maxHeap.empty() && temp.empty()) {
                    break;
                }
            }

            // Add the tasks back to the max heap
            for (int freq : temp) {
                maxHeap.push(freq);
            }
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
- Use a max heap to prioritize tasks with the highest frequency.
- Schedule tasks in cycles to ensure the cooling time is respected.
- The time complexity is O(n log k), where n is the number of tasks and k is the number of unique tasks.