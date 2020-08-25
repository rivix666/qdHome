"""TODO"""


class HomeData:
    def __init__(self):
        self.__title = "Uninitialized"
        self.__price = -1.0
        self.__rooms = -1
        self.__area = -1.0
        self.__m_price = -1
        self.__district = ""
        self.__desc_url = ""

    def __str__(self):
        """ For Debug Purposes """
        return (f"Name:        {self.__title}\n" 
                f"Price:       {self.__price} zl\n"
                f"Rooms:       {self.__rooms}\n"
                f"Area:        {self.__area} m2\n"
                f"Price per m: {self.__m_price} zl/m2\n"
                f"District:    {self.__district}\n"
                f"Url:         {self.__desc_url}\n"
                f"-----------------------------")

    # If something goes wrong we can always use RegExp # [0-9]+
    @classmethod
    def find_int_in_str(cls, value):
        """ Finds integer in string """

        tmp = value.strip()
        numbers = [s for s in tmp.split() if s.isdigit()]
        num_str = "".join(numbers)
        return int(num_str) if num_str else -1

    # If something goes wrong we can always use RegExp # [0-9]+(\,[0-9][0-9]?)?
    @classmethod
    def find_float_in_str(cls, value):
        """ Finds float in string """
        tmp = value.strip().replace(",", ".")
        # TODO This wont work in special cases, but on otodom it will be enough
        numbers = [s for s in tmp.split() if s.isdigit() or "." in s]
        num_str = "".join(numbers)
        return float(num_str) if num_str else -1.0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Wrong value type")
        self.__title = value.strip()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if isinstance(value, str):
            self.__price = self.find_float_in_str(value)
        elif isinstance(value, float):
            self.__price = value
        else:
            raise ValueError("Wrong value type")

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, value):
        if isinstance(value, str):
            self.__rooms = self.find_int_in_str(value)
        elif isinstance(value, int):
            self.__rooms = value
        else:
            raise ValueError("Wrong value type")

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        if isinstance(value, str):
            self.__area = self.find_float_in_str(value)
        elif isinstance(value, float):
            self.__area = value
        else:
            raise ValueError("Wrong value type")

    @property
    def m_price(self):
        return self.__m_price

    @m_price.setter
    def m_price(self, value):
        if isinstance(value, str):
            self.__m_price = self.find_int_in_str(value)
        elif isinstance(value, int):
            self.__m_price = value
        else:
            raise ValueError("Wrong value type")

    @property
    def district(self):
        return self.__district.strip()

    @district.setter
    def district(self, value):
        if not isinstance(value, str):
            raise ValueError("Wrong value type")
        self.__district = value.strip()

    @property
    def desc_url(self):
        return self.__desc_url

    @desc_url.setter
    def desc_url(self, value):
        if not isinstance(value, str):
            raise ValueError("Wrong value type")
        self.__desc_url = value.strip()
