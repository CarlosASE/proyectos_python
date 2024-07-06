import matplotlib.pyplot as plt
import random
import datetime

class BugReport:
    def __init__(self, id, description, severity, status='open'):
        self.id = id
        self.description = description
        self.severity = severity
        self.status = status
        self.date_reported = datetime.datetime.now().date()

    def __str__(self):
        return f"ID: {self.id}, Description: {self.description}, Severity: {self.severity}, Status: {self.status}, Date Reported: {self.date_reported}"

class BugTracker:
    def __init__(self):
        self.bug_reports = []

    def add_bug_report(self, description, severity):
        bug_id = len(self.bug_reports) + 1
        new_bug = BugReport(bug_id, description, severity)
        self.bug_reports.append(new_bug)
        print(f"Bug report added: {new_bug}")

    def list_bug_reports(self):
        for bug in self.bug_reports:
            print(bug)

# Simulación del incremento diario de bugs
bug_tracker = BugTracker()
start_date = datetime.datetime(2024, 1, 1)
num_days = 30
daily_bugs = []

for day in range(num_days):
    current_date = start_date + datetime.timedelta(days=day)
    num_new_bugs = random.randint(1, 10)  # Simulando entre 1 y 10 bugs nuevos por día
    daily_bugs.append(num_new_bugs)
    for _ in range(num_new_bugs):
        bug_tracker.add_bug_report(f"Bug reportado el {current_date}", random.choice(['Low', 'Medium', 'High']))

# Graficar el incremento diario de bugs
dates = [start_date + datetime.timedelta(days=i) for i in range(num_days)]
total_bugs = [sum(daily_bugs[:i+1]) for i in range(num_days)]

plt.figure(figsize=(10, 5))
plt.plot(dates, total_bugs, marker='o', linestyle='-', color='b')
plt.xlabel('Fecha')
plt.ylabel('Total de Bugs Reportados')
plt.title('Incremento Diario de Bugs Reportados')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()