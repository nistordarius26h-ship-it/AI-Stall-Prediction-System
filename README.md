# AI-Based Aircraft Stall Margin Prediction System

![Python](https://img.shields.io/badge/Python-3.11-blue)
![AI](https://img.shields.io/badge/AI-Machine%20Learning-green)
![License](https://img.shields.io/badge/License-MIT-red)
![Research](https://img.shields.io/badge/Research-Aerospace-orange)

## Overview

This project presents a research prototype for an **AI-powered aircraft stall margin prediction system** that combines forward-looking LiDAR, conventional aircraft sensors, and machine learning techniques.

Unlike traditional stall warning systems that react when the aircraft is already approaching a stall, this project investigates whether incoming airflow disturbances can be detected in advance and used to estimate the remaining stall margin.

> **Disclaimer**
>
> This project is intended for educational and research purposes only. It is **not** certified for use in real aircraft and must not be used for operational flight decisions.

---

## Features

- Forward-looking LiDAR concept
- Sensor fusion
- Machine learning prediction
- Effective Angle of Attack estimation
- Stall Margin calculation
- Python implementation
- Flight simulator integration
- Research documentation

---

<img width="1536" height="1024" alt="xiaomipad" src="https://github.com/user-attachments/assets/993de853-e09d-4937-84c9-5ed2080b9689" />

## System Architecture

-- Environment
-- LiDAR Sensors
-- ESP32 Data Acquisition
-- Jetson AI Computer
-- Sensor Fusion
-- Machine Learning
-- Stall Margin Prediction
-- Cockpit Warning Display

---

## Technologies

- Python
- ESP32
- NVIDIA Jetson Orin Nano
- LiDAR
- Scikit-Learn
- TensorFlow
- Streamlit
- FlightGear
- X-Plane

---

## Hardware

- Benewake TF03 LiDAR
- Livox Mid-360 LiDAR
- Bosch BNO055 IMU
- Honeywell Pressure Sensor
- u-blox GPS
- ESP32
- NVIDIA Jetson Orin Nano

---

## Project Structure

Python/
AI source code

Hardware/
Hardware documentation

Simulation/
Flight simulation

Architecture/
Engineering diagrams

Images/
Figures

[AI-Stall-Prediction-System.pdf](https://github.com/user-attachments/files/30150712/AI-Stall-Prediction-System.pdf)
/ Complete thesis

---

## Example

```python
effective_aoa = aoa + gust

stall_margin = critical_aoa - effective_aoa

if stall_margin < 2:
    print("STALL WARNING")
```

---

## Future Work

- Neural Networks
- Transformer Models
- Real-time LiDAR Processing
- FPGA Acceleration
- Flight Testing
- Digital Twin

---

## Research Paper

The complete research paper is included in:

[AI-Stall-Prediction-System.pdf](https://github.com/user-attachments/files/30150707/AI-Stall-Prediction-System.pdf)

---

## License

MIT License

---

## Author

Nistor Darius

Artificial Intelligence • Aerospace • Engineering
