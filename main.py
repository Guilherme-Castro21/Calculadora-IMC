import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from design import Ui_MainWindow


def calcula_imc(peso, altura):
    if ',' in peso:
        peso = peso.replace(',', '.')

    if ',' in altura:
        altura = altura.replace(',', '.')

    if altura == '' or peso == '':
        return ''

    try:
        peso = float(peso)
        altura = float(altura)
        if peso < 0 or altura < 0:
            return 'Erro, valores negativos são inválidos'

        imc = peso / altura ** 2
        if imc < 18.5:
            classificacao = 'Magreza'
        elif imc >= 18.5 and imc < 25:
            classificacao = 'Normal'
        elif imc >= 25 and imc < 30:
            classificacao = 'Sobrepeso'
        elif imc >= 30 and imc < 40:
            classificacao = 'Obesidade'
        else:
            classificacao = 'Obesidade Grave'
    except ValueError:
        return 'Erro, digite somente valores válidos'
    except Exception:
        return 'Ocorreu um Erro'

    imc = f'{imc:.2f}'
    imc = imc.replace('.', ',')
    return f' Seu IMC: {imc}\n Classificação: {classificacao}'


class CalculaIMC(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnCalcular.clicked.connect(self.calcula)
        self.btnLimpar.clicked.connect(self.limpar)
        self.btnCalcular.setStyleSheet('* {background: #002276; color: #FFF;}')
        self.btnLimpar.setStyleSheet('* {background: #8E2500; color: #FFF;}')

    def calcula(self):
        peso = self.linePeso.text().strip()
        altura = self.lineAlt.text().strip()
        imc = calcula_imc(peso, altura)
        self.labelResult.setText(imc)
        self.labelResult.setStyleSheet('* {background: #FFF; color: #black;}')

    def limpar(self):
        self.linePeso.setText('')
        self.lineAlt.setText('')
        self.labelResult.setText('')


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    calc = CalculaIMC()
    calc.show()
    qt.exec_()
