# 📡 PyComToAWS - Cloud-Integrated IoT Firmware Core

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AWS](https://img.shields.io/badge/AWS_IoT_Core-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![MQTT](https://img.shields.io/badge/Protocol-MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white)

## 📖 Overview

This repository contains the firmware core and cloud-integration logic for **PyCom** microcontrollers (LoPy, FiPy, GPy) connecting to **AWS IoT Core**. It serves as a robust baseline for developing edge devices that require real-time state synchronization, remote configuration, and secure telemetry transmission in industrial environments.

## 🏗️ Technical Architecture

The project implements a comprehensive communication layer between physical hardware and the AWS cloud infrastructure:

* **`main_shadowUpdater.py` (State Management):** Implements AWS Device Shadow updates, ensuring the digital twin in the cloud accurately reflects the physical device's current sensor data and health status.
* **`main_deltaListener.py` (Remote Control):** Listens for "Delta" state changes from the AWS cloud, allowing for remote configuration and command execution on the physical device.
* **`AWSIoTPythonSDK` Integration:** Utilizes the industry-standard SDK for secure, certificate-based authentication and TLS-encrypted MQTT communication.
* **`config.example.py`:** Provides a template for managing sensitive cloud credentials and endpoint definitions.

## ✨ Key Capabilities

* **Asynchronous Messaging:** Utilizes the MQTT protocol for lightweight, low-bandwidth communication, ideal for industrial IoT deployments.
* **Digital Twin Synchronization:** Full support for Device Shadows, allowing for seamless state persistence even during intermittent network connectivity.
* **Edge-to-Cloud Telemetry:** Optimized data pipelines for transmitting high-frequency sensor readings to AWS for further AI processing or storage.

## 🚀 Getting Started

### Prerequisites
* A PyCom Microcontroller (LoPy4, FiPy, etc.)
* An active AWS Account with IoT Core enabled.
* Firmware flashed with MicroPython.

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Wuradclan/PyComToAWS.git](https://github.com/Wuradclan/PyComToAWS.git)
   cd PyComToAWS
2. Configure your credentials:
    Rename config.example.py to config.py and populate it with your AWS IoT Endpoint, Certificate paths, and Device Client ID.
3. Upload to Device:
    Using the Pymakr plugin (VS Code or Atom), upload the lib folder and your desired main.py variant to your PyCom device.
   
🧠 Engineering Philosophy
This project was developed with a focus on Edge Computing reliability:
Fault Tolerance: Designed to handle network dropouts by leveraging AWS IoT's state-persistence features.
Security First: Implementation of X.509 certificate-based authentication to ensure industrial-grade security at the edge.
Modular Design: The separation of Shadow Updaters and Delta Listeners allows for easy scaling of device functionality.
