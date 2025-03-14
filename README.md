# WhatsApp Message Sender

This script automates sending messages via WhatsApp Web using Python. It reads contact details and messages from a JSON file and sends them through the WhatsApp Web interface.

## Prerequisites

Before running this script, ensure you have the following:

- **Python 3.x** installed on your system ([Download Python](https://www.python.org/downloads/)).
- **Google Chrome or any default web browser** installed.
- **WhatsApp Web** should be accessible on your system.
- **PyAutoGUI** installed for automating UI interactions.

## Installation

1. Clone this repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install the required dependencies:
   ```sh
   pip install pyautogui
   ```
3. Ensure that **contact-details.json** is present in the same directory as the script.

## Usage

1. Open a terminal and navigate to the script directory.
2. Run the script:
   ```sh
   python whatsapp_sender.py
   ```
3. The script will open WhatsApp Web and send messages to the contacts listed in `contact-details.json`.

## Tested Environment

- **OS:** macOS (Tested on latest version)
- **Python Version:** 3.x
- **Browser:** Google Chrome
- **WhatsApp Web:** Required

## Notes

- Ensure your WhatsApp Web is logged in before running the script.
- The script waits for a few seconds between actions to ensure smooth execution.
- It uses **PyAutoGUI**, so do not use your keyboard or mouse while the script is running to avoid interruptions.

## About CrakCode

At **CrakCode**, we help individuals crack job offers from top **product-based companies**. Our structured programs have successfully assisted candidates in securing positions at **Swiggy, BlinkIt, Khatabook, AstroTalk, BMW Techworks India, EasyDinner**, and many more. The success stories continue to grow!

For more details, you can reach out to us on **WhatsApp: +917303778817** or visit our website:
👉 [CrakCode Website](https://www.crakcode.in)

### Connect with us on LinkedIn:
- **Company Page:** [CrakCode LinkedIn](https://www.linkedin.com/company/crakcode/)
- **Founder Profile:** [Tarun Mehta](https://www.linkedin.com/in/tarun-mehta-8541016b/)

## License

This project is open-source. Feel free to modify and improve it as needed.

## Support

For any issues, feel free to raise a GitHub issue or reach out.

