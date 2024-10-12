import winsound
# an alarm should be set off when two coordinates 
# When expected boxes have overlap of two different cars, sound an alarm.
# This means that two cars are likely to collide with each other and can cause a dangerous event, 
# define a function that is able to set off an alarm
# define a function that sees when two 'lines' or 'boxes' overlap
# Write a function to detect if two lines were to overlap based on their start and end coordinates

def soundAlarm():
    duration = 3000 # 3000 ms
    freq = 440 #Hz
    winsound.Beep(freq, duration)
    
soundAlarm()
def overlap(start1, end1, start2, end2):
    """
    Determine if two line segments overlap.
    
    Parameters:
    start1 (list): [x, y] coordinates of the start point of the first line
    end1 (list): [x, y] coordinates of the end point of the first line
    start2 (list): [x, y] coordinates of the start point of the second line
    end2 (list): [x, y] coordinates of the end point of the second line
    
    Returns:
    bool: True if the line segments overlap, False otherwise
    """
    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
    
    def intersect(A, B, C, D):
        # Example: StartPoint1 is on left of startPoint2. But at the endpoints, startpoint1 is on the right of endpoint2. This means somewhere, an intersection occured
        return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
    
    return intersect(start1, end1, start2, end2)

# Test the function
# start1, end1 = [2, 1], [4, 4]
# start2, end2 = [2, 3], [5, 1]
# THE EXPECTED OUTPUT IS TRUE
# print(f"Do the lines overlap? {overlap(start1, end1, start2, end2)}")

# # Additional test cases
# print(f"Overlapping lines: {overlap([0, 0], [5, 5], [0, 5], [5, 0])}")
# print(f"Parallel lines: {overlap([0, 0], [2, 2], [1, 0], [3, 2])}")
# print(f"Touching endpoints: {overlap([0, 0], [2, 2], [2, 2], [4, 4])}")
# print(f"One point on the other line: {overlap([0, 0], [4, 4], [2, 2], [4, 0])}")
