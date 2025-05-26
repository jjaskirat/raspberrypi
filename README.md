# Real-Time Object Detection with YOLO on Raspberry Pi

## Overview

This project implements real-time object detection on a Raspberry Pi using the YOLO (You Only Look Once) algorithm. It's designed to be a lightweight and efficient solution for various applications like security systems, robotics, or interactive art installations. This README provides instructions on how to set up the hardware and software, and run the object detection model.

## Features

* **Real-time object detection:** Identifies multiple objects in a video stream.
* **YOLO Algorithm:** Utilizes a pre-trained YOLO model (YOLOv8-n).
* **Modular Code:** Different files for Raspberry Pi and Server PC.

## Hardware Requirements

* **Raspberry Pi:**
    * Raspberry Pi 3 Model B+ or newer.
    * MicroSD Card (16GB or larger).
    * Raspberry Pi Camera Module.

## How to run
* **Raspberry Pi:**
    * Run the file `cameras/scripts/test.py`
* **PC Capable of YOLO Inference:**
    * Run the file `server/scripts/test_predict.py`
