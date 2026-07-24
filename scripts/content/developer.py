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

SUMMARY = (
    "Backend developer specializing in Python and Go, with production experience at Yandex and T-Bank. "
    "Owned end-to-end feature delivery, from design to production rollout. Multiple-time winner of programming and data analysis competitions."
)

SUMMARY_RU = (
    "Бэкенд-разработчик на Python и Go с промышленным опытом в Яндексе и Т-Банке. "
    "Отвечал за полный цикл разработки фич, от проектирования до релиза. "
    "Многократный победитель олимпиад по разработке и анализу данных."
)

EDUCATION = [
    {
        "name": "HSE University",
        "name__ru": "НИУ ВШЭ",
        "degree": "Bachelor in Software Engineering",
        "degree__ru": "Бакалавриат, Программная инженерия",
        "period": "Sep. 2026 -- est. June 2030",
        "period__ru": "Сентябрь 2026 -- Июнь 2030",
        "location": "Moscow, Russia",
        "location__ru": "Москва, Россия",
    },
]

EXPERIENCE = [
    {
        "name": "Backend Developer Intern",
        "name__ru": "Стажер бэкенд-разработчик",
        "stack": "Python, FastAPI, Airflow, Selenium",
        "period": "January 2026 -- Current",
        "period__ru": "Январь 2026 -- текущее время",
        "company": "T-Bank, T-City Search",
        "company__ru": "Т-Банк, поиск Т-Города",
        "location": "Moscow",
        "location__ru": "Москва",
        "points": [
            "Implemented a parser for 5 competitor services (Ozon, Wildberries, others) using Selenium with anti-bot bypass and automated it via Airflow, enabling multiple ML teams to compare search quality with competitors and identify enhancement opportunities",
            "Integrated Airflow search quality pipeline into «Metrics» (service to collect SERPs from Shopping search), reducing human work time to run A/B test from several hours to 2-3 minutes (used in 30+ A/B tests)",
            "Shipped 15+ features (including UX enhancements) to «Metrics» driven by user feedback, increasing user count to 10 employees across 3 teams",
            "Developed end-to-end tests for «Metrics» using Tavern as framework and WireMock for mocking Airflow and Search API, increasing test coverage and catching bugs early",
        ],
        "points__ru": [
            "Реализовал парсер 5 сервисов-конкурентов (Ozon, Wildberries, др.) через Selenium с обходом антибота и автоматизировал его через Airflow, что позволило нескольким ML-командам сравнивать качество поиска с конкурентами и находить точки роста",
            "Интегрировал Airflow-пайплайн оценки качества поиска в «Metrics» (внутренний сервис для парсинга поисковой выдачи Шопинга), ускорив время ручной работы на запуск A/B-теста с нескольких часов до 2–3 минут (применяли в 30+ A/B-тестах)",
            "Выкатил 15+ фич (включая улучшения UX) в «Metrics» на основе фидбэка пользователей, нарастив аудиторию до 10 человек в 3 командах",
            "Разработал end-to-end тесты для «Metrics», используя Tavern и WireMock (мокал Airflow и API поиска), подняв тестовое покрытие и отлавливая ошибки до релиза",
        ],
    },
    {
        "name": "Backend Developer Intern",
        "name__ru": "Стажер бэкенд-разработчик",
        "stack": "Go, YDB",
        "period": "June 2025 -- October 2025",
        "period__ru": "Июнь 2025 -- Октябрь 2025",
        "company": "Yandex, Yandex Cloud, <a href='https://github.com/ydb-platform/nbs'>Network Block Store</a>",
        "company__ru": "Яндекс, Яндекс Облако, <a href='https://github.com/ydb-platform/nbs'>Сетевое блочное хранилище</a>",
        "location": "Moscow, Russia",
        "location__ru": "Москва, Россия",
        "points": [
            "Redesigned Disk Manager's task processor time estimation model for hanging task detection, which enhanced observability and SRE's diagnostic capabilities and eliminated false-positive alerts (<a href='https://github.com/ydb-platform/nbs/issues/3738'>#3738</a>)",
            "Optimized clearing ended tasks logic by analyzing and rewriting YDB query, achieving 60x task execution speedup and fixing bug that would lead to incident on 2x load increase (<a href='https://github.com/ydb-platform/nbs/pull/3851'>#3851</a>)",
            "Developed and executed a data integrity verification service task for petabytes of migrated snapshot data, confirming 100% post-migration data consistency",
            "Analyzed and instituted SLO for disk I/O latency and created a dashboard to monitor SLO compliance",
        ],
        "points__ru": [
            "Реализовал новую архитектуру определения зависших задач, что улучшило observability, расширило возможности для диагностики и убрало некорректные срабатывания алерта (<a href='https://github.com/ydb-platform/nbs/issues/3738'>#3738</a>)",
            "Оптимизировал логику очистки завершенных задач путем анализа и рефакторинга запроса в YDB, ускорив выполнение процесса в 60 раз и исправив баг, который привел бы к инциденту при увеличении нагрузки в 2 раза (<a href='https://github.com/ydb-platform/nbs/pull/3851'>#3851</a>)",
            "Разработал и запустил сервисную задачу для проверки чексумм нескольких петабайт мигрированных снэпшотов, подтвердив 100% целостность скопированных данных",
            "Проанализировал и установил SLO для latency дисков и создал дашборд для мониторинга его соблюдения",
        ],
    },
    {
        "name": "Backend Developer Intern",
        "name__ru": "Стажер бэкенд-разработчик",
        "stack": "Python, Django, GitLab CI",
        "period": "July 2024 -- August 2024",
        "period__ru": "Июль 2024 -- Август 2024",
        "company": "VK, VK Maps",
        "company__ru": "VK, VK Карты",
        "location": "Moscow, Russia",
        "location__ru": "Москва, Россия",
        "points": [
            "Developed software for efficient cross-check validation of 100+ GB geo objects data from two sources",
            "Integrated ruff formatter and docker build into CI of 4 projects for proper code quality linting",
        ],
        "points__ru": [
            "Разработал инструмент для эффективной кросс-валидации 100+ ГБ данных гео-объектов из двух источников",
            "Интегрировал ruff formatter и сборку docker-образов в CI 4 проектов для контроля чистоты кода",
        ],
    },
]

