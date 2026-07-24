HEADER = {
    "first_name": "Albert",
    "first_name__ru": "Альберт",
    "last_name": "Zuev",
    "last_name__ru": "Зуев",
    "title": "Albert Zuev | CV",
    "title__ru": "Альберт Зуев | CV",
    "contacts": {
        "github": "iamnalinor",
        "telegram": "nalinor",
        "email": "i@nlnr.ru",
    },
}

EDUCATION = [
    {
        "name": "HSE University",
        "name__ru": "НИУ ВШЭ",
        "degree": "Bachelor in Computer Science",
        "degree__ru": "Бакалавриат, Факультет компьютерных наук",
        "period": "Sep. 2026 -- est. June 2030",
        "period__ru": "Сентябрь 2026 -- Июнь 2030",
        "location": "Moscow, Russia",
        "location__ru": "Москва, Россия",
    },
]

EXPERIENCE = [
    {
        "name": "Python Developer Intern",
        "name__ru": "Стажер Python-разработчик",
        "stack": "Python, Airflow, Selenium",
        "period": "January 2026 -- July 2026",
        "period__ru": "Январь 2026 -- Июль 2026",
        "company": "T-Bank, T-City, ML in Shopping Search",
        "company__ru": "Т-Банк, Т-Город, ML в Поиске Шопинга",
        "location": "Remote",
        "location__ru": "Удалённо",
        "points": [
            "Implemented a parser for 5 competitor services (Ozon, Wildberries, others) using Selenium with anti-bot bypass and automated it via Airflow, enabling multiple ML teams to compare search quality with competitors and identify enhancement opportunities",
            "Integrated Airflow search quality pipeline into «Metrics» (service to collect SERPs from Shopping search), reducing human work time to run A/B test from several hours to 2-3 minutes (used in 30+ A/B tests)",
            "Shipped 15+ features (including UX enhancements) to «Metrics» driven by user feedback, increasing user count to 10 employees across 3 teams",
        ],
        "points__ru": [
            "Реализовал парсер 5 сервисов-конкурентов (Ozon, Wildberries, др.) через Selenium с обходом антибота и автоматизировал его через Airflow, что позволило нескольким ML-командам сравнивать качество поиска с конкурентами и находить точки роста",
            "Интегрировал Airflow-пайплайн оценки качества поиска в «Metrics» (внутренний сервис для парсинга поисковой выдачи Шопинга), ускорив время ручной работы на запуск A/B-теста с нескольких часов до 2–3 минут (применяли в 30+ A/B-тестах)",
            "Выкатил 15+ фич (включая улучшения UX) в «Metrics» на основе фидбэка пользователей, нарастив аудиторию до 10 человек в 3 командах",
        ],
    },
]

PROJECTS = [
    {
        "name": "<a href='https://dano.hse.ru/mirror/pubs/share/1123688294'>Impact of Real Estate Developer Reputation on Property Prices</a>",
        "name__ru": "<a href='https://dano.hse.ru/mirror/pubs/share/1123688294'>Влияние репутации застройщика на цену недвижимости</a>",
        "stack": "Research",
        "stack__ru": "Исследование",
        "period": "2025",
        "points": [
            "Analyzed a dataset of 50K new-build property transactions in New Moscow covering 23 developers and 45 residential complexes",
            "Enriched the dataset by scraping transport accessibility and infrastructure data from 2GIS",
            "Quantified the developer reputation effect (~5% average price premium) using hedonic regression with fixed effects",
            "Verified robustness via permutation tests",
            "Scored 100/100 in the DANO'25 olympiad finals, <b>#1</b> out of 65 teams",
        ],
        "points__ru": [
            "Исследовали датасет сделок по новостройкам Новой Москвы: 50К покупок, 23 застройщика, 45 ЖК",
            "Обогатили датасет парсингом данных о транспортной доступности и инфраструктуре ЖК с 2GIS",
            "Численно оценили эффект репутации застройщика (в среднем ~5%) с помощью гедонической регрессии с фиксированными эффектами",
            "Проверили модель на устойчивость пермутационными тестами",
            "100/100 баллов на финале олимпиады DANO'25, <b>1</b> место среди 65 команд",
        ],
    },
    {
        "name": "<a href='https://github.com/iamnalinor/prod26-onetwo'>OneTwo</a>",
        "stack": "Python, Litestar, Postgres, ClickHouse, Redis, Prometheus, Docker",
        "period": "2026",
        "points": [
            "A/B testing platform with deterministic flag assignment, metrics DSL compiled to ClickHouse SQL, role model, autopilot, guardrails, and notifications",
            "Scored 93/100 in the PROD'26 Olympiad finals, <b>#2</b> out of 200+ participants",
        ],
        "points__ru": [
            "Платформа A/B-тестов с детерминированной выдачей флагов, DSL метрик с компиляцией в ClickHouse SQL, ролевой моделью, автопилотом, guardrail-правилами и уведомлениями",
            "93/100 баллов на финале олимпиады PROD'26, <b>2</b> место среди 200+ участников",
        ],
    },
]

