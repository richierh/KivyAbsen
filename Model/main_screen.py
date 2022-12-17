from Model.base_model import BaseScreenModel,Database


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.database = MainScreenDatabase()
        pass

    def check_all(self,*args,**kwargs):
        with Database() as db:
            self.data = db.get_data_all()
        return self.data     

    def data_validation_status(self,username,password):
        self.username=username
        self.password=password

        with self.database as db:
            self.validate=db.query_username_password(self.username,self.password)

        if bool(self.validate):
            self.data_validation = True
            with self.database as db:
                self.role = db.get_role(self.validate[0][2])
        else:
            self.role=None
            self.data_validation=False
        self.notify_observers('main screen')
    
    def data_validation_status_check(self):
        return self.role,self.data_validation



class MainScreenDatabase(Database):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
    def query_username_password(self,username,password):
        self.sql_cmd='''
        SELECT id,
            username,
            password,
            role
        FROM Person
        WHERE username=? AND password=?
        '''
        self.data=self.cur.execute(self.sql_cmd,(username,password)).fetchall()
        return self.data


    def get_role(self,id):
        self.id=self.data[0][3]
        self.sql_cmd='''
        SELECT role
        FROM Role
        WHERE id=?
        '''        
        self.data=self.cur.execute(self.sql_cmd,(self.id)).fetchall()
        return self.data[0][0]