from typing import List, Dict
from collections import defaultdict


def alert_names(key_name: List[str], key_time: List[str]) -> List[str]:
    """
    Finds workers who used their keycard 3 or more times within a one-hour period.

    Time Complexity: O(n log n)
        - Sorting times for each worker takes O(k log k) where k is number of times per worker.
        - Overall complexity is O(n log n) in worst case.

    Space Complexity: O(n)
        - Stores the times for each worker in a dictionary.

    Parameters:
    key_name (List[str]): List of worker names.
    key_time (List[str]): List of corresponding access times in "HH:MM" format.

    Returns:
    List[str]: Sorted list of worker names who received alerts.
    """

    def time_to_minutes(time_str: str) -> int:
        """Convert time string "HH:MM" to minutes since midnight."""
        hours, minutes = map(int, time_str.split(":"))
        return hours * 60 + minutes

    # Group times by worker name
    worker_times: Dict[str, List[int]] = defaultdict(list)
    for name, time in zip(key_name, key_time):
        worker_times[name].append(time_to_minutes(time))

    alert_workers: List[str] = []

    # Check each worker's access times
    for name, times in worker_times.items():
        # Sort times for this worker
        times.sort()

        # Check for 3 or more accesses within 60 minutes
        for i in range(len(times) - 2):
            # Check if there are 3 accesses within 60 minutes starting from index i
            if times[i + 2] - times[i] <= 60:
                alert_workers.append(name)
                break  # Found alert for this worker, no need to check further

    # Return sorted list of alert workers
    return sorted(alert_workers)


# Example usage
if __name__ == "__main__":
    # Test case 1
    key_name1 = ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"]
    key_time1 = ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]
    result1 = alert_names(key_name1, key_time1)
    print(f"Test case 1 - Alert workers: {result1}")  # Expected: ["daniel"]

    # Test case 2
    key_name2 = ["alice", "alice", "alice", "bob", "bob", "bob", "bob"]
    key_time2 = ["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]
    result2 = alert_names(key_name2, key_time2)
    print(f"Test case 2 - Alert workers: {result2}")  # Expected: ["bob"]

    # Additional test case
    key_name3 = ["john", "john", "john"]
    key_time3 = ["23:58", "23:59", "00:01"]
    result3 = alert_names(key_name3, key_time3)
    print(f"Test case 3 - Alert workers: {result3}")  # Expected: [] (crosses midnight)
