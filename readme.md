# Rest API From Scratch

A minimalist HTTP server built from scratch in Python using raw sockets. Inspired by Django's project structure, this server allows you to start it via `manage.py` with a familiar `runserver` command.

---

## Getting Started

### Run the Server

```bash
python manage.py runserver [host] [port]
```

**Examples:**

```bash
python manage.py runserver 
python manage.py runserver 0.0.0.0 8080
```

By default, the server runs on `127.0.0.1:8000`.

## ⚙️ Project Structure

```bash
rest_api_from_scratch/ 
├── manage.py 
├── socket_server/ 
│   ├── __init__.py 
│   ├── server_socket.py 
│   └── utils.py  # (e.g., create_http_response, parse_http_request) └── README.md
```



---

## 📡 What It Does

- Accepts incoming socket connections
- Parses basic HTTP requests
- Sends a static `200 OK` HTTP response

---

## 📦 Dependencies

Only Python’s standard library is used:

- `socket`
- `sys`

---

## 🛑 Stopping the Server

Press `Ctrl+C` in the terminal to stop the server gracefully.

---

## 📌 To-Do

-  Support multiple clients (`threading` or `asyncio`)
-  Parse GET/POST parameters
-  Implement routing
-  Support HTML/JSON responses
-  Add logging
-  Write unit tests

---

## 👤 Author

Project for educational purposes and low-level experimentation.  
Author: **[Your Name]**
