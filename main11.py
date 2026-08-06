from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()

def send_email(email: str):
    print(f"Sending email to: {email}")
    time.sleep(10)  # Simulate sending email
    print("Email sent successfully!")

@app.post("/register")
async def register(email: str, background_tasks: BackgroundTasks):
    print("User registered successfully!")

    # Run send_email in the background
    background_tasks.add_task(send_email, email)

    return {
        "message": "Registration successful",
        "status": "Email will be sent in the background"
    }