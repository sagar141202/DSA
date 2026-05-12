# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do, where different letters represent different tasks. The length of the array is n. The CPU can only perform one task at a time. In one second, the CPU can complete one task. At any moment, the CPU can choose any task from the task list and start a 1-second timer. Once the timer goes off, the CPU can choose another task from the task list and reset the timer. The task list is given as a string of characters, and the CPU needs to find the least number of units of time that the CPU will take to finish all the given tasks, assuming that the CPU can't perform a task until the cooling period of the previous task is over. The cooling period of a task is n units of time, where n is the number of different tasks in the task list.

## Approach
The approach to solve this problem is to use a priority queue to store the frequency of each task and then use a greedy algorithm to schedule the tasks. We can calculate the maximum frequency of any task and the number of tasks with that frequency, and then use these values to calculate the minimum time required to finish all tasks.

## Complexity
- Time: O(n log n)
- Space: O(n)

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
        for (auto& it : count) {
            maxHeap.push(it.second);
        }

        int time = 0;
        while (!maxHeap.empty()) {
            int i = 0;
            vector<int> temp;
            while (i <= n) {
                if (!maxHeap.empty()) {
                    if (maxHeap.top() > 1) {
                        temp.push_back(maxHeap.top() - 1);
                    }
                    maxHeap.pop();
                }
                time++;
                if (i == n && !maxHeap.empty() && temp.size() == 0) {
                    time++;
                }
                i++;
            }
            for (int t : temp) {
                maxHeap.push(t);
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
- The priority queue is used to store the frequency of each task.
- The time complexity of the solution is O(n log n) due to the use of the priority queue.
- The space complexity of the solution is O(n) for storing the frequency of each task.