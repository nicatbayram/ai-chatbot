# Modern AI Chatbot

This project is a modern chatbot application built using Python and PyQt5. It integrates with Google's Generative AI to provide intelligent responses to user inputs.

## Features

- Modern UI with dark mode support
- Chat bubbles for displaying messages
- Integration with Google's Generative AI (Gemini model)
- Message history restoration
- Responsive design with dynamic resizing

## Requirements

- Python 3.x
- PyQt5
- google-generativeai

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/nicatbayram/ai-chatbot.git
    cd modern-chatbot
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:
    ```sh
    python main.py
    ```

## Usage

- Type your message in the input field and press Enter or click the "Send" button to send a message.
- Toggle dark mode by clicking the moon/sun icon in the header.
- The chatbot will respond to your messages using Google's Generative AI.

## Code Overview

- [main.py](http://_vscodecontentref_/0): The main application file containing the [ChatbotGUI](http://_vscodecontentref_/1) class and the [ChatBubbleWidget](http://_vscodecontentref_/2) class.
- [ChatbotGUI](http://_vscodecontentref_/3): The main window class that sets up the UI and handles interactions.
- [ChatBubbleWidget](http://_vscodecontentref_/4): A custom widget for displaying chat messages.

## Configuration

- The API key for Google's Generative AI is hardcoded in the [setup_gemini](http://_vscodecontentref_/5) method of the [ChatbotGUI](http://_vscodecontentref_/6) class. Replace it with your own API key if necessary.

## ScreenShots

<img width="400" alt="1" src="https://github.com/user-attachments/assets/8596132a-36f9-4c6a-8c56-86f9a4bd0547" />
<img width="400" alt="2" src="https://github.com/user-attachments/assets/23c2d5bd-d6f8-464f-bbd3-32600d5b1de9" />
<img width="400" alt="3" src="https://github.com/user-attachments/assets/e74c2f77-7fae-47d5-97ba-801e1d381098" />
<img width="400" alt="4" src="https://github.com/user-attachments/assets/badf7438-4393-43f0-86c0-d8f94790c1ac" />
