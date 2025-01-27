class Lane:
    """
    Represents a lane in the SUMO network.
    """

    def __init__(self, lane_id: str, shape: list[tuple[float, float]]):
        """
        Initializes a Lane object.

        :param lane_id: The ID of the lane.
        :param shape: The shape of the lane as a list of (x, y) coordinates.
        """
        self.lane_id = lane_id
        self.shape = shape
        self.queue_length: float = 0.0  # Default queue length

    def __str__(self):
        """
        Returns a string representation of the lane.
        """
        return f"Lane ID: {self.lane_id}, Shape: {self.shape}"
