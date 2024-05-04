> GPUs aren't just fast because of parallelism, but also due to their bandwidth-optimized architecture

**CPU vs GPU Memory Optimization**

* CPUs are latency optimized (like a Ferrari) while GPUs are bandwidth optimized (like a big truck)
* GPUs can fetch more memory at once, reducing the need for repeated fetches like CPUs
* Best CPUs have 50GB/s memory bandwidth, while best GPUs have 750GB/s

**Hiding Latency with Thread Parallelism**

* Use multiple threads to fetch packages (memory) concurrently, hiding latency
* This is why GPUs are faster than CPUs for large chunks of memory
* More threads don't help CPUs, as they're already optimized for latency

**Register and L1 Cache Advantages**

* GPUs have many small register files per processing unit (stream processor)
* Total register size is much larger and faster than CPU registers
* GPU registers operate at 80TB/s, while CPU registers operate at 10-20TB/s

**Conclusion**

* High bandwidth main memory
* Hiding memory access latency under thread parallelism
* Large and fast register and L1 cache that's easily programmable

---
**Most Important GPU Specs for Deep Learning Processing Speed**

1. **Tensor Cores**: Most critical component
2. **Memory Bandwidth**: Second most important factor
3. **Cache Hierarchy**: Next in importance
4. **FLOPS (Floating-Point Operations Per Second)**: Least important, but still relevant


---
Link - [GPU for DL](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)
