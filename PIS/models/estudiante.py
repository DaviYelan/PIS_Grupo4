import json
import os
import pandas as pd #type: ignore

DATA_FILE = "data/students.json"
class Estudiante:
    def __init__(self, nombre, apellido, matricula):
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.scores = {}


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def load_excel_data():
    data = {}
    for unit in range(1, 4):
        try:
            df = pd.read_excel(f"uploads/unit{unit}_data.xlsx")
            data[f"unit{unit}"] = df.to_dict("records")
        except FileNotFoundError:
            data[f"unit{unit}"] = []
    return data


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def calculate_averages(data):
    results = {}
    for student, info in data.items():
        all_scores = []
        for unit in ["unit1", "unit2", "unit3"]:
            if unit in info:
                scores = [
                    float(score)
                    for score in info[unit]
                    if isinstance(score, (int, float))
                ]
                all_scores.extend(scores)

        if all_scores:
            average_score = sum(all_scores) / len(all_scores)
            results[student] = {
                "average": average_score,
                "matricula": info["matricula"],
                "categoria": get_category(average_score),
                "unit_scores": {
                    unit: info.get(unit, []) for unit in ["unit1", "unit2", "unit3"]
                },
            }
    return results


def get_category(average):
    if 8.5 <= average <= 10:
        return "A"
    elif 7.5 <= average < 8.5:
        return "B"
    elif 5 <= average < 7.5:
        return "C"
    else:
        return "D"


def find_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
