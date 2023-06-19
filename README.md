# Benchmark Data/AI Code on GKE Notebooks (inc. Accelerators)

Prerequisite: __Create a Standard GKE Cluster, with the Cloud TPUs feature enabled.__

_Install Nvidia drivers and deploy the notebook resources_
```bash
kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/cos/daemonset-preloaded-latest.yaml
kubectl apply -f resources.yaml
```

_Example Baseline (and/or TPU) Configuration_
```bash
# 16 CPU, 60 GB RAM
gcloud container node-pools create baseline \
  --machine-type n1-standard-16 \
  --zone us-central1-a \
  --cluster cluster-1 \
  --node-locations us-central1-a \
  --num-nodes 1 \
  --scopes cloud-platform
```

_Example Nividia A100 Configuration_
```bash
# 12 CPU, 85 GB RAM
gcloud container node-pools create nvidia-tesla-a100 \
  --accelerator type=nvidia-tesla-a100,count=1 \
  --machine-type a2-highgpu-1g \
  --zone us-central1-a \
  --cluster cluster-1 \
  --node-locations us-central1-a \
  --num-nodes 1 \
  --scopes cloud-platform
```

_Example Nividia L4 Configuration_
```bash
# 16 CPU, 64 GB RAM
gcloud container node-pools create nvidia-l4 \
  --accelerator type=nvidia-l4,count=1 \
  --machine-type g2-standard-16 \
  --zone us-central1-a \
  --cluster cluster-1 \
  --node-locations us-central1-a \
  --num-nodes 1 \
  --scopes cloud-platform
```