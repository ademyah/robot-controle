from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Qt
from database import add_user
import sqlite3

class SignupWindow(QWidget):
    def __init__(self, login_window=None):
        super().__init__()
        self.login_window = login_window
        self.setWindowTitle("Sign Up")
        self.setFixedSize(500, 600)  # Ajustez la taille de la fenêtre si nécessaire

        # Configuration du dégradé de fond
        self.set_background_gradient()

        # Création du layout principal
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(30, 30, 30, 30)
        self.layout.setSpacing(20)
        self.layout.setAlignment(Qt.AlignCenter)

        # Création des widgets
        self.firstname_label = QLabel("First Name")
        self.firstname_input = QLineEdit()
        self.lastname_label = QLabel("Last Name")
        self.lastname_input = QLineEdit()
        self.email_label = QLabel("Email")
        self.email_input = QLineEdit()
        self.password_label = QLabel("Password")
        self.password_input = QLineEdit()
        self.cin_label = QLabel("CIN")
        self.cin_input = QLineEdit()
        self.signup_button = QPushButton("Sign Up")
        self.back_button = QPushButton("Back")  # Ajout du bouton "Back"

        self.signup_button.clicked.connect(self.signup)
        self.back_button.clicked.connect(self.back_to_login)  # Connexion au bouton "Back"

        # Appliquer le style aux boutons
        self.signup_button.setStyleSheet(self.get_button_style())
        self.back_button.setStyleSheet(self.get_back_button_style())

        # Ajouter les widgets au layout
        self.layout.addWidget(self.firstname_label)
        self.layout.addWidget(self.firstname_input)
        self.layout.addWidget(self.lastname_label)
        self.layout.addWidget(self.lastname_input)
        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.cin_label)
        self.layout.addWidget(self.cin_input)
        self.layout.addWidget(self.signup_button)
        self.layout.addWidget(self.back_button)  # Ajouter le bouton "Back"

        # Appliquer le layout au widget
        self.setLayout(self.layout)

    def set_background_gradient(self):
        """Définit un dégradé de fond pour le widget."""
        self.setStyleSheet("""
            QWidget {
                background: linear-gradient(135deg, #E0F7FA, #A5D6A7, #E0F7FA);  /* Dégradé du bleu ciel au vert et retour au bleu ciel */
                color: black;
            }
        """)

    def get_button_style(self):
        """Retourne le style pour les boutons principaux."""
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

    def signup(self):
        firstname = self.firstname_input.text()
        lastname = self.lastname_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        cin = self.cin_input.text()

        try:
            add_user(firstname, lastname, email, password, cin)
            QMessageBox.information(self, "Success", "User registered successfully!")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Error", "Email already exists.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def back_to_login(self):
        """Retourne à la fenêtre de connexion."""
        if self.login_window:
            self.login_window.show()
        self.close()
