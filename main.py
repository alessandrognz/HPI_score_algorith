from fc import theory_score, fundamentos_de_computadores
from algebra import algebra_final_score


def main():
    print("\033[38;2;0;102;166m" + r"""
   ██ ███    ███████ ██ ██          █████  ██     ██ ███████ ██████   █████   ██████  ███████
  ███ █ █    ██      ██ ██         ██   ██ ██     ██ ██      ██   ██ ██   ██ ██       ██
   ██ ███    █████   ██ ██  ████   ███████  ██   ██  █████   ██████  ███████ ██   ███ █████
   ██        ██      ██ ██         ██   ██   ██ ██   ██      ██   ██ ██   ██ ██    ██ ██
   ██        ███████ ██ ██         ██   ██    ███    ███████ ██   ██ ██   ██  ██████  ███████

 ██████  █████  ██      ██ ███████ ██  ██████  █████  ████████ ██  ██████  ███    ██ ███████
██      ██   ██ ██      ██ ██      ██ ██      ██   ██    ██    ██ ██    ██ ████   ██ ██
██      ███████ ██      ██ █████   ██ ██      ███████    ██    ██ ██    ██ ██ ██  ██ ███████
██      ██   ██ ██      ██ ██      ██ ██      ██   ██    ██    ██ ██    ██ ██  ██ ██      ██
 ██████ ██   ██ ███████ ██ ██      ██  ██████ ██   ██    ██    ██  ██████  ██   ████ ███████
"""
+ "\033[0m")
    subject = input("Select a subject to calculate your grade\n" \
    "[1] - Habilidades Profesionales para Ingenieros\n" \
    "[2] - Fundamentos de Programación 1\n" \
    "[3] - Fundamentos de Computadores\n" \
    "[4] - Álgebra y Geometría\n" \
    "[5] - Matemática Discreta\n" \
    "Option: ").strip()

    match subject:
        case "1":
            pass
        case "2":
            pass
        case "3":
            # 1) Ask for the theory grades
            partial1 = float(input("Enter your score in first partial exam: "))
            partial2 = float(input("Enter your score in second partial exam: "))
            partial3 = float(input("Enter your score in third partial exam: "))
            ordinary_score = float(input("Enter your score in ordinary exam (theory): "))

            # 2) Find the theory grade (function from fc.py)
            theory = theory_score(partial1, partial2, partial3, ordinary_score)

            # 3) Ask for the other grades: lab exam and quizzes
            practical_exam = float(input("Enter your score in practical exam: "))
            ae_score = float(input("Enter your average score in exercise quizzes (AE): "))
            ap_score = float(input("Enter your average score in lab quizzes (AP): "))

            # 4) Find and show the final grade
            fundamentos_de_computadores(theory, practical_exam, ae_score, ap_score)
        case "4":
            pass
        case "5":
            pass

if __name__ == "__main__":
    main()