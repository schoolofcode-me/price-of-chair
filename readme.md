# Pricing Service

This is an application built to allow the periodic scanning of online webstores, to notify users of changes in prices of items they select.

It allows administrators (defined via `src/config.py`) to add, remove, and edit online stores.

It parses the store websites using `requests` and `BeautifulSoup`.

It **does not work with Stores that dynamically inject content using JavaScript**.

It allows users to register, log in, and create and modify their alerts.

Technology stack: MongoDB, Python (Flask & Jinja2), HTML/CSS/Bootstrap.

![Home Screen](readme-files/home.png)

![Sign up Screen](readme-files/signup.png)

![Alerts Screen](readme-files/alerts.png)

![Create Alert Screen](readme-files/create_alert.png)

![Stores Screen](readme-files/stores.png)

![Edit Store Screen](readme-files/edit_store.png)