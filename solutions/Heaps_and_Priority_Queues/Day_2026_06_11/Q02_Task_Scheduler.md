# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z. Each letter represents a different task. A task could be done one unit of time per execution. For each unit of time, CPU could complete one task or change the current task. The tasks array is given, return the least number of units of times that the CPU will take to finish all the given tasks. The tasks array can have duplicate tasks. For example, tasks = ["A","A","A","B","B","B"], n = 2, the output will be 8 because the CPU can execute the task in the following order: A -> B -> idle -> A -> B -> idle -> A -> B.

## Approach
The task scheduler problem can be solved by using a priority queue to store the frequency of tasks. We use a max heap to store the tasks, and then we pop the task with the highest frequency from the heap, decrease its frequency by 1, and push it back into the heap after a certain number of idle time units. This approach ensures that we are always executing the task with the highest frequency.

## Complexity
- Time: O(n log k)
- Space: O(k)

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
        
        int time = 0;
        while (!maxHeap.empty()) {
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
                if (i == n) {
                    for (int t : temp) {
                        maxHeap.push(t);
                    }
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
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
```

## Key Takeaways
- The problem can be solved using a priority queue to store the frequency of tasks.
- We need to consider the idle time units when scheduling the tasks.
- The time complexity is O(n log k) where n is the number of tasks and k is the number of unique tasks.