# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are given as pairs of start and finish times, and the goal is to maximize the number of activities that do not conflict with each other. For example, if we have three activities with start and finish times (1, 4), (3, 5), and (0, 6), we can select only two activities, such as (1, 4) and (3, 5) is not possible but (1, 4) and (0, 6) is not possible, (0, 6) and (3, 5) is not possible but (1, 4) is not possible with (0, 6) and (3, 5) but (1, 4) and (5, 7) is possible if (5, 7) exists.

## Approach
The approach is to sort the activities based on their finish times and then select the activities greedily. We start with the activity that finishes earliest and then select the next activity that starts after the previous activity finishes. This approach ensures that we select the maximum number of activities that do not conflict with each other. The key insight is that the activity with the earliest finish time should be selected first.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// solution with comments
bool compare(pair<int, int> a, pair<int, int> b) {
    // compare two activities based on their finish times
    return a.second < b.second;
}

int activitySelection(vector<pair<int, int>> activities) {
    // sort the activities based on their finish times
    sort(activities.begin(), activities.end(), compare);
    int count = 1;  // count of selected activities
    int finish = activities[0].second;  // finish time of the last selected activity
    for (int i = 1; i < activities.size(); i++) {
        // check if the current activity starts after the last selected activity finishes
        if (activities[i].first >= finish) {
            count++;  // increment the count of selected activities
            finish = activities[i].second;  // update the finish time of the last selected activity
        }
    }
    return count;
}

int main() {
    vector<pair<int, int>> activities = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    cout << activitySelection(activities) << endl;
    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4
```

## Key Takeaways
- The greedy approach can be used to solve the activity selection problem by sorting the activities based on their finish times and then selecting the activities that do not conflict with each other.
- The time complexity of the solution is O(n log n) due to the sorting step.
- The space complexity of the solution is O(1) as we only use a constant amount of space to store the count of selected activities and the finish time of the last selected activity.