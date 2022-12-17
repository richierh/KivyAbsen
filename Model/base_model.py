# The model implements the observer pattern. This means that the class must
# support adding, removing, and alerting observers. In this case, the model is
# completely independent of controllers and views. It is important that all
# registered observers implement a specific method that will be called by the
# model when they are notified (in this case, it is the `model_is_changed`
# method). For this, observers must be descendants of an abstract class,
# inheriting which, the `model_is_changed` method must be overridden.


class BaseScreenModel:
    """Implements a base class for model modules."""

    _observers = []

    def add_observer(self, observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self, name_screen: str) -> None:
        """
        Method that will be called by the observer when the model data changes.

        :param name_screen:
            name of the view for which the method should be called
            :meth:`model_is_changed`.
        """

        for observer in self._observers:
            if observer.name == name_screen:
                observer.model_is_changed()
                break
import sqlite3
import os
from pathlib import Path

class Database():
    """sqlite3 database class that holds testers jobs"""

    def __init__(self):
        """Initialize db class variables"""
        # self.parent=parent
        # self.name_file=parent
        pass

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def execute(self, new_data):
        """execute a row of data to current cursor"""
        self.cur.execute(new_data)

    def executemany(self, many_new_data):
        """add many new data to database in one go"""
        self.create_table()
        self.cur.executemany('REPLACE INTO jobs VALUES(?, ?, ?, ?)', many_new_data)

    def create_table(self):
        """create a database table if it does not exist already"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS jobs(title text, \
                                                            job_id integer PRIMARY KEY, 
                                                            company text,
                                                            age integer)''')

    def commit(self):
        """commit changes to database"""
        self.connection.commit()

    def get_data_all(self):
        self.cur.execute('''
        SELECT * FROM [jobs]
        ''')
        self.data = self.cur.fetchall()
        return self.data
  
    def __enter__(self,*args):
        self.konek=Database()
        self.name_file = self.konek='core.db'
        DB_LOCATION = Path(os.getcwd(),"Model",self.name_file)
        self.connection = sqlite3.connect(DB_LOCATION)
        self.cur = self.connection.cursor()

        return self

    def __exit__(self, ext_type, exc_value, traceback):
        # self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

