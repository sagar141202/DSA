# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are represented as pairs of integers, where the first integer is the start time and the second integer is the finish time. For example, if we have two activities (1, 4) and (3, 5), we can only select one of them because they overlap.

## Approach
The algorithm sorts the activities by their finish times and then iterates through the sorted list, selecting the activities that do not conflict with the previously selected activity. This approach ensures that we select the maximum number of non-conflicting activities. The key idea is to always select the activity with the earliest finish time.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent an activity
struct Activity {
    int start;
    int finish;
};

// Comparison function to sort activities by finish time
bool compareActivities(const Activity &a, const Activity &b) {
    return a.finish < b.finish;
}

// Function to select the maximum number of non-conflicting activities
int activitySelection(vector<Activity> &activities) {
    // Sort the activities by their finish times
    sort(activities.begin(), activities.end(), compareActivities);

    // Initialize the count of selected activities
    int count = 0;

    // Initialize the finish time of the last selected activity
    int lastFinish = -1;

    // Iterate through the sorted activities
    for (const auto &activity : activities) {
        // Check if the current activity does not conflict with the last selected activity
        if (activity.start >= lastFinish) {
            // Select the current activity
            count++;

            // Update the finish time of the last selected activity
            lastFinish = activity.finish;
        }
    }

    // Return the count of selected activities
    return count;
}

int main() {
    // Example usage
    vector<Activity> activities = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    cout << "Maximum number of non-conflicting activities: " << activitySelection(activities) << endl;
    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4
```

## Key Takeaways
- The greedy approach can be used to solve the activity selection problem by selecting the activity with the earliest finish time.
- The time complexity of the algorithm is O(n log n) due to the sorting step.
- The space complexity of the algorithm is O(1) because we only use a constant amount of space to store the count of selected activities and the finish time of the last selected activity.