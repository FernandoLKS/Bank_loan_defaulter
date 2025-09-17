from pydantic import BaseModel

class ClientData(BaseModel):
    Age: int
    Income: int
    Family: int
    CCAvg: float
    Mortgage: int
    Education: int
    SecuritiesAccount: int
    CDAccount: int
    Online: int
    CreditCard: int