import heapq
from typing import List

# Problem: Meeting Rooms III
# LeetCode: https://leetcode.com/problems/meeting-rooms-iii/
# LeetCode Daily Challenge
# Approach: Min Heaps (free rooms + busy rooms)
# Time Complexity: O(m log n)
# Space Complexity: O(n)

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Min heap of free room indices
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)

        # Min heap of (end_time, room_index)
        busy_rooms = []

        # Count how many meetings each room handles
        count = [0] * n

        # Sort meetings by start time
        meetings.sort()

        for start, end in meetings:
            # Free all rooms that have finished before this meeting starts
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)

            # If a room is free, use the smallest index room
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                # No room is free, delay the meeting
                earliest_end, room = heapq.heappop(busy_rooms)
                new_end = earliest_end + (end - start)
                heapq.heappush(busy_rooms, (new_end, room))

            count[room] += 1

        # Return the room with the maximum meetings (smallest index on tie)
        return count.index(max(count))
