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
