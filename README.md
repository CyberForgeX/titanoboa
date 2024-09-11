# Titanoboa Framework

**Titanoboa** is a dynamic, scalable, and modular Python framework that handles thread-based communication, dynamic module registration, and orchestrator generation. It's designed to handle large, complex projects with ease, and it's production-ready with error handling, logging, and a flexible architecture.

## Features
- **Dynamic Orchestrator Generation**: Automatically generates orchestrators for each module folder based on the file structure.
- **Thread-Based Communication**: Uses Python threads for seamless communication between modules (server-client architecture).
- **Scalable and Modular**: The system auto-discovers modules, registers them dynamically, and scales as folders and files are added or removed.
- **CLI-Based Management**: Use the `titanoboa` command-line tool to initialize, run, and manage projects.
- **Production-Ready**: Error handling, logging, and modular architecture make it robust and scalable for large projects.
- **Symbolic Computation**: Integrated symbolic computation and data encryption using SymPy and Cryptography.

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Commands](#commands)
- [License](#license)

---

## Installation

### Prerequisites

- **Python 3.6+**
- **pip**

### Install Titanoboa

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/titanoboa.git
   cd titanoboa
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Optional Installation with `setup.sh`**:
   Run the installer script to set up the framework and make the `titanoboa` command globally available:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

4. **Manual Setup**:
   - If you do not use the `setup.sh` script, you can manually copy `main.py` to a directory and create a symbolic link to `/usr/local/bin/titanoboa` for easy CLI usage.

---

## Usage

Once installed, you can use the `titanoboa` command to manage projects, initialize folders, and dynamically register modules and orchestrators.

### Initialize a Project

To initialize a project, run the following command:

```bash
titanoboa init <project_name>
```

This will:
- Dynamically generate orchestrators based on the folder structure.
- Discover and register all modules within the project.
- Start server and client communication using threads.

### Example

```bash
titanoboa init my_project
```

This command will:
- Set up the project directory.
- Dynamically generate orchestrators.
- Auto-discover modules.
- Start the server-client communication system.

---

## Project Structure

Once you run the `titanoboa init <project_name>` command, the project will be set up with the following structure:

```
project_name/
│
├── models/
│   ├── 1_user.py
│   ├── 2_product.py
│   └── 1_orchestrate_2.py   # Orchestrator for the models folder
│
├── services/
│   ├── 1_payment.py
│   ├── 2_subscription.py
│   └── 1_orchestrate_2.py   # Orchestrator for the services folder
│
├── controllers/
│   ├── 1_controller.py
│   └── 1_orchestrate_1.py   # Orchestrator for the controllers folder
│
├── utils/
│   ├── 1_helper.py
│   └── 1_orchestrate_1.py   # Orchestrator for the utils folder
│
└── main.py                  # Main entry point for the project
```

- **Orchestrators**: Orchestrators like `1_orchestrate_2.py` are generated dynamically for each folder. These orchestrators handle the execution order of the files in their respective folders.
- **Dynamic Modules**: Files like `1_user.py` and `2_subscription.py` represent individual modules that are auto-discovered and registered into the framework.

---

## Commands

You can use the following commands with `titanoboa`:

### `titanoboa init <project_name>`
- Initializes the project with the specified name.
- Automatically generates orchestrators based on the folder structure.
- Starts the server and client communication system.
  
### `titanoboa run <project_name>`
- Starts the system for the specified project.
- Runs the orchestrators and modules that have been discovered.

### `titanoboa clean <project_name>`
- Cleans up the project by removing dynamically generated orchestrators.

---

## How It Works

1. **Orchestrator Generation**: The framework scans each folder, counts the Python files (ignoring orchestrators), and generates a new orchestrator file. This orchestrator manages the execution order of the files in that folder.
  
2. **Module Registration**: All modules (Python files) are auto-discovered and registered dynamically. The framework keeps track of the module order based on folder and file naming conventions.

3. **Server-Client Communication**: The framework starts both a server and a client using threads. The server listens for incoming messages via a thread-safe `Queue`, and the client sends messages to the server.

4. **CLI-Based Workflow**: The `titanoboa` CLI tool allows you to initialize, run, and manage projects directly from the command line. It handles all the boilerplate for you, so you can focus on building your application.

---

## License

This project is licensed under the MIT License.

---

## Contributing

If you'd like to contribute to Titanoboa, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

We welcome contributions to improve the system and add new features!

---

### That's it!

With **Titanoboa**, you're equipped to manage large, modular Python projects with ease, and handle dynamic module registration and execution through a robust, scalable architecture.
