import joblib
import pandas as pd
from schemas.client import ClientData

model_path = "\Projects\Codes\Bank_Loan_Defaulter\Model\model.pkl"

model = joblib.load(model_path)

def predict_client(data: ClientData, threshold: float) -> bool:
   
    X = pd.DataFrame([{
        "Age": data.Age,
        "Income": data.Income,
        "Family": data.Family,
        "CCAvg": data.CCAvg,
        "Education": data.Education,
        "Mortgage": data.Mortgage,
        "Securities Account": data.SecuritiesAccount,
        "CD Account": data.CDAccount,
        "Online": data.Online,
        "CreditCard": data.CreditCard
    }])

    proba = model.predict_proba(X)[0,1]    
    return proba >= threshold
  
