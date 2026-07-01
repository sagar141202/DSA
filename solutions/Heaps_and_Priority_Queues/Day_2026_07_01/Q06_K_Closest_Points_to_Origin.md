# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, find the K closest points to the origin. The distance between two points on the X-Y plane is calculated using the Euclidean distance formula: √(x2 - x1)^2 + (y2 - y1)^2. Here, the origin is (0, 0), so the distance of a point (x, y) to the origin is √(x^2 + y^2). Return the K closest points to the origin. If there are multiple answers, you can return them in any order. Constraints: 1 <= K <= points.length <= 10^4, -10^4 < xi, yi < 10^4.

## Approach
We will use a priority queue to store points based on their Euclidean distance from the origin. The priority queue will automatically order points by their distance, allowing us to efficiently select the K closest points. We calculate the distance of each point and push it into the priority queue. Then, we pop the K smallest distances from the queue to get the K closest points.

## Complexity
- Time: O(N log K)
- Space: O(K)

## C++ Solution
```cpp
#include <queue>
#include <vector>
#include <iostream>

using namespace std;

struct Point {
    int x, y;
    int distance;
    Point(int x, int y) : x(x), y(y) {
        distance = x * x + y * y;
    }
};

struct Compare {
    bool operator()(const Point& a, const Point& b) {
        return a.distance > b.distance;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
    priority_queue<Point, vector<Point>, Compare> pq;
    for (auto& point : points) {
        pq.push(Point(point[0], point[1]));
        if (pq.size() > K) {
            pq.pop();
        }
    }

    vector<vector<int>> result;
    while (!pq.empty()) {
        Point p = pq.top();
        pq.pop();
        result.push_back({p.x, p.y});
    }
    return result;
}

int main() {
    vector<vector<int>> points = {{1, 3}, {-2, 2}};
    int K = 1;
    vector<vector<int>> result = kClosest(points, K);
    for (auto& point : result) {
        cout << "[" << point[0] << ", " << point[1] << "]" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: points = [[1, 3], [-2, 2]], K = 1
Output: [[-2, 2]]
```

## Key Takeaways
- Using a priority queue allows us to efficiently find the K smallest elements in an unsorted list.
- The Euclidean distance formula is used to calculate the distance between a point and the origin.
- The time complexity of this solution is O(N log K) due to the priority queue operations.