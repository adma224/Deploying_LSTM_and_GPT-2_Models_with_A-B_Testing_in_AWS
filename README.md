# ml-cloud-pipeline-generative-tweets
This repository contains a scalable generative ML pipeline on AWS, demonstrating real-time text generation, model deployment, and A/B testing in a serverless setup. Ideal for ML model integration and comparison.

Install NVIDIA Container Toolkit (For GPU Support)
Add the NVIDIA package repository

bash
Copy
Edit
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb