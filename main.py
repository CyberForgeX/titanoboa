import os
import logging
import importlib
import threading
import sqlite3
import asyncio
from queue import Queue
from cryptography.fernet import Fernet
from sympy import symbols, Eq, solve
import argparse
import sys

# =======================
# Initialize Logging
# =======================
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# =======================
# Shared Libraries (HTTP, JSON, DB, Security, etc.)
# =======================
class SharedLibs:
    def __init__(self):
        self.logger = self.setup_logger()
        self.communication_queue = Queue()
        self.security_manager = SecurityManager()
        self.optimizer = SymbolicOptimizer()
        self.db_connection = self.setup_database()

    def setup_logger(self):
        logging.info("Setting up logger...")
        return logging

    def setup_database(self):
        """Create a SQLite connection."""
        try:
            conn = sqlite3.connect('app.db')
            logging.info("Database connected successfully.")
            return conn
        except Exception as e:
            logging.error(f"Error connecting to the database: {e}")
            sys.exit(1)


# =======================
# Security Manager for Encryption/Decryption
# =======================
class SecurityManager:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt(self, message):
        logging.info(f"Encrypting message: {message}")
        return self.fernet.encrypt(message.encode())

    def decrypt(self, token):
        logging.info(f"Decrypting token...")
        return self.fernet.decrypt(token).decode()


# =======================
# Symbolic Optimizer for Complex Equations
# =======================
class SymbolicOptimizer:
    @staticmethod
    def optimize_equation():
        logging.info("Optimizing equation...")
        x, y = symbols('x y')
        equation = Eq(2 * x + 3 * y, 12)
        solution = solve(equation, x)
        logging.info(f"Optimized equation solution: {solution}")
        return solution

    @staticmethod
    def reverse_engineer_data(data):
        logging.info(f"Reverse engineering data: {data}")
        var = symbols('var')
        equation = Eq(var ** 2, data)
        solution = solve(equation, var)
        logging.info(f"Reverse engineered solution: {solution}")
        return solution


# =======================
# Framework for Managing Modules and Orchestrators
# =======================
class Framework:
    def __init__(self, shared_libs):
        self.shared_libs = shared_libs
        self.modules = {}
        self.module_types = ['models', 'controllers', 'services', 'utils', 'security']
        logging.info("Framework initialized successfully.")

    def auto_discover_and_register(self):
        """Auto-discover and register orchestrators in each folder."""
        for module_type in self.module_types:
            dir_path = f"./{module_type}"
            if os.path.exists(dir_path):
                for file in sorted(os.listdir(dir_path)):
                    if file.endswith(".py") and 'orchestrate' in file:
                        module_name = f"{module_type}.{file[:-3]}"  # Strip off .py
                        try:
                            module = importlib.import_module(module_name)
                            self.register_module(module_name, module)
                        except Exception as e:
                            logging.error(f"Failed to load {module_name}: {e}")

    def register_module(self, name, module):
        if name in self.modules:
            logging.error(f"Module {name} already exists!")
            return
        self.modules[name] = module
        logging.info(f"Module {name} registered successfully.")

    async def run_module(self, name, *args, **kwargs):
        """Run the orchestrated module."""
        if name not in self.modules:
            logging.error(f"Module {name} not found!")
            return
        module = self.modules[name]
        await module.run(self.shared_libs, *args, **kwargs)


# =======================
# Orchestrator Generator
# =======================
def generate_orchestrators(base_dir):
    """Generates orchestrators for each folder dynamically."""
    logging.info(f"Generating orchestrators for: {base_dir}")
    for root, dirs, files in os.walk(base_dir):
        py_files = [f for f in files if f.endswith('.py') and not 'orchestrate' in f]
        if not py_files:
            continue
        
        folder_name = os.path.basename(root)
        folder_number = folder_name.split('_')[0]
        orchestrator_name = f"{folder_number}_orchestrate_{len(py_files)}.py"
        orchestrator_path = os.path.join(root, orchestrator_name)

        try:
            with open(orchestrator_path, 'w') as f:
                f.write(f"# Automatically generated orchestrator for {folder_name}\n")
                f.write("import importlib\n")
                f.write("import logging\n\n")

                function_name = folder_name.split('_')[1]
                f.write(f"def run_{function_name}(shared_libs):\n")
                f.write(f"    logging.info('Running {function_name} in order...')\n\n")

                f.write("    files = [\n")
                for py_file in py_files:
                    module_name = py_file[:-3]
                    f.write(f"        '{folder_name}.{module_name}',\n")
                f.write("    ]\n\n")

                f.write("    for file in files:\n")
                f.write("        try:\n")
                f.write("            module = importlib.import_module(file)\n")
                f.write("            module.execute(shared_libs)\n")
                f.write("        except Exception as e:\n")
                f.write("            logging.error(f'Error loading {file}: {e}')\n")

            logging.info(f"Orchestrator {orchestrator_name} generated successfully.")
        except Exception as e:
            logging.error(f"Failed to create orchestrator: {e}")


# =======================
# Server and Client with Thread-based Communication
# =======================
class Server:
    def __init__(self, framework):
        self.framework = framework
        self.queue = framework.shared_libs.communication_queue

    def start(self):
        logging.info("Starting server...")
        threading.Thread(target=self.run_server).start()

    def run_server(self):
        while True:
            if not self.queue.empty():
                data = self.queue.get()
                logging.info(f"Server received: {data}")
                self.queue.put(f"Server acknowledged: {data}")  # Reply to client


class Client:
    def __init__(self, framework):
        self.framework = framework
        self.queue = framework.shared_libs.communication_queue

    def start(self):
        logging.info("Starting client...")
        threading.Thread(target=self.run_client).start()

    def run_client(self):
        for i in range(5):  # Simulate sending 5 messages
            message = f"Client message {i}"
            logging.info(f"Client sending: {message}")
            self.queue.put(message)  # Send message to server
            threading.Event().wait(1)  # Wait for a second before checking response
            if not self.queue.empty():
                response = self.queue.get()
                logging.info(f"Client received: {response}")


# =======================
# Command-line Interface (CLI)
# =======================
def titanoboa(project_name):
    logging.info(f"Initializing project: {project_name}")

    # Generate orchestrators dynamically based on folder structure
    generate_orchestrators('./')

    # Initialize shared libraries
    shared_libs = SharedLibs()

    # Initialize the framework and pass shared libraries
    app = Framework(shared_libs)

    # Auto-discover and register orchestrators
    app.auto_discover_and_register()

    # Start server and client using threads
    server = Server(app)
    client = Client(app)

    server.start()
    client.start()

    # Run a dynamically loaded module (dynamic orchestrator discovery)
    for module in app.modules:
        asyncio.run(app.run_module(module))


# Main CLI Handler
def main():
    parser = argparse.ArgumentParser(description="Titanoboa Framework")
    parser.add_argument("command", help="Command to execute: init/run/clean")
    parser.add_argument("project_name", help="Name of the project")

    args = parser.parse_args()

    if args.command == "init":
        titanoboa(args.project_name)
    else:
        logging.error("Unknown command")


if __name__ == "__main__":
    main()
