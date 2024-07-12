from simple_screen import Screen_manager
from app.controladores import Zoo

with Screen_manager:
    zoo = Zoo()
    zoo.run()
