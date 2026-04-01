import torch

# Check if CUDA is available
print(f"Is CUDA available? {torch.cuda.is_available()}")

# Check the installed CUDA version
print(f"CUDA Version: {torch.version.cuda}")

# Get the current device ID and name
if torch.cuda.is_available():
    cuda_id = torch.cuda.current_device()
    print(f"Current CUDA Device ID: {cuda_id}")
    print(f"CUDA Device Name: {torch.cuda.get_device_name(cuda_id)}")
