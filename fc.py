# Fundamentos de Computadores (FC)
# This file finds the final grade for this subject.


def theory_score(partial1: float, partial2: float, partial3: float, exam_score: float) -> float:
    """Find the THEORY grade.

    Theory = 30% of the partial exams average + 70% of the ordinary exam.
    """
    # Take the average of the 3 partial exams
    average_controls = (partial1 + partial2 + partial3) / 3

    # The partials are 30% and the exam is 70%
    return 0.30 * average_controls + 0.70 * exam_score


def fundamentos_de_computadores(theory: float, practica_exam: float, ae_score: float, ap_score: float) -> float:
    """Find and return the FINAL grade.

    Theory 40%, lab exam 40%, AE 10%, AP 10%.
    """
    # Multiply each grade by its percent. The total is 100%.
    final = (
        0.40 * theory          # theory grade
        + 0.40 * practica_exam # lab exam grade
        + 0.10 * ae_score      # AE: exercise quizzes
        + 0.10 * ap_score      # AP: lab quizzes
    )

    # Show the result on the screen
    print(f"Theory: {theory:.2f}, Lab: {practica_exam:.2f}, Final: {final:.2f}")
    return final
