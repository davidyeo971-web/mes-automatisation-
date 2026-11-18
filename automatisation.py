taches = [
    "Organiser mes fichiers",
    "Préparer mon rapport",
    "Vérifier mes messages"
]

print("=== MON ASSISTANT AUTOMATIQUE ===")

for numero, tache in enumerate(taches, start=1):
    print(f"{numero}. {tache}")

print("Toutes les tâches ont été affichées !")