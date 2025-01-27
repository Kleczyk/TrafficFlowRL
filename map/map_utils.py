from typing import Dict, List
import sumolib


class MapUtils:
    @staticmethod
    def get_junctions_with_edges(network_file: str) -> Dict[str, List[str]]:
        """
        Retrieves junctions with their incoming edges.

        :param network_file: Path to the SUMO network file.
        :return: A dictionary where keys are junction IDs and values are lists of incoming edge IDs.
        """
        net = sumolib.net.readNet(network_file)
        junctions_with_edges = {}

        for junction in net.getNodes():
            incoming_edges = [edge.getID() for edge in junction.getIncoming()]
            if incoming_edges:
                junctions_with_edges[junction.getID()] = incoming_edges

        return junctions_with_edges
