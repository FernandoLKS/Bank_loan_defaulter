from pydantic import BaseModel

class ClientData(BaseModel):
    Age: int
    Income: float
    Family: int
    CCAvg: float
    Mortgage: float
    Education: int
    SecuritiesAccount: int
    CDAccount: int
    Online: int
    CreditCard: int