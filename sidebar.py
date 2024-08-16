import sqlite3
from PySide6.QtWidgets import QMainWindow, QMessageBox
from sidbbar_ui import Ui_MainWindow 
import serial

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")

        # Cacher le widget par défaut
        self.icon_name_widget.setHidden(True)

        # Connecter les signaux des boutons de la sidebar aux méthodes correspondantes
        self.auto1.clicked.connect(self.switch_to_automatiquePage)
        self.auto2.clicked.connect(self.switch_to_automatiquePage)
        self.man1.clicked.connect(self.switch_to_manuelPage)
        self.man2.clicked.connect(self.switch_to_manuelPage)
        self.noti1.clicked.connect(self.switch_to_notificationsPage)
        self.noti2.clicked.connect(self.switch_to_notificationsPage)
        self.sitt1.clicked.connect(self.switch_to_sittingPage)
        self.sitt2.clicked.connect(self.switch_to_sittingPage)
        self.help1.clicked.connect(self.switch_to_helpPage)
        self.help2.clicked.connect(self.switch_to_helpPage)
        self.p.clicked.connect(self.switch_to_userPage)
        self.profile1.clicked.connect(self.switch_to_userPage)
        self.profile2.clicked.connect(self.switch_to_userPage)
        self.acc.clicked.connect(self.switch_to_firstPage)

        self.current_user_id = user_id  # Utiliser l'ID utilisateur passé
        self.serial_port = None

        # Connecter le bouton "change" à la méthode update_user_data
        self.change.clicked.connect(self.update_user_data)

        # Afficher les données utilisateur dès l'initialisation
        self.display_user_data()

    def switch_to_automatiquePage(self):
        self.stackedWidget.setCurrentIndex(1)
        self.check_robot_connection()  # Vérifier la connexion du robot lorsque la page est affichée

    def switch_to_manuelPage(self):
        self.stackedWidget.setCurrentIndex(2)
        self.check_robot_connection()  # Vérifier la connexion du robot lorsque la page est affichée

    def switch_to_notificationsPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_sittingPage(self):
        self.stackedWidget.setCurrentIndex(4)
        self.check_robot_connection()

    def switch_to_helpPage(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_userPage(self):
        self.stackedWidget.setCurrentIndex(6)
    
    def switch_to_firstPage(self):
        self.stackedWidget.setCurrentIndex(7)

    def check_robot_connection(self):
        if self.serial_port is None:
            # Initialiser la connexion série
            try:
                self.serial_port = serial.Serial('COM6', 115200, timeout=1)
                self.serial_port.write(b'ping')  # Envoyer un ping pour vérifier la connexion
                response = self.serial_port.readline()
                if response.strip() == b'Hello, I am OK':
                    self.activate_buttons(True)
                else:
                    self.activate_buttons(False)
            except serial.SerialException as e:
                QMessageBox.critical(self, "Erreur", f"Échec de la connexion au robot : {e}")
                self.activate_buttons(False)
        else:
            self.activate_buttons(True)

    def activate_buttons(self, active):
        self.activateButton.setEnabled(active)  # Activer ou désactiver le bouton d'activation
        self.evacuateButton.setEnabled(active)  # Activer ou désactiver le bouton d'évacuation
        self.takeButton.setEnabled(active)  # Activer ou désactiver le bouton de prise
        self.pumpingButton.setEnabled(active)  # Activer ou désactiver le bouton de pompage
        self.homeButton.setEnabled(active)  # Activer ou désactiver le bouton de retour à la position initiale

    def update_user_data(self):
        if self.current_user_id is not None:
            new_firstname = self.firstname.text() if hasattr(self, 'firstname') else None
            new_lastname = self.lastname.text() if hasattr(self, 'lastname') else None
            new_email = self.email_p.text() if hasattr(self, 'email_p') else None
            new_password = self.password_p.text() if hasattr(self, 'password_p') else None
            new_cin = self.cin_p.text() if hasattr(self, 'cin_p') else None

            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()

            if new_firstname:
                cursor.execute('UPDATE users SET firstname = ? WHERE id = ?', (new_firstname, self.current_user_id))
            if new_lastname:
                cursor.execute('UPDATE users SET lastname = ? WHERE id = ?', (new_lastname, self.current_user_id))
            if new_email:
                cursor.execute('UPDATE users SET email = ? WHERE id = ?', (new_email, self.current_user_id))
            if new_password:
                cursor.execute('UPDATE users SET password = ? WHERE id = ?', (new_password, self.current_user_id))
            if new_cin:
                cursor.execute('UPDATE users SET cin = ? WHERE id = ?', (new_cin, self.current_user_id))

            conn.commit()
            conn.close()
            
            QMessageBox.information(self, 'Succès', 'Informations utilisateur mises à jour avec succès.')
        else:
            QMessageBox.warning(self, 'Erreur', 'Aucun utilisateur sélectionné.')

    def display_user_data(self):
        if self.current_user_id is not None:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute('SELECT firstname, lastname, email, cin FROM users WHERE id = ?', (self.current_user_id,))
            user = cursor.fetchone()
            conn.close()

            if user:
                self.user_firstname.setText(user[0])
                self.user_lastname.setText(user[1])
                self.user_email.setText(user[2])
                self.user_cin.setText(user[3])
            else:
                QMessageBox.warning(self, 'Erreur', 'Utilisateur non trouvé.')
        else:
            QMessageBox.warning(self, 'Erreur', 'Aucun utilisateur sélectionné.')
