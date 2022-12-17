from View.base_screen import BaseScreenView
from kivy.properties import ObjectProperty

class MainScreenView(BaseScreenView):

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.role,self.validate = self.model.data_validation_status_check()
        if self.validate and self.role=='superuser':
            self.manager_screens.current='server screen'
        if self.validate and self.role=='user':
            self.manager_screens.current='absen screen'
        


    def login(self,username,password):
        self.username = username.text
        self.password = password.text
        # print(self.username)
        # import pdb
        # pdb.set_trace()
        # self.manager_screens.current='server screen'

        # print(self.controller.get_view())
        self.controller.set_view(self.username,self.password)

        # print(self.controller.view)        
        # if self.validation(self.username,self.password):
        #     self.manager_screens.current='server screen'

        # else:
        #     self.manager_screens.current="absen screen"
        print('ddf')
        # print(self.controller.get_data_all())

        


    def validation(self,username,password):
        self.username = username
        self.password = password
        if self.username=='' and self.password=='':
            return True
        return False
