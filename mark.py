import string
import random
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QCheckBox,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QSpacerItem,
    QSizePolicy,
)
from PyQt5.QtGui import QGuiApplication, QFont


class MainApp(QWidget):
    def __init__(self, window_title: str, size_w: int, size_h: int):
        """
        Базовий клас для створення вікна
        """
        super().__init__()
        self.setWindowTitle(window_title)
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.resize(size_w, size_h)
        self.show()


class FirstApp(MainApp):
    def __init__(self, window_title: str, size_w: int, size_h: int):
        super().__init__(window_title, size_w, size_h)

        # Покращений стиль
        self.setStyleSheet("""
            QWidget {
                background-color: #1E1E2F;  /* Темний фон */
                color: white;  /* Основний колір тексту */
                font-family: "Arial";  /* Шрифт */
            }
            QLabel {
                font-size: 16px;
            }
            QLineEdit {
                background-color: #2B2B3C;
                color: #FFD700;  /* Золотий текст */
                border: 1px solid #FFD700;
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
            }
            QCheckBox {
                font-size: 14px;
            }
            QPushButton {
                background-color: #5A5A8F;  /* Темно-синя кнопка */
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #6B6BAF;  /* Світліший варіант при наведенні */
            }
        """)

        # --- Поля введення ---
        self.h_layout2 = QHBoxLayout()
        self.v_layout.addLayout(self.h_layout2)

        label_len = QLabel("Довжина пароля:")
        label_len.setFont(QFont("Arial", 14))
        self.h_layout2.addWidget(label_len)

        self.len_field = QLineEdit()
        self.len_field.setText("0")
        self.h_layout2.addWidget(self.len_field)

        # --- Поля відображення ---
        out_label = QLabel("Ваш пароль:")
        out_label.setFont(QFont("Arial", 14))
        self.h_layout.addWidget(out_label)

        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)
        self.h_layout.addWidget(self.password_display)

        # --- Опції ---
        self.options_layout = QVBoxLayout()
        self.v_layout.addLayout(self.options_layout)

        self.use_digits = QCheckBox("Цифри (0-9)")
        self.use_digits.setChecked(True)
        self.options_layout.addWidget(self.use_digits)

        self.use_upper_eng = QCheckBox("Англійські великі літери (A-Z)")
        self.options_layout.addWidget(self.use_upper_eng)

        self.use_lower_eng = QCheckBox("Англійські малі літери (a-z)")
        self.options_layout.addWidget(self.use_lower_eng)

        self.use_upper_ukr = QCheckBox("Українські великі літери (А-Я)")
        self.options_layout.addWidget(self.use_upper_ukr)

        self.use_lower_ukr = QCheckBox("Українські малі літери (а-я)")
        self.options_layout.addWidget(self.use_lower_ukr)

        self.use_chinese = QCheckBox("Китайські символи (汉字)")
        self.options_layout.addWidget(self.use_chinese)

        self.use_german = QCheckBox("Німецькі літери (ÄÖÜäöüß)")
        self.options_layout.addWidget(self.use_german)

        # --- Кнопки ---
        self.h_layout_buttons = QHBoxLayout()
        self.v_layout.addLayout(self.h_layout_buttons)

        self.generate_button = QPushButton("Генерувати")
        self.generate_button.clicked.connect(self.generate_password)
        self.h_layout_buttons.addWidget(self.generate_button)

        self.copy_button = QPushButton("Скопіювати")
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.h_layout_buttons.addWidget(self.copy_button)

        self.switch_language_button = QPushButton("Перекласти (EN/UA)")
        self.switch_language_button.clicked.connect(self.switch_language)
        self.h_layout_buttons.addWidget(self.switch_language_button)

        # Додаткові відступи для кращого вигляду
        self.v_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.language = "UA"

    def generate_password(self):
        """
        Генерація пароля.
        """
        try:
            length = int(self.len_field.text())
        except ValueError:
            self.password_display.setText("Некоректна довжина!")
            return

        if length <= 0:
            self.password_display.setText("Довжина повинна бути > 0!")
            return

        chars = ""
        if self.use_digits.isChecked():
            chars += string.digits
        if self.use_upper_eng.isChecked():
            chars += string.ascii_uppercase
        if self.use_lower_eng.isChecked():
            chars += string.ascii_lowercase
        if self.use_upper_ukr.isChecked():
            chars += "АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
        if self.use_lower_ukr.isChecked():
            chars += "абвгдеєжзиіїйклмнопрстуфхцчшщьюя"
        if self.use_chinese.isChecked():
            chars += "汉字漢字你好世界"
        if self.use_german.isChecked():
            chars += "ÄÖÜäöüß"

        if not chars:
            self.password_display.setText("Оберіть опцію!")
            return

        password = "".join(random.choice(chars) for _ in range(length))
        self.password_display.setText(password)

    def copy_to_clipboard(self):
        """
        Копіює пароль у буфер обміну.
        """
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(self.password_display.text())

    def switch_language(self):
        """
        Перемикання мови інтерфейсу.
        """
        if self.language == "UA":
            self.language = "EN"
            self.setWindowTitle("Password Generator")
            self.generate_button.setText("Generate")
            self.copy_button.setText("Copy")
            self.switch_language_button.setText("Translate (EN/UA)")
        else:
            self.language = "UA"
            self.setWindowTitle("Генератор паролів")
            self.generate_button.setText("Генерувати")
            self.copy_button.setText("Скопіювати")
            self.switch_language_button.setText("Перекласти (EN/UA)")


if __name__ == "__main__":
    app = QApplication([])
    window = FirstApp("Генератор паролів", 800, 400)
    app.exec_()