from lane import Lane
from typing import List


class JunctionState:
    """
    Represents the state of a junction at a specific moment in time.
    """

    def __init__(self, junction_id: str):
        """
        Initializes a JunctionState object.

        :param junction_id: The ID of the junction.
        """
        self.junction_id = junction_id
        self.lanes: List[Lane] = []

    def add_lane(self, lane: Lane, queue_length: float):
        """
        Adds a lane to the junction state, including its queue length.

        :param lane: The Lane object.
        :param queue_length: The queue length for this lane.
        """
        lane.queue_length = queue_length
        self.lanes.append(lane)

    def __str__(self):
        """
        Returns a string representation of the junction state.
        """
        output = [f"Junction {self.junction_id}:"]
        for lane in self.lanes:
            output.append(f"  {lane}, Queue length = {lane.queue_length:.2f} meters")
        return "\n".join(output)
