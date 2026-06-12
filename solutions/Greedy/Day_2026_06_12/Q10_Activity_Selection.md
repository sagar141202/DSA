# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are given as pairs of integers (start, finish), where start is the start time and finish is the finish time of the activity. The goal is to find the maximum number of activities that can be selected such that no two activities overlap. For example, if we have the following activities: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)], the maximum number of activities that can be selected is 4: [(1, 4), (5, 7), (8, 11), (12, 14)]. The constraints are: 1 <= number of activities <= 10^5, 1 <= start time <= 10^6, 1 <= finish time <= 10^6.

## Approach
The approach to solve this problem is to use a greedy algorithm, sorting the activities by their finish times and then selecting the activities that do not overlap with the previously selected activities. This approach ensures that we select the maximum number of activities that can be performed without any overlap. We will use a vector to store the selected activities and a variable to keep track of the finish time of the last selected activity.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to select the maximum number of activities
int activitySelection(vector<pair<int, int>> activities) {
    // Sort the activities by their finish times
    sort(activities.begin(), activities.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second < b.second;
    });

    // Initialize the count of selected activities and the finish time of the last selected activity
    int count = 1;
    int lastFinish = activities[0].second;

    // Iterate through the activities to select the non-overlapping activities
    for (int i = 1; i < activities.size(); i++) {
        if (activities[i].first >= lastFinish) {
            count++;
            lastFinish = activities[i].second;
        }
    }

    return count;
}

int main() {
    // Example usage
    vector<pair<int, int>> activities = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    cout << "Maximum number of activities: " << activitySelection(activities) << endl;
    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4
Input: [(1, 2), (2, 3), (3, 4), (4, 5)]
Output: 4
```

## Key Takeaways
- The greedy algorithm is used to solve the activity selection problem by sorting the activities by their finish times and selecting the non-overlapping activities.
- The time complexity of the algorithm is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the activities.
- The approach ensures that the maximum number of activities are selected without any overlap, making it an efficient solution for the problem.