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
    