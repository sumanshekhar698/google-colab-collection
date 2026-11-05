# Google Colab Notebooks & Engineering Lab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)

A structured collection of hands-on Google Colab notebooks, practical code examples, reproducible experiments, and engineering implementations spanning Generative AI, Deep Learning, Data Engineering, Machine Learning, Python, and Embedded Systems.

This repository serves as a practical learning and experimentation lab, bringing together notebooks, source code, and engineering implementations.

---

## 📚 Python Learning Resources

A collection of Python notebooks and practical code examples organized into different learning tracks.

### 1. Python Fundamentals

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1BmU0fJTk2AkLQVm3TIpWf-dODJMam5j3?usp=sharing)

[Open Notebook](https://colab.research.google.com/drive/1BmU0fJTk2AkLQVm3TIpWf-dODJMam5j3?usp=sharing)

### 2. Python Core Extended

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zP4D36Za_nelWrfKVDAlX_ZWRqxGSYg-?usp=sharing)

[Open Notebook](https://colab.research.google.com/drive/1zP4D36Za_nelWrfKVDAlX_ZWRqxGSYg-?usp=sharing)

### 3. Advanced Python

A separate notebook dedicated to further Python learning and experimentation.

**Notebook:** `Advanced_Python.ipynb`

---

## 📓 Working with Jupyter Notebooks

The `.ipynb` notebooks can be opened and executed using Google Colab, JupyterLab, or Visual Studio Code.

### Option 1: Google Colab

Google Colab allows you to execute notebooks directly in your browser without installing Python or configuring a local environment.

**Steps:**

1. Open [Google Colab](https://colab.research.google.com/).
2. Sign in with your Google account.
3. Select **File → Open notebook**.
4. Navigate to the **GitHub** tab.
5. Enter the repository URL.
6. Select the notebook you want to open.
7. Start executing the cells.

Alternatively, use the direct Colab links provided in the Python Learning Resources section.

**Note:** Changes made in Colab are not automatically committed to this GitHub repository. Save a copy to Google Drive or download your modified notebook.

### Option 2: JupyterLab

You can execute notebooks locally using JupyterLab.

**Step 1: Clone the repository**

```bash
git clone <repository-url>
cd <repository-name>
```

**Step 2: Create and activate a virtual environment**

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Step 3: Install project dependencies**

```bash
python -m pip install -r requirements.txt
```

**Step 4: Install JupyterLab**

```bash
python -m pip install jupyterlab
```

**Step 5: Launch JupyterLab**

```bash
jupyter lab
```

JupyterLab will open in your default browser.

Navigate to the `Python/Notebooks/` directory and select the notebook you want to execute.

### Option 3: Visual Studio Code

You can also work with notebooks directly inside VS Code.

1. Install [Visual Studio Code](https://code.visualstudio.com/).
2. Install the official **Python** extension.
3. Install the official **Jupyter** extension.
4. Clone and open this repository.
5. Navigate to `Python/Notebooks/`.
6. Open any `.ipynb` file.
7. Select the Python kernel.
8. Execute the notebook cells.

---

## 📂 Repository Structure

```text
.
├── C_Language/
│   └── ...
│
├── DataEngineering/
│   └── ...
│
├── DeepLearning/
│   └── ...
│
├── EmbeddedC/
│   └── ...
│
├── GenAI/
│   └── ...
│
├── MachineLearning/
│   └── ...
│
├── Python/
│   │
│   ├── Notebooks/
│   │   ├── Advanced_Python.ipynb
│   │   ├── Core_Python.ipynb
│   │   └── Python_Core_Extended.ipynb
│   │
│   ├── PythonExtended/
│   │   └── ...
│   │
│   └── PythonLangCore/
│       ├── functions/
│       │   └── ...
│       ├── fundamentals/
│       │   └── ...
│       ├── strings/
│       │   └── ...
│       └── ...
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🛠️ Environment Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create a Virtual Environment

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 📦 Python Package Management

Some useful commands for managing project dependencies.

### Common Commands

```bash
# Install dependencies from requirements.txt
python -m pip install -r requirements.txt

# List installed packages
python -m pip list

# Inspect a specific package
python -m pip show numpy

# Uninstall a package
python -m pip uninstall -y pandas

# Upgrade a package
python -m pip install --upgrade numpy

# Check Python version
python --version

# Check pip version
python -m pip --version
```

**Note:** Removing a package from `requirements.txt` does not automatically uninstall it from your virtual environment. You must uninstall it separately.

### Version Specification in requirements.txt

| Syntax | Meaning | Example |
|---|---|---|
| `numpy==2.2.0` | Exact version only | `numpy==2.2.0` |
| `numpy>=2.0` | Version 2.0 or newer | `numpy>=2.0` |
| `numpy<3.0` | Any version below 3.0 | `numpy<3.0` |
| `numpy>=2.0,<3.0` | Version range | `numpy>=2.0,<3.0` |
| `matplotlib~=3.10.0` | Compatible release, normally 3.10.x | `matplotlib~=3.10.0` |

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.