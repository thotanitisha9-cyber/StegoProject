# Abstract

**Project Title:** A Deep Learning-Based Ensemble Framework for Multi-Modal Steganography and Steganalysis

**Abstract:**

Steganography, the art of hiding information within innocuous carriers, poses significant challenges to digital forensic analysis. While traditional steganography provides a means for covert communication, it is equally critical to develop robust steganalysis tools to detect illicitly hidden data. This project presents a comprehensive web-based framework that integrates multi-modal steganography tools with an advanced, ensemble-based detection system.

The proposed system implements robust steganographic algorithms across three media types: **Image Steganography** using the Least Significant Bit (LSB) technique, **Audio Steganography** employing LSB modification on WAV data, and **Text Steganography** utilizing Zero Width Characters (ZWC) for invisible message embedding. These modules allow users to securely encode and decode secret messages, demonstrating the efficacy of modern data hiding nuances.

The core innovation of this framework lies in its **Intelligent Steganalysis Engine**. To address the limitations of single-model detection, the system employs an **Ensemble Learning approach** that combines the feature-extraction capabilities of Deep Learning with the statistical rigor of classical Machine Learning. The detection pipeline consists of:
1.  **Deep Learning Model (CNN):** A custom Convolutional Neural Network (`ProposedNet`) that analyzes grayscale image patches to detect structural anomalies and embedding artifacts.
2.  **Machine Learning Model (Random Forest):** A classifier trained on hand-crafted statistical features, including LSB entropy, RGB histograms, and pixel variance.

By aggregating the confidence scores of these two distinct models, the system achieves higher reliability and reduced false positives compared to individual methods. The entire framework is deployed via a user-friendly **Flask web application**, offering real-time encoding, decoding, and detailed forensic analysis of suspect images. This project demonstrates a holistic approach to information security, bridging the gap between offensive steganography and defensive steganalysis.
