import importlib

import View.EmployeeScreen.employee_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.EmployeeScreen.employee_screen)




class EmployeeScreenController:
    """
    The `EmployeeScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.employee_screen.EmployeeScreenModel
        self.view = View.EmployeeScreen.employee_screen.EmployeeScreenView(controller=self, model=self.model)

    def get_view(self) -> View.EmployeeScreen.employee_screen:
        return self.view
