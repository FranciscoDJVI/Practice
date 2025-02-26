from datetime import datetime


class Event:

    def __init__(self):

        self.name_event: str = ""
        self.date_event: str = ""
        self.event: dict = {}
        self.list_events: list = []
        self.count: int = 0
        self.new_event: str = ""
        self.date_object: datetime = None

    def create_event(self):

        self.name_event = input("Ingrese el nombre del evento: ")
        self.date_event = input("Ingrese la fecha del evento: ")

        self.date_format = "%d-%m-%Y"

        self.date_object = datetime.strptime(self.date_event, self.date_format)
        
        self.event[self.name_event]=self.date_object
        self.list_events.append(self.event)

        #Comprobracion para evitar eventos duplicado dentro de la lista.
        if self.event not in self.list_events:
            raise ValueError("Evento no encontrado")

        return self.list_events

    def view_event(self):

        if len(self.list_events) == 0:
            print("No hay enventos para mostrar")
        
        for index, event in enumerate(self.list_events):
            print(f"Index:{index} --> Event:{event}")

    def delete_event(self):

        if len(self.list_events) == 0:
            print("No hay eventos guardados para borrar")
        else:
            self.index_event_delete = int(input("Ingrese indice del evento a eliminar: "))
            for index, event in enumerate(self.list_events):
                if self.index_event_delete != index:
                    raise ValueError("Evento no encontrado")

            del self.list_events[index]

    def update_event(self):

        self.index_event_for_update = int(input("Ingrese el indice del evento a Actualizar: "))
        for index, event in enumerate(self.list_events):
            if self.index_event_for_update != index:
                print("Evento no encontrado")
            else:
                del self.list_events[self.index_event_for_update]

                self.name_event_update = input("Ingrese el nuevo nombre para el evento: ")
                self.date_event_update = input("Ingrese la nueva fecha para el evento: ")

                self.date_format = "%d-%m-%Y"

                self.date_object = datetime.strptime(self.date_event_update, self.date_format)

                new_event = {self.name_event_update: self.date_object}
                self.list_events.append(new_event)

        return self.list_events


event = Event()

while True:
    print("-----MENU-----\n")
    print("1.Crear evento")
    print("2.Ver eventos")
    print("3.Eliminar evento")
    print("4.Actualizar evento")
    print("5.Salir\n")

    option = input("\nIngrese una opción: ")

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
