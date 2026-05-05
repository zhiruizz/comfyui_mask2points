import json
import numpy as np
import torch


class MaskToPoints:
    """
    Mask to Points Node

    Converts a mask to random coordinate points sampled from the mask's active area.
    Outputs a JSON string of coordinates compatible with SAM2 point prompts.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "mask": ("MASK", {"tooltip": "Input mask to sample points from"}),
                "num_points": ("INT", {
                    "default": 3,
                    "min": 1,
                    "max": 10000,
                    "step": 1,
                    "tooltip": "Number of random points to sample from the mask"
                }),
                "seed": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 0xFFFFFFFF,
                    "step": 1,
                    "tooltip": "Random seed for reproducible point sampling"
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("points_json",)
    FUNCTION = "mask_to_points"
    CATEGORY = "SAM3"

    def mask_to_points(self, mask, num_points, seed):
        # mask shape: [B, H, W], use first batch item
        if torch.is_tensor(mask):
            mask_np = mask[0].cpu().numpy()
        else:
            mask_np = np.array(mask[0])

        # Binarize mask - find active pixels (value > 0)
        binary_mask = mask_np > 0
        coords = np.argwhere(binary_mask)  # returns (row, col) pairs = (y, x)

        if len(coords) == 0:
            return (json.dumps([]),)

        rng = np.random.default_rng(seed)

        if num_points >= len(coords):
            # If requested more points than available, use all points
            sampled = coords
        else:
            indices = rng.choice(len(coords), size=num_points, replace=False)
            sampled = coords[indices]

        # Convert (row, col) to {"x": col, "y": row}
        points = [{"x": int(pt[1]), "y": int(pt[0])} for pt in sampled]

        return (json.dumps(points),)


NODE_CLASS_MAPPINGS = {
    "MaskToPoints": MaskToPoints,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MaskToPoints": "Mask to Points",
}
