from View.base_screen import BaseScreenView


class ServerScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def _halamanutama(self,*args):
        self.manager_screens.current='server screen'


from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from Utility.Table  import Table

from kivymd.uix.behaviors import RectangularRippleBehavior
# import importlib
# importlib.import_module("kivymd.uix.behaviors")
class IconCustomButton( RectangularRippleBehavior,ButtonBehavior, Image):
    pass

class TableInherited(Table):
    
    def __init__(self,*args,**kwrgs):
        super().__init__(*args,**kwrgs)
        pass