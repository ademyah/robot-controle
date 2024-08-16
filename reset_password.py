from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Qt
from email.mime.text import MIMEText
import smtplib
import random
import string
import re
import os

class ResetPasswordWindow(QWidget):
    def __init__(self, login_window=None):
        super().__init__()
        self.login_window = login_window
        self.setWindowTitle("Reset Password")
        self.setFixedSize(400, 300)  # Définir une taille fixe pour la fenêtre
        self.setStyleSheet("""
            QWidget {
                background-color: #E0F7FA;  /* Bleu ciel */
                color: black;
            }
            QLabel {
                color: #00796B;  /* Couleur bleu-vert */
                font-size: 14px;
            }
            QLineEdit {
                min-height: 45px;
                border-radius: 10px;  /* Coins arrondis */
                background-color: #FFFFFF;
                padding-left: 15px;
                color: #333333;
                border: 1px solid #00796B;
            }
            QLineEdit:focus {
                border: 2px solid #004D40;
            }
            QPushButton {
                min-height: 15px;
                border-radius: 10px;  /* Coins arrondis */
                background-color: #00796B;
                color: white;
                font-size: 16px;
                padding: 10px;
                border: none;
            }   
            QPushButton:hover {
                background-color: #004D40;
                border: 2px solid #004D40;
            }
        """)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(30, 30, 30, 30)  # Marges internes ajustées
        self.layout.setSpacing(20)  # Espacement entre les widgets
        self.layout.setAlignment(Qt.AlignCenter)  # Centrer les widgets dans le layout

        self.email_label = QLabel("Email")
        self.email_input = QLineEdit()
        self.reset_button = QPushButton("Reset Password")
        self.back_button = QPushButton("Back")  # Ajout du bouton "Back"

        self.reset_button.clicked.connect(self.reset_password)
        self.back_button.clicked.connect(self.back_to_login)  # Connexion au bouton "Back"

        # Appliquer le style aux boutons
        self.reset_button.setStyleSheet(self.get_reset_button_style())
        self.back_button.setStyleSheet(self.get_back_button_style())

        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.reset_button)
        self.layout.addWidget(self.back_button)  # Ajouter le bouton "Back"

        self.setLayout(self.layout)

        self.verification_code = None

    def reset_password(self):
        email = self.email_input.text()
        if not self.is_valid_email(email):
            QMessageBox.warning(self, "Error", "Invalid email address. Please enter a valid email.")
            return

        self.verification_code = self.generate_verification_code()
        if self.send_verification_email(email, self.verification_code):
            QMessageBox.information(self, "Email Sent", "A verification code has been sent to your email.")
        else:
            QMessageBox.warning(self, "Error", "Failed to send verification email. Please try again.")

    def generate_verification_code(self, length=6):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))

    def send_verification_email(self, email, verification_code):
        try:
            msg = MIMEText(f"Your verification code is: {verification_code}")
            msg['Subject'] = 'Password Reset Verification Code'
            msg['From'] = os.getenv('EMAIL_USER')
            msg['To'] = email

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASSWORD'))
                server.sendmail(msg['From'], [msg['To']], msg.as_string())

            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

    def is_valid_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def get_reset_button_style(self):
        """Retourne le style pour le bouton 'Reset Password'."""
        return """
            QPushButton {
                min-height: 15px;
                border-radius: 10px;
                background-color: #00796B;
                color: white;
                font-size: 16px;
                padding: 10px;
                border: none;
            }
            QPushButton:hover {
                background-color: #004D40;
                border: 2px solid #004D40;
            }
        """

    def get_back_button_style(self):
        """Retourne le style pour le bouton 'Back'."""
        return """
            QPushButton {
                border: none;
                font-size: 12px;
                color: #00796B;
                text-align: center;
            }
            QPushButton:hover {
                text-decoration: underline;
            }
        """

    def back_to_login(self):
        """Retourne à la fenêtre de connexion."""
        if self.login_window:
            self.login_window.show()
        self.close()
