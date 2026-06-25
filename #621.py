# 621. Task Scheduler

from collections import defaultdict
from collections import deque
import heapq


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = defaultdict(int)

        for task in tasks:
            count[task] += 1
        heap = []
        for task, val in count.items():
            heap.append((-val, task))

        heapq.heapify(heap)

        q = deque()
        time = 0

        while heap or q:
            if heap:
                currFreq, currTask = heapq.heappop(heap)
                currFreq *= -1
                currFreq -= 1

                if currFreq > 0:
                    q.append((currFreq, currTask, time + n + 1))

            time += 1
            i = 0
            while q and q[0][2] <= time:
                f, t, ti = q.popleft()
                heapq.heappush(heap, (-f, t))

        return time


# Time complexity: O(nlogn), loop through all tasks and heappush/pop each iteration.
# Space complexity: O(n), hashmap, heap, and queue all store n things

# Technically, n is bounded by the alphabet so only 26 at most,
# making both the space and time complexity O(1)
