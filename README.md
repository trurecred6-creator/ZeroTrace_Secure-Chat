# ZeroTrace 🔒

### Secure End-to-End Messaging System Demonstration

ZeroTrace is an interactive educational demonstration of modern cryptographic messaging principles. It features a pixel-perfect WhatsApp clone interface that allows users to visualize how a message travels from a sender to a receiver using end-to-end encryption (E2EE).

![Landing Page Prompt](https://via.placeholder.com/800x400?text=ZeroTrace+Secure+Messaging+Demo)

## 🚀 Key Features

- **WhatsApp Clone UI**: Authentic design with doodle backgrounds, message bubbles, and intuitive headers.
- **Interactive E2EE Flow**: A step-by-step walkthrough of the encryption and decryption processes.
- **Real-time Sync**: Demonstrates messaging between two separate "devices" (browser tabs) using `localStorage`.
- **Advanced Security**:
  - **AES-256 Symmetric Encryption**: For fast and secure message locking.
  - **RSA Asymmetric Encryption**: For secure exchange of session keys.
  - **SHA-256 Integrity Verification**: To detect any tampering during transit.
- **Privacy First**:
  - **Anonymous IDs**: Masks sender identity from intermediate layers.
  - **Self-Destructing Messages**: Automatic deletion of messages after they are read.

## 💻 Local Hosting

To run ZeroTrace on your local machine, follow these steps:

### Option 1: Direct Open (Simplest)
1. Navigate to the project folder.
2. Double-click [index.html](file:///Users/masuddarrahaman/Desktop/ZeroTrace/index.html) to open the landing page in your default browser.

### Option 2: Using Python (Recommended)
This method mimics a real server environment.
1. Open your terminal.
2. Navigate to the project directory:
   ```bash
   cd /Users/masuddarrahaman/Desktop/ZeroTrace
   ```
3. Start a local server:
   ```bash
   python3 -m http.server 8000
   ```
4. Open your browser and go to: `http://localhost:8000`

### Option 3: Using Node.js
If you have Node.js installed:
```bash
npx serve .
```

> [!IMPORTANT]
> **To see the real-time synchronization:**
> 1. Open the [Sender](file:///Users/masuddarrahaman/Desktop/ZeroTrace/sender.html) page in one tab.
> 2. Open the [Receiver](file:///Users/masuddarrahaman/Desktop/ZeroTrace/receiver.html) page in another tab (ensure it's the **same browser**).
> 3. Send a message from the Sender tab and switch to the Receiver tab to see it arrive!

## 🐍 CLI Simulation (`zerotrace.py`)

For a deeper dive into the logic, you can run the Python-based simulation of the cryptographic steps.

### Prerequisites
Ensure you have the required libraries:
```bash
pip install cryptography rsa
```

### Running the Script
```bash
python3 zerotrace.py
```
This script will walk you through generating keys, encrypting a message, and simulating the receiver's decryption process in your terminal.

## 🌐 Deployment

The project is pre-configured for deployment on **Netlify**.
- The `netlify.toml` file includes security headers (X-Frame-Options, XSS Protection) and SPA-style redirects to ensure the demo runs smoothly in a hosted environment.

---
*Built with ❤️ for educational purposes to demonstrate the power of cryptography.*
