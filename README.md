# Real-Time Object Detection with YOLO on Raspberry Pi

## Overview

This project implements real-time object detection on a Raspberry Pi using the YOLO (You Only Look Once) algorithm. It's designed to be a lightweight and efficient solution for various applications like security systems, robotics, or interactive art installations. This README provides instructions on how to set up the hardware and software, and run the object detection model.

## Features

* **Real-time object detection:** Identifies multiple objects in a video stream or static images.
* **YOLO Algorithm:** Utilizes a pre-trained YOLO model (YOLOv8-n optimized for performance on resource-constrained devices.
* **Raspberry Pi Optimized:** Designed to run efficiently on Raspberry Pi.
* **Customizable:** Easily adaptable for different YOLO versions, datasets, and camera inputs.
* **Modular Code:** Assumes a Python-based implementation, making it easy to understand and modify.

## Hardware Requirements

* **Raspberry Pi:**
    * Raspberry Pi 3 Model B+ or newer (Raspberry Pi 4 Model B recommended for better performance).
    * MicroSD Card (16GB or larger, Class 10 or faster).
    * Power Supply for Raspberry Pi.
* **Camera:**
    * Raspberry Pi Camera Module (V1, V2, or HQ).
    * OR a USB Webcam compatible with Raspberry Pi.

## How to run
* **Raspberry Pi:**
    * Run the file `cameras/scripts/test.py`
* **PC Capable of YOLO Inference:**
    * Run the file `server/scripts/test_predict.py`
