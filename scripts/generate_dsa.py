from groq import Groq
import os
import json
import random
from datetime import datetime
from pathlib import Path

# ─────────────────────────────────────────────
#  QUESTION BANK — All major DSA topics
# ─────────────────────────────────────────────
QUESTION_BANK = {
    "Arrays_and_Strings": [
        "Two Sum", "Best Time to Buy and Sell Stock", "Contains Duplicate",
        "Product of Array Except Self", "Maximum Subarray (Kadane's Algorithm)",
        "Maximum Product Subarray", "Find Minimum in Rotated Sorted Array",
        "Search in Rotated Sorted Array", "3Sum", "Container With Most Water",
        "Trapping Rain Water", "Sliding Window Maximum", "Longest Substring Without Repeating Characters",
        "Minimum Window Substring", "Group Anagrams", "Valid Anagram",
        "Rotate Array", "Move Zeroes", "Merge Intervals", "Insert Interval",
        "Spiral Matrix", "Set Matrix Zeroes", "Pascal's Triangle",
        "Next Permutation", "Jump Game", "Gas Station"
    ],
    "Trees_and_Graphs": [
        "Binary Tree Inorder Traversal", "Binary Tree Level Order Traversal",
        "Maximum Depth of Binary Tree", "Symmetric Tree", "Path Sum",
        "Construct Binary Tree from Preorder and Inorder Traversal",
        "Binary Tree Zigzag Level Order Traversal", "Lowest Common Ancestor of BST",
        "Validate Binary Search Tree", "Kth Smallest Element in BST",
        "Number of Islands", "Clone Graph", "Course Schedule (Topological Sort)",
        "Pacific Atlantic Water Flow", "Surrounded Regions",
        "Word Ladder", "Word Search", "Graph Valid Tree",
        "Redundant Connection", "Accounts Merge",
        "Serialize and Deserialize Binary Tree", "Binary Tree Maximum Path Sum",
        "Diameter of Binary Tree", "Right Side View of Binary Tree",
        "Invert Binary Tree", "Flatten Binary Tree to Linked List"
    ],
    "Dynamic_Programming": [
        "Climbing Stairs", "House Robber", "House Robber II",
        "Longest Common Subsequence", "Longest Increasing Subsequence",
        "Coin Change", "Word Break", "Combination Sum IV",
        "Partition Equal Subset Sum", "Target Sum",
        "Distinct Subsequences", "Edit Distance", "Regular Expression Matching",
        "Wildcard Matching", "Minimum Path Sum", "Unique Paths",
        "Decode Ways", "Jump Game II", "Burst Balloons",
        "Palindromic Substrings", "Longest Palindromic Subsequence",
        "Maximum Square of 1s", "Triangle Minimum Path", "Interleaving String",
        "Paint House", "Best Time to Buy and Sell Stock with Cooldown"
    ],
    "Linked_Lists": [
        "Reverse Linked List", "Linked List Cycle", "Linked List Cycle II",
        "Merge Two Sorted Lists", "Merge K Sorted Lists", "Remove Nth Node From End",
        "Reorder List", "Add Two Numbers", "Copy List with Random Pointer",
        "Flatten a Multilevel Doubly Linked List", "Rotate List",
        "Partition List", "Sort List", "Intersection of Two Linked Lists",
        "Remove Duplicates from Sorted List", "Odd Even Linked List"
    ],
    "Stacks_and_Queues": [
        "Valid Parentheses", "Min Stack", "Evaluate Reverse Polish Notation",
        "Daily Temperatures", "Car Fleet", "Largest Rectangle in Histogram",
        "Implement Queue using Stacks", "Implement Stack using Queues",
        "Decode String", "Asteroid Collision", "Basic Calculator II",
        "Next Greater Element I", "Next Greater Element II",
        "Remove K Digits", "Simplify Path"
    ],
    "Recursion_and_Backtracking": [
        "Subsets", "Subsets II", "Permutations", "Permutations II",
        "Combination Sum", "Combination Sum II", "Letter Combinations of Phone Number",
        "Palindrome Partitioning", "N-Queens", "Sudoku Solver",
        "Word Search II", "Generate Parentheses", "Beautiful Arrangement",
        "Restore IP Addresses", "Gray Code"
    ],
    "Sorting_and_Searching": [
        "Merge Sort Implementation", "Quick Sort Implementation",
        "Kth Largest Element in Array", "Find Peak Element",
        "Search a 2D Matrix", "Search a 2D Matrix II",
        "Find K Closest Elements", "Median of Two Sorted Arrays",
        "Count of Smaller Numbers After Self", "Wiggle Sort II",
        "Sort Colors (Dutch Flag)", "Largest Number", "Meeting Rooms II"
    ],
    "Heaps_and_Priority_Queues": [
        "Kth Largest Element in a Stream", "Top K Frequent Elements",
        "Find Median from Data Stream", "K Closest Points to Origin",
        "Task Scheduler", "Reorganize String", "Sliding Window Median",
        "Smallest Range Covering Elements from K Lists"
    ],
    "Tries": [
        "Implement Trie (Prefix Tree)", "Search Suggestions System",
        "Design Add and Search Words Data Structure", "Replace Words",
        "Longest Word in Dictionary"
    ],
    "Bit_Manipulation": [
        "Single Number", "Number of 1 Bits", "Counting Bits",
        "Reverse Bits", "Missing Number", "Sum of Two Integers",
        "Power of Two", "XOR of all Numbers in Range", "Bitwise AND of Numbers Range"
    ],
    "Math_and_Number_Theory": [
        "Palindrome Number", "Reverse Integer", "Pow(x,n)",
        "Sqrt(x)", "Roman to Integer", "Integer to Roman",
        "Count Primes (Sieve)", "Happy Number", "Excel Sheet Column Number",
        "Factorial Trailing Zeroes"
    ],
    "Greedy": [
        "Activity Selection", "Fractional Knapsack", "Huffman Coding",
        "Minimum Spanning Tree (Prim's)", "Dijkstra's Algorithm",
        "Assign Cookies", "Non-overlapping Intervals", "Boats to Save People",
        "Minimum Number of Arrows to Burst Balloons"
    ],
    "Advanced_Graphs": [
        "Bellman-Ford Algorithm", "Floyd-Warshall Algorithm",
        "Minimum Spanning Tree (Kruskal's)", "Tarjan's Algorithm (SCC)",
        "Bridges in Graph", "Articulation Points", "Euler Path",
        "Bipartite Graph Check", "Alien Dictionary"
    ]
}

