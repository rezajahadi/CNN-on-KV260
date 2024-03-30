from common import *


model = CNN()
# Calculate number of parameters
num_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
# Calculate memory footprint
# Assuming each parameter takes 4 bytes (float32)
memory_footprint = num_params * 4
# Number of layers
num_layers = len(model.network)
print("Memory Footprint:", memory_footprint, "bytes")
print("Number of Layers:", num_layers)
print("Number of Trainable Parameters:", num_params)