# Kria KV260 Convolutional Neural Network Deployment

## Overview
This repository contains scripts and resources for deploying a Convolutional Neural Network (CNN) on the Kria KV260 target board. The CNN deployment is based on Xilinx Vitis AI samples, tailored for execution on the KV260 board.

## Usage
To run the deployment process, execute the `run_all.sh` script on the host machine. It orchestrates the execution of all necessary scripts for deploying the CNN onto the Kria KV260 board.

### Prerequisites
- Ensure that you are running all scripts within the Vitis-ai-pytorch-cpu Docker container.
- Activate the Conda environment for PyTorch before running the scripts.

## Additional Resources
In addition to the deployment scripts, this repository includes architectural details of the Kria KV260 board. These details are essential for compiling the quantized model specifically for the target board.

## Getting Started
Follow these steps to begin deploying the CNN on the Kria KV260 board:
1. Clone this repository to your local machine.
2. Set up the Vitis-ai-pytorch-cpu Docker container environment.
3. Activate the Conda environment for PyTorch.
4. Execute the `run_all.sh` script to initiate the deployment process.

## Support
For any issues or inquiries regarding the deployment process, feel free to [raise an issue](link-to-issue-tracker) on this repository.