EXTRACURRICULAR_ACTIVITIES = [
    "<b>Big Data</b>, Yandex Lyceum, Autumn 2024",
    "<b>Data Analytics</b>, Yandex Lyceum, Spring 2024",
    "<b>Algorithms & Data Structures</b>, T-Bank Generation, 2023--2024",
]

EXTRACURRICULAR_ACTIVITIES_RU = [
    "<b>Большие данные</b>, Яндекс.Лицей, осень 2024",
    "<b>Анализ данных</b>, Яндекс.Лицей, весна 2024",
    "<b>Алгоритмы и структуры данных</b>, Т-Поколение, 2023--2024",
]

HONORS_AND_AWARDS = [
    '<b>Winner</b> of <a href="https://cu.ru/events/bachelor-casecontest">DEADLINE case competition</a>, 2026',
    '<b>Winner</b> (2026) and <b>double prize winner</b> (2024, 2025) of <a href="https://prodcontest.ru">PROD Olympiad</a>',
    '<b>Winner</b> (2025) and <b>prize winner</b> (2024) of <a href="https://dano.hse.ru">DANO Olympiad</a>',
    '<b>3-time winner</b> of <a href="https://dano.hse.ru/hackathon/">DANO Hackathon</a> (Saint Petersburg, Yekaterinburg, Perm), 2025',
]

HONORS_AND_AWARDS_RU = [
    '<b>Победитель</b> <a href="https://cu.ru/events/bachelor-casecontest">кейс-чемпионата DEADLINE</a>, 2026',
    '<b>Победитель</b> (2026) и <b>дважды призёр</b> (2024, 2025) <a href="https://prodcontest.ru">олимпиады PROD</a>',
    '<b>Победитель</b> (2025) и <b>призёр</b> (2024) <a href="https://dano.hse.ru">олимпиады DANO</a>',
    '<b>3-кратный победитель</b> <a href="https://dano.hse.ru/hackathon/">хакатонов DANO</a> (Санкт-Петербург, Екатеринбург, Пермь), 2025',
]

TECHNICAL_SKILLS = [
    {
        "name": "Languages",
        "name__ru": "Языки",
        "value": "Python, Go, TypeScript",
    },
    {
        "name": "Frameworks",
        "name__ru": "Фреймворки",
        "value": "Django/DRF, Elysia, FastAPI, Gin, Litestar",
    },
    {
        "name": "Libraries",
        "name__ru": "Библиотеки",
        "value": "Aiogram, Aiogram-dialog, Beanie, Pandas, Pydantic, Pyrogram, Selenium, SQLAlchemy, Tavern, Telethon",
    },
    {
        "name": "Other",
        "name__ru": "Прочее",
        "value": "Airflow, CI/CD, Docker, Git, Linux, MongoDB, RabbitMQ, SQL (SQLite, MySQL, Postgres, YDB)",
    },
]

BLOCKS = [
    {
        "name": "Education",
        "name__ru": "Образование",
        "type": "education",
        "content": EDUCATION,
    },
    {
        "name": "Projects",
        "name__ru": "Проекты",
        "type": "experience",
        "content": PROJECTS,
    },
    {
        "name": "Experience",
        "name__ru": "Опыт работы",
        "type": "experience",
        "content": EXPERIENCE,
    },
    {
        "name": 'Honors & Awards <a href="https://drive.google.com/drive/folders/1Np04Rl0Beq4wwxtVPJNrBD4GxaCjUWOB">[proofs]</a>',
        "name__ru": 'Достижения <a href="https://drive.google.com/drive/folders/1Np04Rl0Beq4wwxtVPJNrBD4GxaCjUWOB">[дипломы]</a>',
        "type": "list",
        "content": HONORS_AND_AWARDS,
        "content__ru": HONORS_AND_AWARDS_RU,
    },
    {
        "name": 'Extracurricular Activities <a href="https://drive.google.com/drive/folders/1Ivp8OiUzbrBaKCdHkbWCYje76-zrDKEE">[proofs]</a>',
        "name__ru": 'Пройденные курсы <a href="https://drive.google.com/drive/folders/1Ivp8OiUzbrBaKCdHkbWCYje76-zrDKEE">[сертификаты]</a>',
        "type": "list",
        "content": EXTRACURRICULAR_ACTIVITIES,
        "content__ru": EXTRACURRICULAR_ACTIVITIES_RU,
        "proof_url": "https://drive.google.com/drive/folders/1Ivp8OiUzbrBaKCdHkbWCYje76-zrDKEE",
    },
    {
        "name": "Technical Skills",
        "name__ru": "Технические навыки",
        "type": "mapping",
        "content": TECHNICAL_SKILLS,
    },
]
