class LinearSearch:
    @staticmethod
    def search(data, attribute, query, starts_with=False):
        normalized_query = query.lower() if isinstance(query, str) else query
        if starts_with:
            return [item for item in data if str(getattr(item, attribute)).lower().startswith(normalized_query)]
        else:
            return [item for item in data if normalized_query in str(getattr(item, attribute)).lower()]
