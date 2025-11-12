#!/usr/bin/env python3

from procrastibar import StoryProgressBar
import time

# Example usage
print("Starting the procrastibar example...")
with StoryProgressBar(total=20, desc="Processing") as pbar:
    for i in range(20):
        time.sleep(0.025)  # Simulate work
        pbar.update(1)

print(f"Done! The story told was: {pbar.story_name}")
