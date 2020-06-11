from Loader import Loader
from analyser import Lotofacil


load = Loader('lotofacil')
analyse = Lotofacil(load.data)
analyse.save_html()
print(analyse.best_game())
print(analyse.worst_game())
