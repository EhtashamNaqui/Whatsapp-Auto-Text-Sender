from apscheduler.schedulers.blocking import BlockingScheduler
from automate import send_text
# Here send_text is the function you already created in automation.py



sched = BlockingScheduler()

# Schedule job_function to be called every two hours (set according to your need)
sched.add_job(send_text, 'interval', hours=2)

sched.start()