# brief-MoteurRechercheBot
le Brief consiste à scrapter des informations d'es sites web pour créer une base de données destinée à la recherche d'emploi
On utilise le module scrapy du python et mongodb:
- Exécuter le fichier python flashbot_essai_01.py à l'aide de la commande suivante depuis votre terminal:
scrapy crawl flashbot_essai_01 -o
- La connexion avec mongodb est assurée par le fichier pipelines.py
- Les paramètres du scraping telques : le user-agent, les délais de téléchargement, les délais d'attente sont configurées dans le fichier setting.py
