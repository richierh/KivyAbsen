# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
from Model.absen_screen import AbsenScreenModel
from Controller.absen_screen import AbsenScreenController
from Model.server_screen import ServerScreenModel
from Controller.server_screen import ServerScreenController
from Model.time_screen import TimeScreenModel
from Controller.time_screen import TimeScreenController
from Model.report_screen import ReportScreenModel
from Controller.report_screen import ReportScreenController
from Model.settings_screen import SettingsScreenModel
from Controller.settings_screen import SettingsScreenController
from Model.profil_screen import ProfilScreenModel
from Controller.profil_screen import ProfilScreenController
from Model.employee_screen import EmployeeScreenModel
from Controller.employee_screen import EmployeeScreenController
from Model.registration_screen import RegistrationScreenModel
from Controller.registration_screen import RegistrationScreenController

screens = {
    'main screen': {
        'model': MainScreenModel,
        'controller': MainScreenController,
    },
    'settings screen': {
        'model': SettingsScreenModel,
        'controller': SettingsScreenController,
    },
    'registration screen': {
        'model': RegistrationScreenModel,
        'controller': RegistrationScreenController,
    },
    'time screen': {
        'model': TimeScreenModel,
        'controller': TimeScreenController,
    },
    'absen screen': {
        'model': AbsenScreenModel,
        'controller': AbsenScreenController,
    },
    'employee screen': {
        'model': EmployeeScreenModel,
        'controller': EmployeeScreenController,
    },
    'profil screen': {
        'model': ProfilScreenModel,
        'controller': ProfilScreenController,
    },
    'server screen': {
        'model': ServerScreenModel,
        'controller': ServerScreenController,
    },
    'report screen': {
        'model': ReportScreenModel,
        'controller': ReportScreenController,
    },
}