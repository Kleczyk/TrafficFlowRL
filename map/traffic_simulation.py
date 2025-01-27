from traffic_analyzer import TrafficAnalyzer
from map_utils import MapUtils
from trafic_config import TrafficConfig
from lane import Lane
from junction_state import JunctionState
import traci
from sumolib import checkBinary

from traffic_visualizer import TrafficVisualizer

class TrafficSimulation:
    def __init__(self, config: TrafficConfig):
        """
        Initialize the TrafficSimulation instance.

        :param config: An instance of TrafficConfig with the simulation settings.
        """
        self.config = config
        self.analyzer = TrafficAnalyzer(config)
        self.visualizer = TrafficVisualizer(width=800, height=800, scale=0.8)

    def run(self):
        """
        Runs the traffic simulation, calculates queue lengths, and visualizes the state in real-time.
        """
        # Start SUMO with the provided configuration
        traci.start([checkBinary('sumo-gui') if self.config.use_gui else checkBinary('sumo'), "-c", self.config.sumo_config_file])
        junctions_with_edges = MapUtils.get_junctions_with_edges(self.config.network_file)


        while traci.simulation.getMinExpectedNumber() > 0:
            traci.simulationStep()

            # Store the junction states for the current iteration
            current_junction_states = []

            for junction_id, edges in junctions_with_edges.items():
                junction_state = JunctionState(junction_id)

                for edge_id in edges:
                    # Get the number of lanes for the edge
                    num_lanes = traci.edge.getLaneNumber(edge_id)
                    lanes = [
                        Lane(
                            lane_id=f"{edge_id}_{i}",
                            shape=traci.lane.getShape(f"{edge_id}_{i}")
                        )
                        for i in range(num_lanes)
                    ]

                    # Calculate queue length for each lane and add it to the junction state
                    for lane in lanes:
                        queue_length = self.analyzer.calculate_queue_length_for_lane(lane.lane_id)
                        junction_state.add_lane(lane, queue_length)

                current_junction_states.append(junction_state)

            # Determine the maximum queue length for color normalization
            max_queue_length = max(
                lane.queue_length
                for junction_state in current_junction_states
                for lane in junction_state.lanes
            )

            # Update the real-time visualization
            self.visualizer.draw_map(current_junction_states, 100.0)


        # Ensure that SUMO and the visualization window are closed
        traci.close()
        self.visualizer.close()







if __name__ == "__main__":
    config = TrafficConfig("traffic_config.xml")
    simulation = TrafficSimulation(config)
    simulation.run()
