from View.base_screen import BaseScreenView
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.properties import ObjectProperty,StringProperty,BooleanProperty
from kivymd.uix.list import OneLineAvatarListItem
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from Utility.Table  import Table
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class AbsenScreenView(BaseScreenView):
    dialog=ObjectProperty()
    dialog2=ObjectProperty()
    img = StringProperty('assets/images/off-button.png')
    status=BooleanProperty(False)
    lampu=ObjectProperty()
    textlampu=StringProperty('Mati')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # self.datatable = TableInherited(table_columns=6,table_rows=6,table_height =500,table_width=800,header_color=[0,1,1,.3])
        # self.datatable.addRow(["Data","Data2","Data3","Data4","Data5","Data6"])
        # self.datatable.addHeader(["a","b","c","d","e","f","g"])
        # self.children[-1].children[0].add_widget(self.datatable)
        # import pdb
        # pdb.set_trace()
        self.layout = MDBoxLayout(orientation='vertical')
        # self.children[0].children[0]
        # print(self.children[0].children[0].children[0])
        self.data_tables = MDDataTable(
            use_pagination=True,
            check=True,
            column_data=[
                ("No.", dp(30)),
                ("Nama", dp(30)),
            #     ("Signal Name", dp(60), self.sort_on_signal),
            #     ("Severity", dp(30)),
            #     ("Stage", dp(30)),
            #     ("Schedule", dp(30), self.sort_on_schedule),
            #     ("Team Lead", dp(30), self.sort_on_team),
            ],            
            # sorted_on="Nama",
            sorted_order="ASC",
            elevation=2,
            )
        self.children[0].children[0].add_widget(self.data_tables)

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    def sort_on_signal(self,*args):
        pass
    def sort_on_schedule(self,*args):
        pass
    def sort_on_team(self,*args):
        pass
    def click(self,status):
        self.status = status
        print(self.status)
        if self.status:
            self.img = 'assets/images/off-button.png'
            self.status=False
            self.textlampu="Mati"
            self.no = 1
            self.nama ='andid'
            data=((self.no),(self.nama))
            self.data_tables.add_row(data)


            # self.label =MDLabel(text='jjj')
            # self.children[0].children[0].children[0].add_widget(self.label)
        else:
            self.img = 'assets/images/on-button.png'
            self.status=True
            self.textlampu='Hidup'
        print('dd')
        
        pass
    def open(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Set backup account",
                type="simple",
                items=[
                    Item2(text="user01@gmail.com", icong="language-python"),
                    Item(text="user02@gmail.com", sourced="data/logo/kivy-icon-128.png"),
                    Item2(text="Logout", icong="logout",on_release=self._pindahscreen),

                ],
            )
        self.dialog.open()
        print("open option")

    def _keluar(self):
        # self.manager_screens.current='main screen'
        from kivymd.uix.dialog import MDDialog

        if not self.dialog2:
            self.dialog2 = MDDialog(
                text="Apakah anda akan keluar aplikasi?",
                buttons=[
                    MDFlatButton(
                        text="Tidak",
                        on_release=self._tutup

                        # theme_text_color="Custom",
                        # text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="Iya",
                        on_release=self._keluaraplikasi
                        # theme_text_color="Custom",
                        # text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog2.open()
        # import pdb
        # pdb.set_trace()
    def _keluaraplikasi(self,*args):
        self.dialog2.dismiss()
        self.app.stop()

    def _tutup(self,*args):
        self.dialog2.dismiss()
    
    def _pindahscreen(self,*args):
        if self.dialog:
            self.dialog.dismiss()
        self.manager_screens.current='main screen'
    
    def _halamanutama(self,*args):
        self.manager_screens.current='absen screen'
    # def laporan(self):

class Item(OneLineAvatarListItem):
    divider = None
    sourced = StringProperty()
class Item2(OneLineAvatarListItem):
    divider = None
    icong=StringProperty()

from kivymd.uix.behaviors import RectangularRippleBehavior
# import importlib
# importlib.import_module("kivymd.uix.behaviors")
class IconCustomButton( RectangularRippleBehavior,ButtonBehavior, Image):
    pass

class TableInherited(Table):
    
    def __init__(self,*args,**kwrgs):
        super().__init__(*args,**kwrgs)
        pass