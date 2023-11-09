from datetime import datetime

class Service:
    """
    DocString
    """
    def __init__(self,
		      client_name:str,
		      service_name:str,
		      pay_date:datetime,
		      pay_type:str,
		      hairdresser:str
		     ) -> None:
        self.__client_name = client_name
        self.__service_name = service_name
        self.__pay_date = pay_date
        self.__pay_type = pay_type
        self.__hairdresser = hairdresser
		
    @property
    def client_name(self):
       return self.__client_name

    @client_name.setter
    def client_name(self, client_name):
       self.__client_name = client_name		 

    @property
    def service_name(self):
       return self.__service_name

    @service_name.setter
    def service_name(self, service_name):
       self.__service_name = service_name

    @property
    def pay_date(self):
       return self.__pay_date

    @pay_date.setter
    def pay_date(self, pay_date):
       self.__pay_date = pay_date

    @property
    def pay_type(self):
       return self.__pay_type

    @pay_type.setter
    def pay_type(self, pay_type):
       self.__pay_type = pay_type

    @property
    def hairdresser(self):
       return self.__hairdresser

    @hairdresser.setter
    def hairdresser(self, hairdresser):
       self.__hairdresser = hairdresser