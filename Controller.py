import View, Model
class Controller():
    def __init__(self, parent):
        self.parent = parent
        self.model = Model(self)
        self.view = View(self)
    
    #events
    def okButton(self, value):
        try:
            self.model.ip_addr = value
            self.model.save()
        
        except ValueError as e:
            self.view.show_error(e)