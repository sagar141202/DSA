# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z. Each letter represents a different task. Tasks could be done without original order. Each task could be done one time at least. CPU could complete one task per "quantom". For a given CPU quatum `n`, how many "quantom"s we need to complete all tasks.

## Approach
We use a max heap to store the frequency of each task and a queue to store the tasks that are waiting to be executed. The max heap ensures that the task with the highest frequency is executed first. We iterate through the tasks, push them into the max heap, and then pop the tasks from the max heap and push them into the queue.

## Complexity
- Time: O(N log K)
- Space: O(K)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> count;
        for (char task : tasks) {
            count[task]++;
        }
        
        priority_queue<int> maxHeap;
        for (auto& pair : count) {
            maxHeap.push(pair.second);
        }
        
        int time = 0;
        queue<pair<int, int>> q;
        while (!maxHeap.empty() || !q.empty()) {
            if (!maxHeap.empty()) {
                int freq = maxHeap.top();
                maxHeap.pop();
                if (freq > 1) {
                    q.push({freq - 1, n});
                }
            }
            if (!q.empty()) {
                auto& pair = q.front();
                if (pair.second > 1) {
                    pair.second--;
                } else {
                    maxHeap.push(pair.first);
                    q.pop();
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
```

## Key Takeaways
- Use a max heap to store the frequency of each task
- Use a queue to store the tasks that are waiting to be executed
- Iterate through the tasks, push them into the max heap, and then pop the tasks from the max heap and push them into the queue.