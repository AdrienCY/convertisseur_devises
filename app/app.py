from PySide2 import QtWidgets # QtWidgets est un module qui permet de créer des interfaces graphique
# from script import logging

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("La fonction a bien été exécutée")


class App(QtWidgets.QWidget): # répresente la fenetre, héritage de QWidget et qui appartient a QtWidgets
    def __init__(self): # méthode init car on veut inialiser notre interface, self représente notre instance de notre fenetre
        super().__init__() # pour appeller ma méthode init de mon QWidget, ca permet d'inialiser ce QWidget à l'intérieur de notre class App
        self.setWindowTitle("Convertisseur de devises") # le nom de la fenetre, on set la méthode setwindowtitle sur l'instance self qui représente notre win et win est une instance de Qwidget
        self.setup_ui() # on appelle cette méthode setup_ui dans la méthode init, ça permet de séparer les méthodes et de pourvoir écrire une autre méthode qui sera ensuite appeller dans le init

    def setup_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self) # les layout permet de positionner différent widget, on créer un widget horizontal, la méthode QHBoxLayout attends le parent(self) pour parenté notre layout à notre interface
        self.cbb_devisesFrom = QtWidgets.QComboBox() # combobox est un menu déroulant qui permet d'afficher les différentes devises, pas besoin de le parenté car il sera rajouter à notre layout à la fin
        self.spn_montant = QtWidgets.QSpinBox() #spinbox qui permet de rentrer une valeur
        self.cbb_deviseTo = QtWidgets.QComboBox() # la devise qu'on veut convertir le montant
        self.spn_montantConverti = QtWidgets.QSpinBox() # renvoi la valeur du montant converti
        self.btn_inverser = QtWidgets.QPushButton("Inverser devises") # un bouton qui permet d'inverser la devise

        self.layout.addWidget(self.cbb_devisesFrom) # permet d'ajouter nos widget dans notre layout et on insere nos widget dans () qui après renvoi au self.layout parenté par self dans notre interface
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_deviseTo)
        self.layout.addWidget(self.spn_montantConverti)
        self.layout.addWidget(self.btn_inverser)

        

app = QtWidgets.QApplication([]) # l'application est créer par la méthode Qapplication puis éxecuter avec app.exec_()
win = App() # permet de créer une fenetre windows, je fait une instance de ma class App que je récupere dans win
win.show() # permet d'afficher l'app
app.exec_()