# Kria KV260 Convolutional Neural Network Deployment

## Overview
This repository is dedicated to running a Convolutional Neural Network (CNN) on the target board Kria KV260. The deployment process is facilitated by the `run_all.sh` script, which orchestrates the execution of all necessary scripts on the host machine.

## Vitis AI and FPGA Acceleration
**Vitis AI**: Vitis AI, provided by Xilinx, is a framework designed for deploying machine learning models on FPGA (Field-Programmable Gate Array) platforms. It allows developers to harness FPGA acceleration for inference tasks, offering significant performance benefits compared to traditional CPU-based inference.

**FPGA Acceleration**: FPGA acceleration refers to the utilization of FPGAs to accelerate computation-intensive tasks, such as machine learning inference. FPGAs are highly parallelizable and customizable, enabling efficient execution of complex algorithms with low latency and high throughput. Offloading computation tasks to FPGAs results in substantial speedup and energy efficiency compared to running on CPU or GPU alone.

## Kria KV260 Board
**Kria KV260**: The Kria KV260 is a system-on-module (SoM) developed by Xilinx, featuring a Zynq UltraScale+ MPSoC with integrated FPGA fabric. Tailored for AI and machine learning applications, the KV260 board offers high performance and power efficiency for edge computing deployments. Its scalable and flexible platform empowers developers to deploy deep learning models in resource-constrained environments.

## Inference Performance Comparison
The repository includes a performance comparison between inference on the Kria KV260 board and a host machine (CPU Core i7 Intel 4th generation). The results demonstrate a significant improvement in throughput on the KV260 board:

- **Host Machine (CPU Core i7 Intel 4th generation)**:
  - Inference on 10,000 images: 23.8 frames per second (FPS)

- **Kria KV260 Board**:
  - Using 1 thread: Throughput = 3,972.87 FPS
  - Using 2 threads: Throughput = 6,698.55 FPS
  - Using 3 threads: Throughput = 7,341.93 FPS

## Usage
To ensure successful deployment, it is imperative to run all scripts in the Vitis-ai-pytorch-cpu Docker container and activate Conda for PyTorch.

## Additional Resources
In addition to the deployment scripts, this repository includes architectural details of the Kria KV260 board. These details are crucial for compiling the quantized model specifically for the target board.

## Support
For any issues or inquiries regarding the deployment process, feel free to raise an issue on this repository.
