class BinarySearch:
    @staticmethod
    def search(data, attribute, query, starts_with=False):
        sorted_data = sorted(data, key=lambda x: getattr(x, attribute))
        left, right = 0, len(sorted_data) - 1
        results = []

        normalized_query = query.lower() if isinstance(query, str) else query

        while left <= right:
            mid = (left + right) // 2
            mid_value = str(getattr(sorted_data[mid], attribute)).lower()

            if starts_with:
                if mid_value.startswith(normalized_query):
                    # Agregar todos los elementos iguales hacia la izquierda
                    i = mid
                    while i >= 0 and str(getattr(sorted_data[i], attribute)).lower().startswith(normalized_query):
                        results.append(sorted_data[i])
                        i -= 1
                    # Agregar todos los elementos iguales hacia la derecha
                    i = mid + 1
                    while i < len(sorted_data) and str(getattr(sorted_data[i], attribute)).lower().startswith(normalized_query):
                        results.append(sorted_data[i])
                        i += 1
                    return results
                elif mid_value < normalized_query:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if normalized_query in mid_value:
                    # Agregar todos los elementos iguales hacia la izquierda
                    i = mid
                    while i >= 0 and normalized_query in str(getattr(sorted_data[i], attribute)).lower():
                        results.append(sorted_data[i])
                        i -= 1
                    # Agregar todos los elementos iguales hacia la derecha
                    i = mid + 1
                    while i < len(sorted_data) and normalized_query in str(getattr(sorted_data[i], attribute)).lower():
                        results.append(sorted_data[i])
                        i += 1
                    return results
                elif mid_value < normalized_query:
                    left = mid + 1
                else:
                    right = mid - 1

        return results
