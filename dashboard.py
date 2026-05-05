import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données brutes pour affichage dans le dashboard
df = pd.read_csv("data/churn.csv")

# Calcul du taux de churn global sur l'ensemble de la base
churn_rate = (df["Churn"] == "Yes").mean()

st.title("Dashboard Churn - Telco")

# Affichage des trois KPIs principaux en colonnes côte à côte
col1, col2, col3 = st.columns(3)
col1.metric("Churn rate global", f"{churn_rate:.2%}")
col2.metric("Clients total", len(df))
col3.metric("Clients à risque", int(len(df) * churn_rate))

st.divider()

# Graphique : taux de churn moyen par type de contrat
# Permet d'identifier quel segment est le plus à risque
st.subheader("Churn par type de contrat")
churn_by_contract = df.groupby("Contract")["Churn"].apply(lambda x: (x == "Yes").mean())
st.bar_chart(churn_by_contract)

st.divider()

# Affichage du profil moyen d'un client qui churne
st.subheader("Profil des clients à risque")
at_risk = df[df["Churn"] == "Yes"][["tenure", "MonthlyCharges", "Contract", "InternetService"]]
st.write(f"Tenure moyen : {at_risk['tenure'].mean():.0f} mois")
st.write(f"Charge mensuelle moyenne : {at_risk['MonthlyCharges'].mean():.2f} €")

# Graphique de dispersion : MonthlyCharges vs Tenure coloré par statut de churn
# Les points rouges (churners) se concentrent en haut à gauche :
# clients récents avec des charges élevées
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

# Recommandations métier affichées directement dans le dashboard
st.subheader("Recommandations")
st.write("- Cibler les clients en contrat mensuel avec moins de 12 mois d'ancienneté")
st.write("- Proposer une remise pour passer en contrat annuel")
st.write("- Priorité aux clients avec MonthlyCharges > 65€")