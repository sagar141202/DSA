# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z. The different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could complete one task or just be idle. However, there is a constraint that at any moment, two same tasks should have at least n intervals. You need to return the least number of intervals the CPU will take to finish all the tasks. For example, if tasks = ['A','A','A','B','B','B'], n = 2, then the output will be 8 because the optimal schedule is 'A' -> idle -> 'B' -> idle -> 'A' -> idle -> 'B' -> idle -> 'A' -> 'B'.

## Approach
The problem can be solved using a priority queue and a hash map to store the frequency of each task. We use a max heap to store the tasks with the highest frequency. The algorithm works by scheduling the task with the highest frequency first and then adding it back to the queue after n intervals.

## Complexity
- Time: O(N log 26)
- Space: O(26)

## C++ Solution
```cpp
#include <queue>
#include <unordered_map>
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
        
        int intervals = 0;
        while (!maxHeap.empty()) {
            vector<int> temp;
            for (int i = 0; i <= n; i++) {
                if (!maxHeap.empty()) {
                    temp.push_back(maxHeap.top() - 1);
                    maxHeap.pop();
                }
                intervals++;
            }
            for (int task : temp) {
                if (task > 0) {
                    maxHeap.push(task);
                }
            }
            if (maxHeap.empty()) {
                break;
            }
            intervals += n - temp.size() + 1;
        }
        return intervals;
    }
};
```

## Test Cases
```
Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Input: tasks = ['A','A','A','B','B','B'], n = 0
Output: 6
```

## Key Takeaways
- Use a priority queue to store tasks with the highest frequency.
- Use a hash map to store the frequency of each task.
- Schedule the task with the highest frequency first and add it back to the queue after n intervals.