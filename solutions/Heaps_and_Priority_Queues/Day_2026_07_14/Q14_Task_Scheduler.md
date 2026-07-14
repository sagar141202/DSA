# Task Scheduler

## Problem Statement
Given a list of tasks and a cooldown period, schedule the tasks such that no two same tasks are executed within the cooldown period. The tasks are represented by characters, and the cooldown period is given by an integer. The goal is to find the least number of time units required to schedule all tasks. For example, given tasks = ["A","A","A","B","B","B"], n = 2, the output should be 8, because one possible schedule is "ABABABCA", where "C" represents an idle time unit.

## Approach
We use a priority queue to store the tasks along with their frequencies. The task with the highest frequency is scheduled first. If a task is scheduled, it is added back to the priority queue after the cooldown period. We also use a queue to store the tasks that are in the cooldown period.

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
        for (char c : tasks) {
            freq[c]++;
        }
        
        priority_queue<int> pq;
        for (auto& it : freq) {
            pq.push(it.second);
        }
        
        int time = 0;
        while (!pq.empty()) {
            int i = 0;
            queue<pair<int, int>> q;
            while (i <= n) {
                if (!pq.empty()) {
                    int count = pq.top();
                    pq.pop();
                    count--;
                    if (count > 0) {
                        q.push({count, i + n});
                    }
                }
                time++;
                i++;
                if (!q.empty() && q.front().second == i) {
                    pq.push(q.front().first);
                    q.pop();
                }
                if (pq.empty() && q.empty()) {
                    break;
                }
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
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
```

## Key Takeaways
- Use a priority queue to store tasks based on their frequencies
- Use a queue to store tasks that are in the cooldown period
- Schedule the task with the highest frequency first and add it back to the priority queue after the cooldown period