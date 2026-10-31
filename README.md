# Google Colab Notebooks & Engineering Lab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

A structured collection of hands-on Google Colab notebooks, reproducible experiments, implementations, and code walkthroughs spanning Generative AI, Deep Learning, Data Engineering, and Embedded Systems.

python -m pip install -r requirements.txt
python -m pip uninstall -y pandas
python -m pip list
python -m pip show numpy

Syntax	Meaning	Example
numpy==2.2.0	Exact version only	numpy==2.2.0
numpy>=2.0	Version 2.0 or newer	numpy>=2.0
numpy<3.0	Any version below 3.0	numpy<3.0
numpy>=2.0,<3.0	Version range	numpy>=2.0,<3.0
matplotlib~=3.10.0	Compatible release, normally 3.10.x	matplotlib~=3.10.0

---

## 📂 Repository Structure

```text
.
├── C_Language/         # C programming fundamentals, memory management, pointers, and data structures
├── DataEngineering/    # ETL pipelines, data wrangling, SQL/NoSQL integrations, and batch/stream processing
├── DeepLearning/       # Neural networks, PyTorch/skorch workflows, training loops, and computer vision
├── EmbeddedC/          # Firmware fundamentals, microcontrollers, register-level code, and protocols
├── GenAI/              # Diffusion models, ControlNet, LLMs, prompt pipelines, and multimodal synthesis
├── MachineLearning/    # Classical ML algorithms, scikit-learn models, regression, clustering, and metrics
└── Python/             # Python core idioms, OOP patterns, automation scripts, and utilities
