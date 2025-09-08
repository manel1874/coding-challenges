"""

You've begun your new job to organize newspapers. Each morning, you are to separate the newspapers into smaller piles and assign each pile to a co-worker. This way, your co-workers can read through the newspapers and examine their contents simultaneously.

Each newspaper is marked with a read time to finish all its contents. A worker can read one newspaper at a time, and, when they finish one, they can start reading the next. Your goal is to minimize the amount of time needed for your co-workers to finish all newspapers. Additionally, the newspapers came in a particular order, and you must not disarrange the original ordering when distributing the newspapers. In other words, you cannot pick and choose newspapers randomly from the whole pile to assign to a co-worker, but rather you must take a subsection of consecutive newspapers from the whole pile.

What is the minimum amount of time it would take to have your coworkers go through all the newspapers? That is, if you optimize the distribution of newspapers, what is the longest reading time among all piles?

Constraints
1 <= newspapers_read_times.length <= 10^5

1 <= newspapers_read_times[i] <= 10^5

1 <= num_coworkers <= 10^5

Examples
Example 1:
Input: newspapers_read_times = [7,2,5,10,8], num_coworkers = 2
Output: 18
Explanation:
Assign first 3 newspapers to one coworker then assign the rest to another. The time it takes for the first 3 newspapers is 7 + 2 + 5 = 14 and for the last 2 is 10 + 8 = 18.

Example 2:
Input: newspapers_read_times = [2,3,5,7], num_coworkers = 3
Output: 7
Explanation:
Assign [2, 3], [5], and [7] separately to workers. The minimum time is 7.

Similar questions:
- https://leetcode.com/problems/koko-eating-bananas/description/
- https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
- https://leetcode.com/problems/snapshot-array/
"""

class Solution:
    def min_time(self, newspapers_read_times: list[int], num_coworkers: int) -> int:

        left = max(newspapers_read_times)
        right = sum(newspapers_read_times)

        while left <= right:
            mid = (left + right) // 2
            
            # Check feasibility
            current_coworkers = 1
            current_read_time = 0
            for read_time in newspapers_read_times:
                if current_read_time + read_time > mid:
                    current_coworkers += 1
                    current_read_time = 0
                current_read_time += read_time
            feasible = (current_coworkers <= num_coworkers)

            if feasible:
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    newspapers_read_times = [7,2,5,10,8]
    num_coworkers = 2
    min_time = Solution().min_time(newspapers_read_times, num_coworkers)
    print(min_time)
