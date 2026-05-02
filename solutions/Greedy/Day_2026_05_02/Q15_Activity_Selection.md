# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are given as pairs of integers (start, finish), where start is the start time and finish is the finish time of the activity. The goal is to find the maximum number of non-overlapping activities that can be selected. For example, if we have the following activities: (1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14), the maximum number of non-overlapping activities that can be selected is 4: (1, 4), (5, 7), (8, 11), (12, 14).

## Approach
The greedy algorithm is used to solve this problem by sorting the activities based on their finish times and then selecting the activities with the earliest finish times. This approach ensures that the maximum number of non-overlapping activities are selected. The algorithm iterates through the sorted activities and selects the activities that do not overlap with the previously selected activities.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent an activity
struct Activity {
    int start;
    int finish;
};

// Comparison function to sort activities based on finish times
bool compareActivities(const Activity &a, const Activity &b) {
    return a.finish < b.finish;
}

// Function to select the maximum number of non-overlapping activities
int selectActivities(vector<Activity> &activities) {
    // Sort the activities based on finish times
    sort(activities.begin(), activities.end(), compareActivities);

    // Initialize the count of selected activities
    int count = 0;

    // Initialize the finish time of the last selected activity
    int lastFinish = -1;

    // Iterate through the sorted activities
    for (const auto &activity : activities) {
        // Check if the current activity does not overlap with the last selected activity
        if (activity.start >= lastFinish) {
            // Increment the count of selected activities
            count++;

            // Update the finish time of the last selected activity
            lastFinish = activity.finish;
        }
    }

    // Return the count of selected activities
    return count;
}

int main() {
    // Define the activities
    vector<Activity> activities = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};

    // Select the maximum number of non-overlapping activities
    int count = selectActivities(activities);

    // Print the count of selected activities
    cout << "Maximum number of non-overlapping activities: " << count << endl;

    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4
```

## Key Takeaways
- The greedy algorithm is used to solve the activity selection problem by sorting the activities based on their finish times.
- The algorithm selects the activities with the earliest finish times to ensure the maximum number of non-overlapping activities are selected.
- The time complexity of the algorithm is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the activities.