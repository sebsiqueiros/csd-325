def city_country(city, country, population=None, language=None):
    result = f"{city}, {country}"

    if population:
        result += f" - population {population}"
    if language:
        result += f", {language}"

    return result


# Final calls
print(city_country("Santiago", "Chile"))
print(city_country("Paris", "France", 2148000))
print(city_country("Tokyo", "Japan", 13960000, "Japanese"))
