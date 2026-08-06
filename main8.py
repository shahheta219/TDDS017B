import time
def verify_student():
    print(" fetching attendence..")
    time.sleep(3)
    print("student verified")
def fetch_attendence():
    print("fetchingn attendence")
    time.sleep(3)
    print("attendence loaded")

def fetch_marks():
    print("fetching marks")
    time.sleep(2)
    print("maeks loaded")

print(" ========= Student Portal ======\n")
start = time.time()
verify_student()
fetch_attendence()
fetch_marks()
end = time.time()
print (f"\n Total Time = {end - start:.2f} seconds")