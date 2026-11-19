#This function is meant to stablish the average from all the notes the user writes down.
def average(scores: list[float]) -> float:
    if not scores:
        raise ValueError("You need to write down at least one score")

    return sum(scores) / len(scores)
#This function calculates the final score from FP1 subject.
def FP1_final_score(questionaries: list[float], activities: list[float], practice_work: list[float]) -> float:
    questionaries_score = average(questionaries)
    activities_score = average(activities)
    practice_work_score = average(practice_work)

    final_score = (
        0.20 * questionaries_score
        + 0.55 * activities_score
        + 0.25 * practice_work_score
        )
    return final_score


def pedir_notas(apartado: str) -> list[float]:
    texto = input(
        f"Introduce las notas de {apartado}, separadas por comas: "
    )
    return [float(nota.strip()) for nota in texto.split(",")]


questionaries = pedir_notas("cuestionarios (FE01a)")
activities = pedir_notas("ejercicios (FE01b)")
practice_work = pedir_notas("trabajos prácticos (FE02)")

nota_final = FP1_final_score(questionaries, activities, practice_work)
print(f"La nota final de FP1 es: {nota_final:.2f}")
