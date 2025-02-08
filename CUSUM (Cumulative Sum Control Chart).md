**Definition**:  
A sequential analysis technique used to detect small shifts in a process mean or variance by accumulating deviations from a target value.

---
## Key Concepts
### How It Works
- **Accumulates deviations** from a target value over time.
- Triggers an alert when cumulative deviations exceed a predefined threshold.
- Effective for detecting **small, persistent shifts** (vs. Shewhart charts for large shifts).

### Key Components
1. **Target Value (μ₀)**: Baseline mean/variance of the process.
2. **Cumulative Sum (Sₜ)**: Sum of deviations from the target.
3. **Control Limit (h)**: Threshold for signalling a change (e.g., 5σ).

---

## Algorithm Steps
1. **Initialise**:  
   - Set target (μ₀), control limit (h), and initial cumulative sum (S₀ = 0).
2. **Calculate Deviation**:  
   For each observation ( $x_t$):  
   ( $d_t = x_t - \mu_0$)  
3. **Update Cumulative Sum**:  
	($S_t = \max(0, S_{t-1} + d_t)$)  
1. **Check Signal**:  
   If ( $S_t \geq h$), trigger a change alert.  
5. **Reset**:  
   After a signal, reset ( $S_t$) to 0.

---

## Advantages
- **High sensitivity** to small shifts.  
- Works well with **sequential data** (real-time monitoring).  
- Adjustable parameters for balance between false alarms and detection speed.

---

## Disadvantages
- Requires **prior knowledge** of target (μ₀) and expected shift size.  
- Sensitive to **parameter selection** (h, μ₀).  
- Computationally intensive for large datasets.

---

## Applications
1. **Manufacturing**: Detect equipment malfunctions.  
2. **Healthcare**: Monitor patient vital signs.  
3. **Finance**: Identify market regime changes.  
4. **Cybersecurity**: Spot anomalous network traffic.

