# Task Scheduler

## Problem Statement
Given a list of tasks and a cooling period, schedule the tasks such that no two same tasks are scheduled within the cooling period. The tasks are represented by characters and the cooling period is an integer. The function should return the least number of time units required to schedule all tasks. For example, given tasks = ["A", "A", "A", "B", "B", "B"] and a cooling period of 2, the function should return 8 because the schedule would be "A -> B -> idle -> A -> B -> idle -> A -> B".

## Approach
The algorithm uses a max heap to store the frequency of each task and a queue to store the tasks that are cooling down. The max heap is used to select the task with the highest frequency to schedule next. The queue is used to store the tasks that are cooling down and to ensure that no two same tasks are scheduled within the cooling period.

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
        // Create a frequency map of tasks
        unordered_map<char, int> freq;
        for (char task : tasks) {
            freq[task]++;
        }
        
        // Create a max heap to store the frequency of each task
        priority_queue<int> maxHeap;
        for (auto& it : freq) {
            maxHeap.push(it.second);
        }
        
        int time = 0;
        while (!maxHeap.empty()) {
            // Create a queue to store the tasks that are cooling down
            queue<pair<int, int>> q;
            int i = 0;
            while (i <= n) {
                if (!maxHeap.empty()) {
                    int freq = maxHeap.top();
                    maxHeap.pop();
                    if (freq > 1) {
                        q.push({freq - 1, i + n});
                    }
                }
                time++;
                if (!q.empty() && q.front().second == i) {
                    maxHeap.push(q.front().first);
                    q.pop();
                }
                if (maxHeap.empty() && q.empty()) {
                    break;
                }
                i++;
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
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
```

## Key Takeaways
- The use of a max heap to store the frequency of each task allows us to schedule the tasks with the highest frequency first.
- The use of a queue to store the tasks that are cooling down ensures that no two same tasks are scheduled within the cooling period.
- The time complexity of the solution is O(n log n) due to the use of the max heap.