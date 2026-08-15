# Task Scheduler

## Problem Statement
Given a list of tasks and a cooling period, schedule the tasks such that the same task is not executed within the cooling period. The tasks are represented by characters, and the cooling period is an integer. The goal is to find the least number of units of time required to schedule all tasks. For example, given tasks = ["A","A","A","B","B","B"], n = 2, the output should be 8, as one possible scheduling is "ABABABAB".

## Approach
The approach involves using a max heap to store the frequency of each task and a queue to store the tasks that are currently in the cooling period. We iterate over the tasks, pushing them into the max heap and then popping the task with the highest frequency, scheduling it and pushing it into the queue. We then increment the time and check if the queue is not empty, if so, we pop the task from the queue and push it back into the max heap.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> freq;
        for (char task : tasks) {
            freq[task]++;
        }

        priority_queue<int> maxHeap;
        for (auto& pair : freq) {
            maxHeap.push(pair.second);
        }

        int time = 0;
        queue<pair<int, int>> q; // stores the task and its cooldown time

        while (!maxHeap.empty() || !q.empty()) {
            if (!maxHeap.empty()) {
                int count = maxHeap.top();
                maxHeap.pop();
                if (count > 1) {
                    q.push({count - 1, n});
                }
            }

            if (!q.empty()) {
                auto top = q.front();
                q.pop();
                if (top.second > 1) {
                    q.push({top.first, top.second - 1});
                } else if (top.first > 0) {
                    maxHeap.push(top.first);
                }
            }

            time++;
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
- Use a max heap to store the frequency of each task
- Use a queue to store the tasks that are currently in the cooling period
- Increment the time and check if the queue is not empty to ensure the cooling period is respected