PROJECTS = [
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
    {
        "name": "<a href='https://github.com/iamnalinor/prod25-adsplatform'>Ads Platform</a>",
        "stack": "Go, Gin, Python, Aiogram, Postgres, Docker, Ollama",
        "period": "2025",
        "points": [
            "A service for managing ad campaigns with GPT integration, Telegram bot and Grafana dashboards out of the box",
            "Scored 87/100 in the PROD'25 Olympiad finals, <b>#12</b> out of 229 participants",
        ],
        "points__ru": [
            "Сервис для управления рекламными кампаниями с интеграцией с GPT, Telegram-ботом и готовыми дашбордами в Grafana",
            "87/100 баллов на финале олимпиады PROD'25, <b>12</b> место среди 229 участников",
        ],
    },
]

EXTRACURRICULAR_ACTIVITIES = [
    "<b>Go Web Development</b>, Yandex Lyceum, Autumn 2025",
    "<b>Big Data</b>, Yandex Lyceum, Autumn 2024",
    "<b>Data Analytics</b>, Yandex Lyceum, Spring 2024",
    "<b>Algorithms & Data Structures</b>, T-Bank Generation, 2023--2024",
    "<b>Programming in Go</b>, Yandex Lyceum, 2023--2024",
]

EXTRACURRICULAR_ACTIVITIES_RU = [
    "<b>Веб-разработка на Go</b>, Яндекс.Лицей, осень 2025",
    "<b>Большие данные</b>, Яндекс.Лицей, осень 2024",
    "<b>Анализ данных</b>, Яндекс.Лицей, весна 2024",
    "<b>Алгоритмы и структуры данных</b>, Т-Поколение, 2023--2024",
    "<b>Программирование на Go</b>, Яндекс.Лицей, 2023--2024",
]

HONORS_AND_AWARDS = [
    '<b>Finalist</b> of <a href="https://yandex.ru/yaintern/universitybattle">Yandex University Battle</a> (#3 among school students, #33 out of 200), 2026',
    '<b>Winner</b> of <a href="https://cu.ru/events/bachelor-casecontest">DEADLINE case competition</a>, 2026',
    '<b>Winner</b> (2026) and <b>double prize winner</b> (2024, 2025) of <a href="https://prodcontest.ru">PROD Olympiad</a>',
    '<b>Winner</b> (2025) and <b>prize winner</b> (2024) of <a href="https://dano.hse.ru">DANO Olympiad</a>',
    '<b>3-time winner</b> of <a href="https://dano.hse.ru/hackathon/">DANO Hackathon</a> (Saint Petersburg, Yekaterinburg, Perm), 2025',
    '<b>Winner</b> of <a href="https://prodcontest.ru/hackathon/">PROD Hackathon</a>, Moscow, 2024',
]

HONORS_AND_AWARDS_RU = [
    '<b>Финалист</b> <a href="https://yandex.ru/yaintern/universitybattle">Баттла Вузов</a> (#3 среди школьников, 33 место из 200), 2026',
    '<b>Победитель</b> <a href="https://cu.ru/events/bachelor-casecontest">кейс-чемпионата DEADLINE</a>, 2026',
    '<b>Победитель</b> (2026) и <b>дважды призёр</b> (2024, 2025) <a href="https://prodcontest.ru">олимпиады PROD</a>',
    '<b>Победитель</b> (2025) и <b>призёр</b> (2024) <a href="https://dano.hse.ru">олимпиады DANO</a>',
    '<b>3-кратный победитель</b> <a href="https://dano.hse.ru/hackathon/">хакатонов DANO</a> (Санкт-Петербург, Екатеринбург, Пермь), 2025',
    '<b>Победитель</b> <a href="https://prodcontest.ru/hackathon/">хакатона PROD</a>, Москва, 2024',
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
        "value": "Airflow, CI/CD, Docker, Git, Linux, MongoDB, SQL (SQLite, MySQL, Postgres, YDB)",
    },
]

BLOCKS = [
    {
        "type": "text",
        "content": SUMMARY,
        "content__ru": SUMMARY_RU,
        "skip_header": True,
    },
    {
        "name": "Education",
        "name__ru": "Образование",
        "type": "education",
        "content": EDUCATION,
    },
    {
        "name": "Experience",
        "name__ru": "Опыт работы",
        "type": "experience",
        "content": EXPERIENCE,
    },
    {
        "name": "Technical Skills",
        "name__ru": "Технические навыки",
        "type": "mapping",
        "content": TECHNICAL_SKILLS,
    },
    {
        "name": "Projects",
        "name__ru": "Проекты",
        "type": "experience",
        "content": PROJECTS,
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
]
