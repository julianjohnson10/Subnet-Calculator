class Controller():
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def save(self, value):
        try:
            self.model.ip_addr = value
            self.model.save()
        
        except ValueError as e:
            self.view.show_error(e)