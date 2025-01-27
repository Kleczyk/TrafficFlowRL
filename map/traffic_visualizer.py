import cv2
import numpy as np
from junction_state import JunctionState


class TrafficVisualizer:
    """
    Real-time visualizer for traffic simulation using OpenCV.
    """

    def __init__(self, width: int = 800, height: int = 800, scale: float = 1.0):
        """
        Initializes the TrafficVisualizer.

        :param width: Width of the visualization window.
        :param height: Height of the visualization window.
        :param scale: Scaling factor for coordinates.
        """
        self.width = width
        self.height = height
        self.scale = scale
        self.image = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background

    def draw_map(self, junction_states: list[JunctionState], max_queue_length: float):
        """
        Draws the traffic map in real-time.

        :param junction_states: List of JunctionState objects representing the current simulation state.
        :param max_queue_length: Maximum queue length for normalizing colors.
        """
        # Reset the image with a white background
        self.image.fill(255)

        for junction_state in junction_states:
            for lane in junction_state.lanes:
                # Scale the coordinates and flip the y-axis
                x_coords = [int(x * self.scale) for x, _ in lane.shape]
                y_coords = [int(self.height - y * self.scale) for _, y in lane.shape]  # Flip y-coordinates

                # Determine the color based on queue length
                color_intensity = int(255 * (lane.queue_length / max_queue_length))
                color = (0, 0, color_intensity)  # Blue color scale

                # Draw the lane as a line
                points = list(zip(x_coords, y_coords))
                for i in range(len(points) - 1):
                    cv2.line(self.image, points[i], points[i + 1], color, thickness=1)  # Thinner lines

        # Display the visualization
        cv2.imshow("Traffic Visualization", self.image)
        cv2.waitKey(1)

    def close(self):
        """
        Closes the visualization window.
        """
        cv2.destroyAllWindows()
