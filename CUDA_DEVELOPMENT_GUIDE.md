# CUDA Development Guide — NVIDIA DGX Spark Founders Edition

This guide covers the essential parameters, compilation flags, and thermal/power management strategies for developing CUDA and AI applications on the **NVIDIA DGX Spark** (Grace Blackwell architecture).

---

## 1. GPU Architecture & Compute Capability

| Parameter | Value |
|-----------|-------|
| **GPU** | NVIDIA Blackwell GB10 (integrated with 20-core ARM CPU) |
| **CUDA Cores** | 6,144 |
| **Streaming Multiprocessors (SM)** | 48 |
| **Compute Capability** | 12.1 (`sm_121`) |
| **Binary Target** | `sm_120` (compatibility mode used by PyTorch) |

### NVCC Compilation Flags

```bash
# Standard build
nvcc -arch=sm_120 -code=sm_120,sm_121 my_kernel.cu -o my_app

# If your CUDA toolkit fully supports 12.1
nvcc -arch=sm_121 my_kernel.cu -o my_app
```

### CMake Configuration

```cmake
set(CMAKE_CUDA_ARCHITECTURES 120)
# or 121 if your toolkit supports it natively
```

---

## 2. Unified Memory Architecture (UMA)

The DGX Spark features **128 GB LPDDR5x** at **273 GB/s**, shared transparently between CPU and GPU.

### Key Implications

| Aspect | Recommendation |
|--------|----------------|
| **Allocation** | Use `cudaMallocManaged()` or plain `cudaMalloc()` — the system handles migration automatically |
| **Oversubscription** | The CPU can reclaim pages from swap; `cudaMemGetInfo()` may under-report allocatable memory |
| **Zero-copy** | No explicit `cudaMemcpy()` needed between CPU and GPU for most workloads |
| **Monitoring** | Watch actual usage with `nvidia-smi` rather than relying solely on CUDA API queries |

### Example

```cpp
float *data;
cudaMallocManaged(&data, size);  // Accessible from both CPU and GPU
// ... compute ...
cudaFree(data);
```

---

## 3. Power & Thermal Management

### Reference Values

| Parameter | Value / Threshold |
|-----------|-------------------|
| **SoC TDP** | 140 W |
| **GPU Power (practical)** | ~100 W under intense load |
| **Recommended Power Cap** | 150 W total (`nvidia-smi -i 0 -pl 150`) |
| **Ideal Ambient Temp** | 5°C – 30°C |
| **GPU Throttling (ACPI)** | ≈ 91.8°C |
| **Typical Load Temp** | 50°C – 60°C (with adequate fan curve) |

### Practical Settings

```bash
# Apply at the start of every development session

# 1. Set power cap
nvidia-smi -i 0 -pl 150

# 2. Set aggressive fan curve (if not managed by DGX Dashboard)
nvidia-smi -i 0 -fan 75  # 75% static, or use a curve script

# 3. Monitor continuously
watch -n 5 nvidia-smi
```

### Fan Curve Script (optional)

Save as `~/bin/dgx_fan_control.sh`:

```bash
#!/bin/bash
while true; do
    TEMP=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits)
    if [ "$TEMP" -gt 55 ]; then
        nvidia-smi -i 0 -fan 80
    elif [ "$TEMP" -gt 45 ]; then
        nvidia-smi -i 0 -fan 60
    else
        nvidia-smi -i 0 -fan 40
    fi
    sleep 10
done
```

---

## 4. Development Workflow by Phase

| Phase | Recommended Setting | Purpose |
|-------|---------------------|---------|
| **Compilation** | `-arch=sm_120 -code=sm_120,sm_121` (NVCC) or `CUDA_ARCHITECTURES=120` (CMake) | Generates binaries optimized for GB10 |
| **Memory** | Prefer `cudaMallocManaged` or `__managed__`; monitor with `nvidia-smi` | Leverages UMA and avoids unnecessary copies |
| **Parallelism** | Limit concurrent streams/blocks if temps rise; reduce grid size for sustained loads | Reduces power/thermal peaks |
| **Monitoring** | `watch -n 5 nvidia-smi` or custom thermal logger; intervene if GPU > 78°C or power > 130W | Keeps system within safe margins |
| **Power/Thermal** | Start session with `nvidia-smi -i 0 -pl 150` and fan curve at 70-80% above 55°C | Prevents throttling and unexpected shutdowns |

---

## 5. Environment Variables

```bash
# CPU thread control — use 6 threads to reduce CPU-GPU contention
export OMP_NUM_THREADS=6
export MKL_NUM_THREADS=6
export OPENBLAS_NUM_THREADS=6

# PyTorch / Transformers
export TRANSFORMERS_NO_APEX=1
export CUDA_VISIBLE_DEVICES=0
export PYTORCH_CUDA_ALLOC_CONF="max_split_size_mb:512"
export TORCH_ALLOW_TF32_CUBLAS_OVERRIDE=1
```

---

## 6. Common Pitfalls

| Problem | Cause | Solution |
|---------|-------|----------|
| `sm_121 not compatible` warning | PyTorch ships without native sm_121 support | Expected — runs in `sm_120` compatibility mode; safe to ignore |
| `nvidia-smi` shows "Memory-Usage: Not Supported" | UMA does not expose discrete GPU memory counters | Expected — use `cudaMemGetInfo()` or `nvidia-smi dmon` |
| Silent Firefox upload failures | Snap confinement blocks file picker access | Use Chrome/Chromium or apply [firefox-snap-upload-fix](https://github.com/geneforge-ai/firefox-snap-upload-fix) |
| Unexpected thermal shutdown | Ambient > 30°C or dust buildup | Improve airflow, clean filters, apply power cap |
| Build times extremely long | All 20 CPU cores competing with GPU | Limit parallel jobs: `make -j6` instead of `-j20` |

---

## 7. Quick Reference Card

```bash
# --- Session Start ---
nvidia-smi -i 0 -pl 150
export OMP_NUM_THREADS=6

# --- Build ---
nvcc -arch=sm_120 -code=sm_120,sm_121 kernel.cu -o app

# --- Run with Monitoring ---
watch -n 5 nvidia-smi &
./app

# --- Check Thermals ---
nvidia-smi --query-gpu=temperature.gpu,power.draw,clocks.sm --format=csv
```

---

*Platform: NVIDIA DGX Spark Founders Edition (Grace Blackwell)*  
*Last updated: 2026-04-16*
