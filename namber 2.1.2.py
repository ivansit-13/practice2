def combination_sum(candidates, target):
    def backindex(index, combination, target):
        if target == 0:#если tagret == 0, это означает что мы уже нашли нужную нам камбинацию
            result.append(combination) #и мы её добавляем в массив результат
            return

        for i in range(index, len(candidates)):
            # Пропускаем дубликаты
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            # Вызываем backtrack для поиска следующего элемента
            backindex(i + 1, combination + [candidates[i]], target - candidates[i])

    candidates.sort()  # Сортируем массив для удобства
    result = [] # это наш массив который будет хранить другие массивы
    backindex(0, [], target) #тут мы всё очищаем для повторного использования
    return result


candidates = [2, 5, 2, 1, 2]
target = 5
print(combination_sum(candidates, target))
