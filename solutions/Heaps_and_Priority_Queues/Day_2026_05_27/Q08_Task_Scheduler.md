# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do, where different letters represent different tasks. The length of the array is n. At any moment, the CPU could complete the task or change the task. The task scheduler will schedule the task in such a way that the same task cannot be done two times in a row. Given a cooldown period of size k, determine the least number of units of time that the CPU will take to finish all tasks with the constraint that the same task cannot be done two times in a row and there is a cooldown period.

## Approach
We can use a priority queue to store the frequency of each task. We will pop the task with the highest frequency from the queue and add it to the result. If the same task is popped consecutively, we will add a cooldown period.

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
        unordered_map<char, int> count;
        for (char task : tasks) {
            count[task]++;
        }

        int maxFreq = 0;
        int maxCount = 0;
        for (auto& pair : count) {
            maxFreq = max(maxFreq, pair.second);
            if (pair.second == maxFreq) {
                maxCount++;
            }
        }

        int ans = (maxFreq - 1) * (n + 1) + maxCount;
        return max((int)tasks.size(), ans);
    }
};

int main() {
    Solution solution;
    vector<char> tasks = {'A', 'A', 'A', 'B', 'B', 'B'};
    int n = 2;
    cout << solution.leastInterval(tasks, n) << endl;
    return 0;
}
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
- Use a priority queue to store the frequency of each task.
- Add a cooldown period when the same task is popped consecutively.
- Calculate the least number of units of time to finish all tasks with the given constraints.