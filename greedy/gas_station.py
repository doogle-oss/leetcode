def canCompleteCircuit(gas, cost):
    """
    LeetCode 134. Gas Station - Optimized Greedy Solution
    
    There are n gas stations around a circular route, where the amount of gas at 
    the ith station is gas[i]. You have a car with an unlimited gas tank and it 
    costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
    
    Given two integer arrays gas and cost, return the starting gas station's index 
    if you can travel around the circuit once in the clockwise direction, 
    otherwise return -1.
    
    Time Complexity: O(n) - single pass through the arrays
    Space Complexity: O(1) - only using a few variables
    
    Greedy Algorithm Key Insights:
    1. If total gas < total cost, impossible to complete circuit
    2. If we can't reach station j from station i, then we can't reach j 
       from any station between i and j-1 (those stations have even less accumulated fuel)
    3. Therefore, we can skip all stations between i and j and start from j
    """
    n = len(gas)
    total_surplus = 0    # Total fuel surplus/deficit for entire trip
    current_surplus = 0  # Current fuel surplus from current starting point
    start_station = 0    # Candidate starting station
    
    if (sum(gas) < sum(cost)):
        return -1
    # Iterate through each gas station
    # Calculate fuel balance at each station and track total surplus
    # If current surplus becomes negative, reset starting point to next station
    # This ensures we only consider valid starting points
    for i in range(n):
        fuel_balance = gas[i] - cost[i]
        total_surplus += fuel_balance
        current_surplus += fuel_balance
        
        # If current surplus becomes negative, we can't reach next station
        # from current starting point, so try starting from next station
        if current_surplus < 0:
            start_station = i + 1  # Start from next station
            current_surplus = 0    # Reset surplus for new starting point
    
    # If total surplus is non-negative, circuit is possible from start_station
    return start_station
def test_solutions():
    """Test cases to verify the optimized solution works correctly"""
    
    test_cases = [
        {
            "gas": [1, 2, 3, 4, 5],
            "cost": [3, 4, 5, 1, 2],
            "expected": 3,
            "description": "LeetCode Example 1"
        },
        {
            "gas": [2, 3, 4],
            "cost": [3, 4, 3],
            "expected": -1,
            "description": "Impossible case - insufficient total gas"
        },
        {
            "gas": [5],
            "cost": [4],
            "expected": 0,
            "description": "Single station with sufficient gas"
        },
        {
            "gas": [3, 1, 1],
            "cost": [1, 2, 2],
            "expected": 0,
            "description": "Can start from first station"
        },
        {
            "gas": [1, 2],
            "cost": [2, 1],
            "expected": 1,
            "description": "Must start from second station"
        }
    ]
    
    print("Testing Gas Station Solutions:")
    print("=" * 50)
    
    for i, test in enumerate(test_cases, 1):
        gas, cost, expected = test["gas"], test["cost"], test["expected"]
        
        # Test optimized solution
        result_optimized = canCompleteCircuit(gas, cost)
        
        
        print(f"Test {i}: {test['description']}")
        print(f"  Gas: {gas}")
        print(f"  Cost: {cost}")
        print(f"  Expected: {expected}")
        print(f"  Optimized: {result_optimized} {'✓' if result_optimized == expected else '✗'}")
        print()


if __name__ == "__main__":
    test_solutions()