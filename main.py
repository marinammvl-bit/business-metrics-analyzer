import pandas as pd


def calculate_profitability(revenue: float, cost: float) -> float:
    """Возвращает рентабельность в процентах."""
    if revenue == 0:
        return 0.0
    return (revenue - cost) / revenue * 100


def main():
    data = {
        "Месяц": ["Январь", "Февраль", "Март"],
        "Выручка": [120000, 150000, 135000],
    }
    df = pd.DataFrame(data)
    print(df)
    print("Средняя выручка:", df["Выручка"].mean())

    # Расчёт KPI: рентабельность
    revenue = 135000.0
    cost = 90000.0
    profitability = calculate_profitability(revenue, cost)
    print(f"Рентабельность: {profitability:.2f}%")


if __name__ == "__main__":
    main()