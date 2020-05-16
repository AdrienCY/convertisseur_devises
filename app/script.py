import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("La fonction a bien été exécutée")