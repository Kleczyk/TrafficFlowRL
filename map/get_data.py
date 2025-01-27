import os
import sys
from typing import List
from sumolib import checkBinary
import traci


def calculate_queue_length(edge_id: str, speed_threshold: float = 2.78) -> float:
    """
    Calculates the queue length on a given edge.

    :param edge_id: Identifier of the edge.
    :param speed_threshold: Speed threshold in m/s (default: 2.78 m/s, approximately 10 km/h).
    :return: Queue length in meters.
    """
    vehicles_on_edge: List[str] = traci.edge.getLastStepVehicleIDs(edge_id)

    vehicles_in_queue: List[str] = [
        vehicle_id for vehicle_id in vehicles_on_edge
        if traci.vehicle.getSpeed(vehicle_id) < speed_threshold
    ]

    if not vehicles_in_queue:
        return 0.0

    positions: List[float] = [
        traci.vehicle.getLanePosition(vehicle_id) for vehicle_id in vehicles_in_queue
    ]

    queue_length: float = max(positions) - min(positions)

    return queue_length


sumo_config_file: str = "sources/sim.sumocfg"
sumo_binary_path: str = checkBinary('sumo-gui')
traci.start([sumo_binary_path, "-c", sumo_config_file])

edge_id: str = '3si'

while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
    queue_length: float = calculate_queue_length(edge_id)
    print(f"Queue length on edge {edge_id}: {queue_length:.2f} meters")

traci.close()
