# ==========================================================
# ThriveDB.py
# Contains a Dictionary to act as a database for Thrive-related data.
# Contains attributes; User Data, Mentor Data, Sleep Data
# ==========================================================

class ThriveDB:
    
    ThriveDBD = {
        "User_data": {"Username": "", "Password": "", "email": ""},
        "mentor_information": [
            {
                "mentor_name": "Dr. Alicia Fernandez",
                "mentor_email": "a.fernandez@university.edu",
                "mentor_phone": "(555) 238-9147",
                "subject": "Math 150",
                "mentor_availability": "Mondays and Wednesdays, 2:00 PM to 4:30 PM (Zoom or Office 312)",
            },
            {
                "mentor_name": "Mr. James Liu",
                "mentor_email": "j.liu@techmentor.org",
                "mentor_phone": "(555) 902-3418",
                "subject": "CS 210",
                "mentor_availability": "Fridays, 10:00 AM to 1:00 PM (Google Meet)",
            },
            {
                "mentor_name": "Prof. Nia Patel",
                "mentor_email": "np@designlab.io",
                "mentor_phone": "(555) 678-2249",
                "subject": "COM 103",
                "mentor_availability": "Tuesdays and Thursdays, 3:00 PM to 5:00 PM (Office Hours)",
            },
        ],
        "Sleep_data": {"sleep_hours": [], "sleep_quality": []},
    }

    def addUserData(self, username, password, email):
        self.ThriveDBD["User_data"]["Username"] = username
        self.ThriveDBD["User_data"]["Password"] = password
        self.ThriveDBD["User_data"]["email"] = email

    def addSleepData(self, hours, quality):
        self.ThriveDBD["Sleep_data"]["sleep_hours"].append(hours)
        self.ThriveDBD["Sleep_data"]["sleep_quality"].append(quality)

    def getMentorInfo(self):
        return self.ThriveDBD["mentor_information"]
    
    