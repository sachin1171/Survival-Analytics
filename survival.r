###################### problem 1 #########################
install.packages('survminer')
install.packages("survival")

library(survminer)
library(survival)
## Importing the data
library(readr)
Patient <- read.csv(file.choose())
View(Patient)
attach(Patient)
str(Patient)
## Removing the ID column
Patient <- Patient[2:4]
colnames(Patient)
# Define variables 
time <- Followup
event <- Eventtype
group <- Scenario 
# Descriptive statistics
summary(time)
table(event)
table(group)  ## The group coulumn having the only one category.
# Kaplan-Meier non-parametric analysis
## Hear the group has only one category so, we build the through the 1 or group
kmsurvival <- survfit(Surv(time, event) ~ 1)
summary(kmsurvival)
## plot
plot(kmsurvival, xlab="Time", ylab="Survival Probability")
## Advanced plot
ggsurvplot(kmsurvival, data=Patient, risk.table = TRUE)
# Kaplan-Meier non-parametric analysis by group
kmsurvival1 <- survfit(Surv(time, event) ~ group)
summary(kmsurvival1)
plot(kmsurvival1, xlab="Time", ylab="Survival Probability")
ggsurvplot(kmsurvival1, data=Patient, risk.table = TRUE)
###################### problem 2 ######################
library(survminer)
library(survival)
library(readxl)

ecg <- read_excel(file.choose())

attach(ecg)
str(ecg)

# Define variables 
time <- survival_time_hr
alive <- alive
group <- group  

# Descriptive statistics
summary(time)
table(alive)
table(group)

# Kaplan-Meier non-parametric analysis
kmsurvival <- survfit(Surv(time, alive) ~ 1)
summary(kmsurvival)
plot(kmsurvival, xlab="Time", ylab="Survival Probability")

ggsurvplot(kmsurvival, data=ecg, risk.table = TRUE)

# Kaplan-Meier non-parametric analysis by group
kmsurvival1 <- survfit(Surv(time, alive) ~ group)
summary(kmsurvival1)

plot(kmsurvival1, xlab="Time", ylab="Survival Probability")
ggsurvplot(kmsurvival1, data=ecg, risk.table = TRUE)
