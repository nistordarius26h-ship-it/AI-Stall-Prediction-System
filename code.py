import math 

def stall_margin(aoa_deg, gust_deg, critical_aoa_deg=16.0): 
    effective_aoa = aoa_deg + gust_deg 
    margin = critical_aoa_deg - effective_aoa 
    if margin <= 0: 
        status = "STALL WARNING" 
    elif margin < 2: 
        status = "HIGH RISK" 
    elif margin < 4: 
        status = "CAUTION" 
    else: 
        status = "SAFE" 
    return effective_aoa, margin, status 

eff, margin, status = stall_margin(aoa_deg=13, gust_deg=2.5) 
print(f"{status}: effective AoA={eff:.1f} deg, margin={margin:.1f} deg") 




from sklearn.ensemble import RandomForestClassifier 
import numpy as np 

# Columns: [angle_of_attack_deg, gust_deg, airspeed_ms] 

X_train = np.array([ 
    [12, 1.2, 78], 
    [14, 2.0, 72], 
    [15, 3.0, 69], 
    [10, 0.5, 90], 
]) 

y_train = np.array([0, 1, 1, 0])  # 0 = Safe, 1 = Stall risk 
model = RandomForestClassifier(n_estimators=200, random_state=42) 
model.fit(X_train, y_train) 
sample = np.array([[13, 2.5, 74]]) 

print(model.predict(sample), model.predict_proba(sample)) 
