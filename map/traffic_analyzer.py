from typing import List
import traci


class TrafficAnalyzer:
    def __init__(self, config):
        self.speed_threshold = config.speed_threshold

    def calculate_queue_length_for_lane(self, lane_id: str) -> float:
        """
        Calculates the queue length for a specific lane.

        :param lane_id: The ID of the lane.
        :return: Queue length in meters.
        """
        vehicles_on_lane: List[str] = traci.lane.getLastStepVehicleIDs(lane_id)

        vehicles_in_queue: List[str] = [
            vehicle_id for vehicle_id in vehicles_on_lane
            if traci.vehicle.getSpeed(vehicle_id) < self.speed_threshold
        ]

        if not vehicles_in_queue:
            return 0.0

        positions: List[float] = [
            traci.vehicle.getLanePosition(vehicle_id) for vehicle_id in vehicles_in_queue
        ]

        return max(positions) - min(positions)
