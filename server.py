import http.server
import socketserver
import json
import os

def load_tasks():
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as f:
            return json.load(f)
    return []

def save_tasks():
    with open('tasks.txt', 'w') as f:
        json.dump(tasks, f, indent=2)

tasks = load_tasks()
task_id_counter = max([task['id'] for task in tasks]) + 1 if tasks else 1

class TaskHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/tasks':
            self.handle_create_task()
        elif self.path.startswith('/tasks/') and self.path.endswith('/complete'):
            self.handle_complete_task()
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        if self.path == '/tasks':
            self.handle_get_tasks()
        else:
            self.send_response(404)
            self.end_headers()

    def handle_create_task(self):
        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)
            if 'title' not in data or 'priority' not in data:
                self.send_error(400, "Missing 'title' or 'priority'")
                return
            global task_id_counter
            new_task = {
                "id": task_id_counter,
                "title": data["title"],
                "priority": data["priority"],
                "isDone": False
            }
            tasks.append(new_task)
            task_id_counter += 1
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data_to_send = json.dumps(new_task)
            self.wfile.write(data_to_send.encode('utf-8'))  # Исправление для строки 39 — явное преобразование в байты
            save_tasks()
        except Exception as e:
            self.send_error(500, str(e))

    def handle_get_tasks(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data_to_send = json.dumps(tasks)
        self.wfile.write(data_to_send.encode('utf-8'))  # Исправление для строки 39

    def handle_complete_task(self):
        try:
            task_id = int(self.path.split('/')[-2])
            for task in tasks:
                if task["id"] == task_id:
                    task["isDone"] = True
                    self.send_response(200)
                    self.end_headers()
                    save_tasks()
                    return
            self.send_response(404)
            self.end_headers()
        except (ValueError, IndexError):
            self.send_response(400)
            self.end_headers()
        except Exception as e:
            self.send_error(500, str(e))

if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), TaskHandler) as httpd:
        print(f"Server running on port {PORT}")
        httpd.serve_forever()
