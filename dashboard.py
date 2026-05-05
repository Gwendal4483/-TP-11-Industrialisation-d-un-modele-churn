import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données brutes pour affichage dans le dashboard
df = pd.read_csv("data/churn.csv")

# Calcul du taux de churn global sur l'ensemble de la base
churn_rate = (df["Churn"] == "Yes").mean()

st.title("Dashboard Churn - Telco")

st.markdown("""
Vous êtes directeur marketing chez Telco. Chaque mois, des clients résilient leur contrat sans que vous puissiez anticiper ces départs.
Ce dashboard vous permet d'identifier les profils à risque dans votre base clients, de comprendre pourquoi ils partent,
et de cibler vos actions de rétention là où elles auront le plus d'impact.
""")

# Affichage des trois KPIs principaux en colonnes côte à côte
col1, col2, col3 = st.columns(3)
col1.metric("Churn rate global", f"{churn_rate:.2%}")
col2.metric("Clients total", len(df))
col3.metric("Clients à risque", int(len(df) * churn_rate))

st.divider()

# Aperçu des données brutes
st.subheader("Aperçu des données")
st.dataframe(df.head(10))
st.write(f"Dimensions du dataset : {df.shape[0]} lignes x {df.shape[1]} colonnes")

st.divider()

# Graphique : taux de churn moyen par type de contrat
# Permet d'identifier quel segment est le plus à risque
st.subheader("Churn par type de contrat")
churn_by_contract = df.groupby("Contract")["Churn"].apply(lambda x: (x == "Yes").mean())
st.bar_chart(churn_by_contract)

st.divider()

st.subheader("Comparaison des profils clients")


# Affichage du profil moyen d'un client qui churne
st.subheader("Profil des clients à risque")
at_risk = df[df["Churn"] == "Yes"][["tenure", "MonthlyCharges", "Contract", "InternetService"]]
st.write(f"Tenure moyen : {at_risk['tenure'].mean():.0f} mois")
st.write(f"Charge mensuelle moyenne : {at_risk['MonthlyCharges'].mean():.2f} €")

#affichage du profil moyen d'un client qui ne churne pas
st.subheader("Profil des clients stables")
stable = df[df["Churn"] == "No"][["tenure", "MonthlyCharges", "Contract", "InternetService"]]
st.write(f"Tenure moyen : {stable['tenure'].mean():.0f} mois")
st.write(f"Charge mensuelle moyenne : {stable['MonthlyCharges'].mean():.2f} €")


st.subheader("Visualisation des profils clients")

# Graphique de dispersion : MonthlyCharges vs Tenure coloré par statut de churn
# Les points rouges (churners) se concentrent en haut à gauche :
# clients récents avec des charges élevées
fig, ax = plt.subplots()
colors = df["Churn"].map({"Yes": "red", "No": "blue"})
ax.scatter(df["tenure"], df["MonthlyCharges"], c=colors, alpha=0.3, s=10)
ax.set_xlabel("Ancienneté (mois)")
ax.set_ylabel("Montant Mensuel (€)")
ax.legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', label='Churn'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', label='No Churn')
])
st.pyplot(fig)

st.divider()

# Graphique : taux de churn selon l'utilisation du support technique
# Permet de voir si les clients qui contactent le support sont plus à risque
st.subheader("Churn selon le support technique")
churn_by_support = df.groupby("TechSupport")["Churn"].apply(lambda x: (x == "Yes").mean())
st.bar_chart(churn_by_support)


# Recommandations métier affichées directement dans le dashboard
st.subheader("Analyse et conseils")
st.write("**Quels clients churne le plus ?**")
st.write("Les clients en contrat mensuel, avec moins de 12 mois d'ancienneté, des charges supérieures à la moyenne et sans support technique.")

st.write("**Pourquoi ?**")
st.write("Un contrat mensuel n'engage pas le client sur la durée. Combiné à une facture élevée et à un manque d'accompagnement technique, le client ne perçoit pas suffisamment la valeur du service pour rester.")

st.write("**Quelles actions business mettre en place ?**")
st.write("Contacter ces clients dans les 3 premiers mois avec une offre de passage en contrat annuel incluant le support technique. C'est la période où le risque est le plus élevé et où une action commerciale a le plus d'impact.")