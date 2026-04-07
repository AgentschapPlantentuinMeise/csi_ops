---
title: Certified Reference Material (CRM) Quality Control Procedure
version: 1.0
author: CSI Laboratory
review_cycle: 12 months
purpose: Use of certified hay CRM for quality control of digestion and ICP-OES analysis.
---

# SOP 03 — CRM Quality Control Procedure

## 1. Purpose
To describe the preparation, digestion, and evaluation of the **European Commission hay Certified Reference Material (CRM)** used for quality control (QC) of digestion efficiency and ICP‑OES analytical accuracy.

## 2. Scope
This SOP applies to all digestion batches and ICP‑OES runs where CRM verification is required to demonstrate method performance, traceability, and compliance with ISO 17025 principles.

## 3. Responsibilities
- **Analysts**: Weigh, digest, and analyse CRM according to this SOP.
- **Lab coordinator**: Verify CRM results and control charts.
- **Quality officer**: Review CRM performance during audits.

## 4. Safety
Follow all safety procedures for:
- Microwave digestion (refer to digestion SOP)
- Nitric acid handling (refer to SOP 01)
- ICP‑OES operation (instrument SOP)

---

## 5. Materials and Reagents
- **European Commission Hay CRM** (certified values for macro‑ and micro‑nutrients)
- Analytical balance (±0.1 mg)
- Microwave digestion vessels
- Nitric acid (65%)
- Hydrogen peroxide (if required by digestion SOP)
- **Y internal standard** (10 ppm stock; see SOP 02)
- 5% NO₃ stock solution (SOP 01)
- Volumetric flasks (50 mL or 100 mL depending on digestion SOP)
- ICP‑OES calibration standards (SOP 02)

---

## 6. CRM Sample Preparation

### 6.1 Weighing
1. Tare a digestion vessel.
2. Weigh **100 mg (0.100 g ± 0.002 g)** of hay CRM directly into the vessel.
3. Record:
   - Mass
   - CRM batch number
   - Vessel ID

### 6.2 Internal Standard Addition
1. Add **2 mL of 10 ppm Y internal standard** (SOP 02) directly into the digestion vessel.
2. This ensures:
   - Constant Y concentration across all samples
   - Correction for plasma drift and matrix effects

### 6.3 Acid Addition
Follow the digestion SOP, typically:
- **5 mL of 65% HNO₃**
- Optional: **1–2 mL H₂O₂** depending on matrix

### 6.4 Digestion
Digest according to the validated microwave program for plant matrices.

---

## 7. Post‑Digestion Dilution

### 7.1 Cooling and Transfer
1. Allow vessels to cool to room temperature.
2. Quantitatively transfer the digest to a **50 mL volumetric flask** (or 100 mL if your method uses that volume).

### 7.2 Matrix Adjustment
1. Add **5% NO₃ stock** (SOP 01) to bring the solution to volume.
2. Final matrix:
   - **5% NO₃**
   - **0.4 ppm Y** (if 2 mL of 10 ppm Y is diluted to 50 mL)

### 7.3 Homogenization
Invert several times.

---

## 8. ICP‑OES Analysis

### 8.1 Calibration
Use calibration standards prepared according to SOP 02:
- Multi‑element: 0, 0.5, 1, 5 ppm
- K and Ca: 0, 50, 100 ppm
- Y internal standard calibration: 0, 0.1, 0.5, 1, 2 ppm

### 8.2 CRM Measurement
Analyse the CRM digest as a sample.

---

## 9. QC Evaluation

### 9.1 Recovery Calculation
For each certified element:



\[
\text{Recovery (\%)} = \frac{\text{Measured concentration}}{\text{Certified concentration}} \times 100
\]



### 9.2 Acceptance Criteria
- **80–120% recovery** for most elements  
- **85–115%** for major nutrients (K, Ca, Mg, P)  
- **70–130%** for trace elements with low certified values  

### 9.3 Control Charts
Maintain Shewhart charts for:
- K
- Ca
- Mg
- P
- Fe
- Mn
- Zn
- Cu

Update after each digestion batch.

### 9.4 Out‑of‑Control Actions
If any element fails acceptance criteria:
1. Check calibration curve (R², residuals, drift).
2. Re‑analyse the CRM digest.
3. If still out of range:
   - Re‑digest CRM
   - Check reagents (acid, Y stock, 5% NO₃)
   - Inspect instrument performance (plasma stability, nebulizer flow)
4. Document all actions.

---

## 10. Documentation
Record in the CRM QC Log:
- CRM batch number
- Weighed mass
- Digestion batch ID
- ICP‑OES run ID
- Measured values
- Recoveries
- Acceptance status
- Corrective actions (if any)

---

## 11. References
- SOP 01 — Preparation of 5% NO₃ Stock Solution  
- SOP 02 — Calibration Standards and Internal Standard Solutions  
- Microwave digestion SOP  
- ICP‑OES instrument method  
- CRM certificate of analysis  
- ISO 17025 requirements for QC  
