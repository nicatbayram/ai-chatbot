import sys
import json
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import google.generativeai as ai

class ChatBubbleWidget(QWidget):
    def __init__(self, text, is_bot, dark_mode=False):
        super().__init__()
        self.text = text
        self.is_bot = is_bot
        self.dark_mode = dark_mode
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()
        if not self.is_bot:
            layout.addStretch()
        
        bubble = QLabel(self.text)
        bubble.setWordWrap(True)
        bubble.setMaximumWidth(600)  # Updated maximum width
        
        # Calculate size based on text content
        font_metrics = QFontMetrics(bubble.font())
        text_width = min(font_metrics.width(self.text) + 40, 800)  # Add padding
        text_height = font_metrics.height() * (len(self.text) // (text_width // font_metrics.averageCharWidth()) + 1)
        
        bubble.setMinimumSize(text_width, text_height + 20)  # Add vertical padding
        
        # Updated color scheme for dark mode
        if self.dark_mode:
            bg_color = '#2A2A2A' if self.is_bot else '#0D47A1'
            text_color = '#FFFFFF'
        else:
            bg_color = '#FFFFFF' if self.is_bot else '#2196F3'
            text_color = '#000000' if self.is_bot else '#FFFFFF'
        
        style = f"""
            QLabel {{
                background-color: {bg_color};
                color: {text_color};
                padding: 15px;
                border-radius: 20px;
                margin: {'0px 15px 0px 0px' if self.is_bot else '0px 0px 0px 15px'};
            }}
        """
        if self.is_bot:
            style += "border-top-left-radius: 0px;"
        else:
            style += "border-top-right-radius: 0px;"
            
        bubble.setStyleSheet(style)
        layout.addWidget(bubble)
        
        if self.is_bot:
            layout.addStretch()
        
        self.setLayout(layout)

class ChatbotGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dark_mode = False
        self.messages = []  # Store message history
        self.initUI()
        self.setup_gemini()

    def setup_gemini(self):
        API_KEY = "AIzaSyCDX0M14chBfXizN0xqH1Vi9oFmiWD5wOA"
        ai.configure(api_key=API_KEY)
        self.model = ai.GenerativeModel("gemini-pro")
        self.chat = self.model.start_chat()

    def initUI(self):
        self.setWindowTitle('Modern Chatbot')
        self.setGeometry(100, 100, 1600, 1200)  # Doubled dimensions
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        
        # Header with updated styling
        header = QWidget()
        header_layout = QHBoxLayout()
        header.setStyleSheet(f"""
            background-color: {('#1A1A1A' if self.dark_mode else '#1976D2')};
            padding: 20px;
            border-bottom: 1px solid {'#333333' if self.dark_mode else '#1565C0'};
        """)
        
        # Updated avatar size
        avatar_label = QLabel()
        avatar_pixmap = QPixmap(64, 64)  # Doubled size
        avatar_pixmap.fill(Qt.transparent)
        painter = QPainter(avatar_pixmap)
        painter.setBrush(QBrush(QColor("#ffffff")))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, 64, 64)
        painter.end()
        avatar_label.setPixmap(avatar_pixmap)
        header_layout.addWidget(avatar_label)
        
        title = QLabel("AI Assistant")
        title.setStyleSheet("color: white; font-size: 36px; font-weight: bold;")  # Doubled font size
        header_layout.addWidget(title)
        
        dark_mode_btn = QPushButton("🌙" if not self.dark_mode else "☀️")
        dark_mode_btn.clicked.connect(self.toggle_dark_mode)
        dark_mode_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: white;
                font-size: 40px;
                padding: 20px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
            }
        """)
        header_layout.addWidget(dark_mode_btn, alignment=Qt.AlignRight)
        
        header.setLayout(header_layout)
        layout.addWidget(header)
        
        # Message area with updated styling
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet(f"""
            QScrollArea {{
                border: none;
                background-color: {'#121212' if self.dark_mode else '#F5F5F5'};
            }}
        """)
        
        self.chat_widget = QWidget()
        self.chat_layout = QVBoxLayout()
        self.chat_layout.addStretch()
        self.chat_widget.setLayout(self.chat_layout)
        self.scroll_area.setWidget(self.chat_widget)
        layout.addWidget(self.scroll_area)
        
        # Input area with updated styling
        input_widget = QWidget()
        input_layout = QHBoxLayout()
        
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Type your message...")
        self.message_input.returnPressed.connect(self.send_message)
        self.message_input.setStyleSheet(f"""
            QLineEdit {{
                padding: 20px;
                border-radius: 30px;
                background-color: {'#2A2A2A' if self.dark_mode else '#FFFFFF'};
                color: {'#FFFFFF' if self.dark_mode else '#000000'};
                border: 2px solid {'#333333' if self.dark_mode else '#E0E0E0'};
                font-size: 24px;
            }}
        """)
        input_layout.addWidget(self.message_input)
        
        send_btn = QPushButton("Send")
        send_btn.clicked.connect(self.send_message)
        send_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 20px 40px;
                border-radius: 30px;
                font-size: 24px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        input_layout.addWidget(send_btn)
        
        input_widget.setLayout(input_layout)
        layout.addWidget(input_widget)
        
        # Restore messages from history
        self.restore_messages()

    def restore_messages(self):
        # Clear existing widgets first
        while self.chat_layout.count() > 1:
            item = self.chat_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # If no messages exist, add initial greeting
        if not self.messages:
            self.messages.append({"text": "Hello! How can I help you today?", "is_bot": True})
        
        # Restore all messages
        for message in self.messages:
            bubble = ChatBubbleWidget(message["text"], message["is_bot"], self.dark_mode)
            self.chat_layout.insertWidget(self.chat_layout.count() - 1, bubble)

    def add_message(self, text, is_bot):
        self.messages.append({"text": text, "is_bot": is_bot})
        bubble = ChatBubbleWidget(text, is_bot, self.dark_mode)
        self.chat_layout.insertWidget(self.chat_layout.count() - 1, bubble)
        QTimer.singleShot(100, lambda: self.scroll_area.verticalScrollBar().setValue(
            self.scroll_area.verticalScrollBar().maximum()
        ))

    def send_message(self):
        message = self.message_input.text().strip()
        if message:
            self.add_message(message, False)
            self.message_input.clear()
            
            try:
                response = self.chat.send_message(message)
                self.add_message(response.text, True)
            except Exception as e:
                self.add_message(f"Error: {str(e)}", True)

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        self.initUI()

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    # Updated font size
    font = QFont('Segoe UI', 20)  # Doubled font size
    app.setFont(font)
    
    window = ChatbotGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()