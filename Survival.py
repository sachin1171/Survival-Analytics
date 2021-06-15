############################## problem 1 ########################
import pandas as pd
# Loading the the survival data
patient = pd.read_csv("C:/Users/usach/Desktop/Survival Analytics/Patient.csv")
patient.head()
patient.describe()

patient = patient.drop(["PatientID"], axis = 1)

patient["Followup"].describe()

# Spell is referring to time 
Time = patient.Followup

# Importing the KaplanMeierFitter model to fit the survival analysis

from lifelines import KaplanMeierFitter

# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitter model on Time and Events for death 
kmf.fit(Time, patient.Eventtype)

# Time-line estimations plot 
kmf.plot()
################################# problem 2 ######################
import pandas as pd
#loading the ecgset
ecg = pd.read_excel("C:/Users/usach/Desktop/Survival Analytics/ECG_Surv.xlsx")
ecg_details =pd.DataFrame({"column name":ecg.columns,
                            "ecg type(in Python)": ecg.dtypes})

ecg.info()
ecg.describe()   
ecg.drop(columns=["name"],inplace = True) # dropind row num 1
S=ecg.survival_time_hr
# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter
# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()
# Fitting KaplanMeierFitter model on Time and groups for death 
kmf.fit(S, ecg.alive)
# Time-line estimations plot 
kmf.plot()




# Over Multiple groups 
# For each group, here group is group
ecg.group.value_counts()

# Applying KaplanMeierFitter model on Time and groups for the group "1"
kmf.fit(S[ecg.group==1], ecg.group[ecg.group==1], label='group-1')
ax = kmf.plot()

# Applying KaplanMeierFitter model on Time and groups for the group "2"
kmf.fit(S[ecg.group==2], ecg.group[ecg.group==2], label='group-2')
ay=kmf.plot()

# Applying KaplanMeierFitter model on Time and groups for the group "3"
kmf.fit(S[ecg.group==3], ecg.group[ecg.group==3], label='group-3')
kmf.plot()
