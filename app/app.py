from PySide2 import QtWidgets # QtWidgets est un module qui permet de créer des interfaces graphique
# from script import logging
import currency_converter
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("La fonction a bien été exécutée")

#ma classe
class App(QtWidgets.QWidget): # répresente la fenetre, héritage de QWidget et qui appartient a QtWidgets
    def __init__(self): # méthode init car on veut inialiser notre interface, self représente notre instance de notre fenetre
        super().__init__() # pour appeller ma méthode init de mon QWidget, ca permet d'inialiser ce QWidget à l'intérieur de notre class App
        self.c = currency_converter.CurrencyConverter()# on créer une instance de cette classe CurrencyConverter  
        self.setWindowTitle("Convertisseur de devises") # le nom de la fenetre, on set la méthode setwindowtitle sur l'instance self qui représente notre win et win est une instance de Qwidget
        self.setup_ui() # on appelle cette méthode setup_ui dans la méthode init, ça permet de séparer les méthodes et de pourvoir écrire une autre méthode qui sera ensuite appeller dans le init
        self.setup_connections() # permet de faire des connections avec des widgets comme le click
        self.set_default_values() #inialiser nos widget avec des valeurs par defaut c'est une méthode
        self.setup_css()
        self.resize(500, 50)

# ma méthode de classe
    def setup_ui(self): # interface graphique avec les différents boutons
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

    def set_default_values(self): # la méthode setdefaultvalues
        self.cbb_devisesFrom.addItems(sorted(list(self.c.currencies)))# la méthode addItems permet de rajouter des objets ou valeurs, trié en list
        self.cbb_deviseTo.addItems(sorted(list(self.c.currencies))) # currencies qui sont défini dans la class CurencyConverter, currencies est un set il ne peut pas avoir de doublons
        self.cbb_devisesFrom.setCurrentText("EUR") # affiche par defaut EUR en set
        self.cbb_deviseTo.setCurrentText("EUR")

        self.spn_montant.setRange(1, 1000000) # un range de 1 à 1 millions
        self.spn_montantConverti.setRange(1, 1000000)
        self.spn_montant.setValue(100) # mettre la valeur à 100
        self.spn_montantConverti.setValue(100)

    def setup_connections(self):
        self.cbb_devisesFrom.activated.connect(self.compute) #on connect le signal activated sur notre widget cbb devisefrom et on le connect à self.compute
        self.cbb_deviseTo.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute) # quand t'on change la valeur à l'interieur du spn ça execute la méthode self.compute
        self.btn_inverser.clicked.connect(self.inverser_devise) #

    def setup_css(self):
        self.setStyleSheet("""
        background-color: rgb(30, 30, 30);
        color: rgb(240, 240, 240);
        border: none;
        """)

    def compute(self): # c'est la méthode qu'on appelle quand ton va modifier la valeur ou la devise pour calculer la devise
        montant = self.spn_montant.value()
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_deviseTo.currentText()

        try: # si le try reussi, il n'y aura pas d'erreur et donc le else pourra s'afficher sinon le except print l'erreur
            resultat = self.c.convert(montant, devise_from, devise_to) # utilise une extension de currency_converter, la fonction convert qui prend le montant qu'on veut convertir, devise from le montant à partir duquel on veut convertir et deviseto c'est le montant dans laquel on veut convertir
        except currency_converter.currency_converter.RateNotFoundError:
            print("La conversion n'est pas disponible.")
        else:
            self.spn_montantConverti.setValue(resultat) # on set le résultat à montant converti

    def inverser_devise(self): # méthode permettant d'inverser la devise
        devise_from = self.cbb_devisesFrom.currentText() # on recupere les deux valeurs 
        devise_to = self.cbb_deviseTo.currentText()

        self.cbb_devisesFrom.setCurrentText(devise_to) #on inverse les devise devisefrom qui devient deviseto etc
        self.cbb_deviseTo.setCurrentText(devise_from)

        self.compute() # on appelle la méthode compute qui permet de convertir une devise en une autre devise et permet de calculer le montant de la nouvelle devise

# mes instances
app = QtWidgets.QApplication([]) # l'application est créer par la méthode Qapplication puis éxecuter avec app.exec_()
win = App() # permet de créer une fenetre windows, je fait une instance de ma class App que je récupere dans win
win.show() # permet d'afficher l'app
app.exec_()