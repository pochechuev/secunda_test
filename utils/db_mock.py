organizations = [
    {
        "name": "ООО 'Рога и Копыта'",
        "phones": ["55-55-55", "88005553535"],
        "address": 1,
    },
    {
        "name": "Магазин",
        "phones": ["625-500"],
        "address": 2,
    },
    {
        "name": "Ферма",
        "phones": ["89002001111"],
        "address": 3,
    },
    {
        "name": "Автосервис",
        "phones": ["+7 123 123 3211", "12-32-11"],
        "address": 1,
    },
]

buildings = [
    {
        "address": "г. Москва, ул. Ленина 1",
        "point_x": 55.7558,
        "point_y": 37.6173,
    },
    {
        "address": "г. Москва, ул. Карла Маркса 1",
        "point_x": 55.6515,
        "point_y": 37.5954,
    },
    {
        "address": "г. Санкт-Петербург, пр-кт. Пионерский 1",
        "point_x": 59.9343,
        "point_y": 30.3351,
    },
]

activity_types = [
    {
      "activity_type": "Еда",
    },
    {
      "activity_type": "Мясная продукция",
      "parent_id": 1,
    },
    {
      "activity_type": "Молочная продукция",
      "parent_id": 1,
    },
    {
      "activity_type": "Автомобили",
    },
    {
      "activity_type": "Грузовые",
      "parent_id": 4,
    },
    {
      "activity_type": "Легковые",
      "parent_id": 4,
    },
    {
      "activity_type": "Запчасти",
      "parent_id": 6,
    },
    {
      "activity_type": "Аксессуары",
      "parent_id": 6,
    },
]

organizations_activity_types = [
    {
        "organization_id": 1,
        "activity_type_id": 1
    },
    {
        "organization_id": 1,
        "activity_type_id": 4
    },
    {
        "organization_id": 2,
        "activity_type_id": 1
    },
    {
        "organization_id": 3,
        "activity_type_id": 2
    },
    {
        "organization_id": 3,
        "activity_type_id": 3
    },
    {
        "organization_id": 4,
        "activity_type_id": 5
    },
    {
        "organization_id": 4,
        "activity_type_id": 6
    },
    {
        "organization_id": 4,
        "activity_type_id": 7
    },
    {
        "organization_id": 4,
        "activity_type_id": 8
    },
]
