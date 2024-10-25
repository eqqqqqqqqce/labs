salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

required_capital = 0
current_spend = spend

for month in range(months):
    if salary < current_spend:
        required_capital += (current_spend - salary)
    current_spend *= (1 + increase)

min_capital = round(required_capital)

print("Подушка безопасности, чтобы протянуть 10 месяцев без долгов:", min_capital)
