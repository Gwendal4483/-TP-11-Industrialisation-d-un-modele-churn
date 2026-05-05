import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/churn.csv")

churn_rate = (df["Churn"] == "Yes").mean()

st.title("Dashboard Churn - Telco")

# KPIs en colonnes
col1, col2, col3 = st.columns(3)
col1.metric("Churn rate global", f"{churn_rate:.2%}")
col2.metric("Clients total", len(df))
col3.metric("Clients à risque", int(len(df) * churn_rate))

st.divider()

# Churn par type de contrat
st.subheader("Churn par type de contrat")
churn_by_contract = df.groupby("Contract")["Churn"].apply(lambda x: (x == "Yes").mean())
st.bar_chart(churn_by_contract)

st.divider()

st.subheader("MonthlyCharges vs Tenure selon le churn")

fig, ax = plt.subplots()
colors = df["Churn"].map({"Yes": "red", "No": "blue"})
ax.scatter(df["tenure"], df["MonthlyCharges"], c=colors, alpha=0.3, s=10)
ax.set_xlabel("Tenure (mois)")
ax.set_ylabel("Monthly Charges (€)")
ax.legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', label='Churn'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', label='No Churn')
])
st.pyplot(fig)

st.divider()

# Recommandations
st.subheader("Recommandations")
st.write("- Cibler les clients en contrat mensuel avec moins de 12 mois d'ancienneté")
st.write("- Proposer une remise pour passer en contrat annuel")
st.write("- Priorité aux clients avec MonthlyCharges > 65€")