ALL_QUESTIONS = []
for topic, questions in QUESTION_BANK.items():
    for q in questions:
        ALL_QUESTIONS.append({"topic": topic, "question": q})

DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"]

# ─────────────────────────────────────────────
#  GROQ API CALL
# ─────────────────────────────────────────────
def generate_solution(client, topic: str, question: str, difficulty: str) -> str:
    prompt = f"""You are an expert competitive programmer. Generate a complete DSA solution.

Topic: {topic.replace('_', ' ')}
Question: {question}
Difficulty: {difficulty}
Language: C++

Respond ONLY with a markdown file in this EXACT format:

# {question}

## 📌 Problem Statement
(Write a clear, complete problem statement with constraints and examples)

## 💡 Approach
(Explain the algorithm/intuition in 3-5 lines)

## ⏱️ Complexity
- **Time:** O(...)
- **Space:** O(...)

## ✅ C++ Solution
```cpp
// Complete, compilable C++ solution with comments
#include <bits/stdc++.h>
using namespace std;

// Your solution here
```

## 🧪 Test Cases
```
Input: ...
Output: ...

Input: ...
Output: ...
```

## 📝 Key Takeaways
(2-3 bullet points on what makes this problem important)
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",   # Free, fast, very capable
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000,
        temperature=0.7,
    )
    return response.choices[0].message.content


# ─────────────────────────────────────────────
#  FILE PATH BUILDER
# ─────────────────────────────────────────────
def get_file_path(topic: str, question: str, day: str, index: int) -> Path:
    safe_question = question.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "").replace("'", "")
    filename = f"Q{index:02d}_{safe_question}.md"
    return Path(f"solutions/{topic}/Day_{day}/{filename}")


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────
def main():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set!")

    client = Groq(api_key=api_key)
    today = datetime.now().strftime("%Y_%m_%d")

    # Track which questions have been done (avoid repeats)
    tracker_path = Path("scripts/.tracker.json")
    tracker_path.parent.mkdir(parents=True, exist_ok=True)

    done = set()
    if tracker_path.exists():
        with open(tracker_path) as f:
            done = set(json.load(f))

    remaining = [q for q in ALL_QUESTIONS if q["question"] not in done]

    # If all questions exhausted, reset tracker
    if len(remaining) < 20:
        print("🔄 All questions completed! Resetting tracker...")
        done = set()
        remaining = ALL_QUESTIONS.copy()

    selected = random.sample(remaining, 20)

    print(f"📅 Generating {len(selected)} DSA solutions for {today}...\n")

    summary_entries = []

    for i, item in enumerate(selected, 1):
        topic = item["topic"]
        question = item["question"]
        difficulty = random.choice(DIFFICULTY_LEVELS)

        print(f"  [{i:02d}/20] {topic} → {question} ({difficulty})")

        try:
            solution = generate_solution(client, topic, question, difficulty)
            file_path = get_file_path(topic, question, today, i)
            file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(solution)

            done.add(question)
            summary_entries.append({
                "index": i,
                "topic": topic,
                "question": question,
                "difficulty": difficulty,
                "file": str(file_path)
            })

        except Exception as e:
            print(f"    ❌ Error: {e}")
            continue

    # Save tracker
    with open(tracker_path, "w") as f:
        json.dump(list(done), f, indent=2)

    # Update daily README log
    update_daily_log(today, summary_entries)

    print(f"\n✅ Done! {len(summary_entries)} solutions committed for {today}")


def update_daily_log(today: str, entries: list):
    log_path = Path("DAILY_LOG.md")

    date_pretty = datetime.now().strftime("%B %d, %Y")
    header = f"\n\n## 📅 {date_pretty}\n\n"
    header += "| # | Topic | Question | Difficulty |\n"
    header += "|---|-------|----------|------------|\n"

    for e in entries:
        topic_clean = e["topic"].replace("_", " ")
        header += f"| {e['index']:02d} | {topic_clean} | [{e['question']}]({e['file']}) | {e['difficulty']} |\n"

    # Prepend to log file
    existing = ""
    if log_path.exists():
        with open(log_path) as f:
            existing = f.read()

    # Build top section once
    if "# 📚 DSA Daily Practice Log" not in existing:
        top = "# 📚 DSA Daily Practice Log\n\nTracking all DSA problems solved, organized by topic and date.\n"
    else:
        top = ""

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(top + header + existing.replace("# 📚 DSA Daily Practice Log\n\nAutomatically generated by GitHub Actions Bot 🤖\n", ""))


if __name__ == "__main__":
    main()
