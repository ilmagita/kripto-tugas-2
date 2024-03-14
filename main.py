import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5 import uic
from datetime import datetime

from ciphers.rc4 import *

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('windows/main.ui', self)

        # init
        self.filePath = ''
        self.fileName = ''
        self.fileType = ''
        self.fileBaseName = ''
        self.outputVar = ''
        self.index = 0

        # hide the options for selecting from file on initial load
        self.browseFileButton.hide()
        self.fileNameTextBox.hide()
        self.fileNameLabel.hide()
        self.fileSavedAutomaticallyText.hide()

        # connection slots
        self.inputSelection.currentIndexChanged.connect(self.onInputSelectionIndexChanged)
        self.browseFileButton.clicked.connect(self.onBrowseFileButtonClicked)
        self.encryptButton.clicked.connect(self.onEncryptButtonClicked)
        self.decryptButton.clicked.connect(self.onDecryptButtonClicked)
        self.saveOutputButton.clicked.connect(self.onSaveOutputButtonClicked)

    def writeFileContents(self, file_path, contents):
        with open(file_path, 'w') as file:
            file.write(contents)

    def onInputSelectionIndexChanged(self, index):
        self.index = index

        if index == 0: # text
            self.browseFileButton.hide()
            self.fileNameTextBox.hide()
            self.fileNameLabel.hide()
            self.saveOutputButton.show()
            self.fileSavedAutomaticallyText.hide()

            self.inputTextBox.show()
            self.inputTextLabel.show()
            
        else: # file
            self.browseFileButton.show()
            self.fileNameTextBox.show()
            self.fileNameLabel.show()
            self.saveOutputButton.hide()

            self.inputTextBox.hide()
            self.inputTextLabel.hide()

    def onBrowseFileButtonClicked(self):
        file_dialog = QFileDialog(self)
        filepath, _ = file_dialog.getOpenFileName(self, "Open File")

        if filepath:
            # Read the file content
            with open(filepath, 'rb') as file:
                contents = file.read()

            # Set the text box to file name
            self.fileNameTextBox.setText(filepath)
            self.filePath = filepath
            self.fileName = get_file_name(filepath)
            self.fileType = get_file_type(filepath)
            self.fileBaseName = get_base_file_name(filepath)

            # Close file dialog
            file_dialog.reject()
            file.close()

            if self.fileType == '.txt':
                self.inputTextBox.show()
                self.inputTextLabel.show()
                self.outputTextBox.show()
                self.saveOutputButton.show()
                self.fileSavedAutomaticallyText.hide()

                self.inputTextBox.setPlainText(read_text_file(filepath))

            else:
                self.fileSavedAutomaticallyText.show()

    def onEncryptButtonClicked(self):
        input_key = self.keyTextBox.toPlainText()

        if not input_key.strip():
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Error')
            msg_box.setText('You must enter a key!')
            msg_box.exec_()
            return

        if self.index == 0: # text
            input_text = self.inputTextBox.toPlainText()
            output = encryption(input_text, input_key)
            self.outputTextBox.setPlainText(output)
            self.outputVar = output

        else: # file
            if self.fileType == '.txt':
                output = rc4_enc_text_file(self.filePath, input_key)
                self.outputTextBox.setPlainText(output)
                self.outputVar = output
            else:
                options = QFileDialog.Options()
                original_file_extension = f"All Files (*{self.fileType})"
                save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", original_file_extension, options=options)

                if save_path:
                    rc4_binary_file(self.filePath, input_key, save_path)

                    msg_box = QMessageBox()
                    msg_box.setWindowTitle('Encryption Saved')
                    msg_box.setText(f'File encrypted as {save_path}.')
                    msg_box.exec_()

    def onDecryptButtonClicked(self):
        input_key = self.keyTextBox.toPlainText()

        if not input_key.strip():
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Error')
            msg_box.setText('You must enter a key!')
            msg_box.exec_()
            return

        if self.index == 0: # text
            input_text = self.inputTextBox.toPlainText()
            output = decryption(input_text, input_key)
            self.outputTextBox.setPlainText(output)
            self.outputVar = output

        else: # file
            if self.fileType == '.txt':
                output = rc4_dec_text_file(self.filePath, input_key)
                self.outputTextBox.setPlainText(output)
                self.outputVar = output
            else:
                options = QFileDialog.Options()
                original_file_extension = f"All Files (*{self.fileType})"
                save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", original_file_extension, options=options)

                if save_path:
                    rc4_binary_file(self.filePath, input_key, save_path)

                    msg_box = QMessageBox()
                    msg_box.setWindowTitle('Decryption Saved')
                    msg_box.setText(f'File decrypted as {save_path}.')
                    msg_box.exec_()
                

    def onSaveOutputButtonClicked(self):
        """
        Only for saving ciphertext from keyboard or .txt files.
        """
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime('%Y%m%d_%H%M%S')

        if self.index == 0: # text
            options = QFileDialog.Options()
            save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)", options=options)

            if save_path:
                self.writeFileContents(save_path, self.outputVar)

                msg_box = QMessageBox()
                msg_box.setWindowTitle('Output Saved')
                msg_box.setText(f'File saved as {save_path}.')
                msg_box.exec_()

        else: # file
            if self.fileType == '.txt':
                options = QFileDialog.Options()
                save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)", options=options)

                if save_path:
                    self.writeFileContents(save_path, self.outputVar)

                    msg_box = QMessageBox()
                    msg_box.setWindowTitle('Output Saved')
                    msg_box.setText(f'File saved as {save_path}.')
                    msg_box.exec_()

            # else:
            #     options = QFileDialog.Options()
            #     original_file_extension = f"All Files (*{self.fileType})"
            #     save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", original_file_extension, options=options)

            #     if save_path:
            #         save_binary_file

            #         msg_box = QMessageBox()
            #         msg_box.setWindowTitle('Output Saved')
            #         msg_box.setText(f'File saved as {save_path}.')
            #         msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())