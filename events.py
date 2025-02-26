from datetime import datetime


class Event:

    def __init__(self):

        self.name_event: str = ""
        self.date_event: str = ""
        self.event: dict = {}
        self.date_object: datetime = None

    def create_event(self):
        self.name_event = input("Ingrese el nombre del evento: ")
        self.date_event = input("Ingrese la fecha del evento: ")

        self.date_format = "%d-%m-%Y"

        self.date_object = datetime.strptime(self.date_event, self.date_format)

        self.event[self.name_event]=self.date_object

        return self.event

    def view_event(self):
        print(self.event)

    def delete_event(self):

        self.name_event_delete = input("Ingrese el nombre del evento a eliminar: ")
 
        for index,result in enumerate(self.event):
            if self.name_event_delete not in self.event:
                raise ValueError("Evento no encontrado")

        del self.event[self.name_event_delete]

    def update_event(self):

        self.name_event_for_update = input("Ingrese el nombre del evento a Actualizar: ")

        for index, result in enumerate(self.event):
            if self.name_event_for_update not in self.event:
                raise ValueError("Evento no encontrado")

        self.name_event_update = input("Ingrese el nuevo nombre del evento: ")
        self.event[self.name_event_update]=self.date_object
        del self.event[self.name_event_for_update]

        return self.event


event = Event()

while True:
    print("____MENU____")
    print("Crear evento")
    print("Ver eventos")
    print("Eliminar evento")
    print("Actualizar evento")
    print("Salir")

    option = input("Ingrese una opción: ")

    match option:
        case "1":
            event.create_event()
        case "2":
            event.view_event()
        case "3":
            event.delete_event()
        case "4":
            event.update_event()
        case "5":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida")
