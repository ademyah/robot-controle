import sys
import serial
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPalette, QBrush
from sidebar import MySideBar
from reset_password import ResetPasswordWindow
from signup import SignupWindow
from database import check_login_credentials

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(500, 500)  # Augmenter la taille de la fenêtre

        # Création du layout principal
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(30, 30, 30, 30)  # Marges internes ajustées
        self.layout.setSpacing(20)  # Espacement entre les widgets
        self.layout.setAlignment(Qt.AlignCenter)  # Centrer les widgets dans le layout

        # Création des widgets
        self.email_label = QLabel("Email")
        self.email_label.setStyleSheet("color: #00796B; font-size: 14px;")  # Couleur bleu et taille du texte

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setStyleSheet("""
            QLineEdit {
                min-height: 45px;
                border-radius: 10px;  /* Coins arrondis */
                background-color: rgba(255, 255, 255, 0.5);  /* Transparent blanc */
                padding-left: 15px;
                color: #333333;
                border: 2px solid #B0BEC5;  /* Bordure grise */
            }
            QLineEdit:focus {
                border: 2px solid #004D40;  /* Bordure verte foncée en focus */
            }
        """)

        self.password_label = QLabel("Password")
        self.password_label.setStyleSheet("color: #00796B; font-size: 14px;")

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setStyleSheet("""
            QLineEdit {
                min-height: 45px;
                border-radius: 10px;  /* Coins arrondis */
                background-color: rgba(255, 255, 255, 0.5);  /* Transparent blanc */
                padding-left: 15px;
                color: #333333;
                border: 2px solid #B0BEC5;  /* Bordure grise */
            }
            QLineEdit:focus {
                border: 2px solid #004D40;  /* Bordure verte foncée en focus */
            }
        """)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        self.login_button.setStyleSheet("""
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

        self.forgot_password_button = QPushButton("Forgot Password")
        self.forgot_password_button.clicked.connect(self.open_reset_password)
        self.forgot_password_button.setStyleSheet("""
            QPushButton {
                border: none;
                font-size: 12px;
                color: #00796B;
                text-align: center;
            }
            QPushButton:hover {
                text-decoration: underline;
            }
        """)

        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.open_signup)
        self.signup_button.setStyleSheet("""
            QPushButton {
                border: none;
                font-size: 12px;
                color: #00796B;
                text-align: center;
            }
            QPushButton:hover {
                text-decoration: underline;
            }
        """)

        # Création du label pour les messages d'erreur
        self.error_message = QLabel("")
        self.error_message.setStyleSheet("""
            QLabel {
                color: #D32F2F;  /* Rouge */
                font-size: 12px;
                margin-top: 10px;
            }
        """)

        # Ajouter les widgets au layout
        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.error_message)  # Ajout du message d'erreur
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.forgot_password_button)
        self.layout.addWidget(self.signup_button)

        # Appliquer le layout au widget
        self.setLayout(self.layout)

        # Configuration de la connexion série
        try:
            self.serial_port = serial.Serial('COM6', 115200, timeout=1)  # Remplacez 'COM6' par le port approprié
        except serial.SerialException as e:
            QMessageBox.critical(self, "Erreur de connexion série", f"Impossible d'ouvrir le port série : {e}")
            self.serial_port = None

    def set_background_image(self, image_path):
        """Définit l'image de fond pour le widget."""
        self.setStyleSheet(f"""
            QWidget {{
                background-color: #FFFFFF;  /* Blanc */
                color: black;
            }}
        """)

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        user_id = check_login_credentials(email, password)
        if user_id:
            self.sidebar = MySideBar(user_id)  # Passer l'ID utilisateur
            self.sidebar.show()
            self.close()
        else:
            self.show_error_message("Email ou mot de passe incorrect.")

    def open_reset_password(self):
        self.reset_password_window = ResetPasswordWindow(self)  # Pass the current LoginWindow instance
        self.reset_password_window.show()

    def open_signup(self):
        self.signup_window = SignupWindow(self)  # Pass the current LoginWindow instance
        self.signup_window.show()

    def show_error_message(self, message):
        """Affiche un message d'erreur sous les champs de saisie."""
        self.error_message.setText(message)
