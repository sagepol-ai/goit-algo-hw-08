import heapq

def min_cost_to_connect_cables(cables):
    """
    Знаходить мінімальні витрати на об'єднання мережевих кабелів.
    cables -- список довжин кабелів
    """
    # Створюємо копію, щоб не змінювати оригінальний список
    heap = list(cables)
    
    # Перетворюємо список у купу (min-heap)
    heapq.heapify(heap)
    
    total_cost = 0
    
    # Поки в купі залишилося більше одного елемента
    while len(heap) > 1:
        # 1. Витягуємо два найменші елементи
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        
        # 2. Об'єднуємо їх
        current_cost = min1 + min2
        
        # 3. Додаємо вартість до загальних витрат
        total_cost += current_cost
        
        print(f"Об'єднуємо кабелі довжиною {min1} та {min2}. Витрати: {current_cost}. Загальні витрати: {total_cost}")
        
        # 4. Повертаємо новий об'єднаний кабель у купу
        heapq.heappush(heap, current_cost)
        
    return total_cost

if __name__ == "__main__":
    # Тестові набори даних (списки довжин кабелів)
    test_cases = [
        [4, 3, 2, 6],
        [1, 2, 3, 4, 5],
        [5, 1, 2, 10, 4, 1, 3, 13],
    ]
    
    for cables in test_cases:
        cost = min_cost_to_connect_cables(cables)
        print(f"Кабелі: {cables} -> Мінімальні витрати: {cost}")