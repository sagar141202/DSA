# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are represented as pairs of integers, where the first integer is the start time and the second integer is the finish time. The goal is to find the maximum number of non-overlapping activities that can be selected.

## Approach
The algorithm sorts the activities based on their finish times and then iterates over the sorted activities, selecting the activities that do not overlap with the previously selected activity. This greedy approach ensures that the maximum number of non-overlapping activities are selected.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool compare(pair<int, int> a, pair<int, int> b) {
    return a.second < b.second;
}

int activitySelection(vector<pair<int, int>> activities) {
    // Sort activities based on finish time
    sort(activities.begin(), activities.end(), compare);
    
    int count = 1;
    int finishTime = activities[0].second;
    
    // Iterate over the sorted activities
    for (int i = 1; i < activities.size(); i++) {
        // Check if the current activity does not overlap with the previous one
        if (activities[i].first >= finishTime) {
            count++;
            finishTime = activities[i].second;
        }
    }
    
    return count;
}

int main() {
    vector<pair<int, int>> activities = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    cout << "Maximum number of activities: " << activitySelection(activities);
    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4
```

## Key Takeaways
- The greedy approach is used to solve the activity selection problem.
- The activities are sorted based on their finish times to ensure that the maximum number of non-overlapping activities are selected.
- The time complexity of the algorithm is O(n log n) due to the sorting step, and the space complexity is O(1) as no extra space is used.