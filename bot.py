import time
from datetime import datetime


class InstagramScheduler:

    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, caption, time_str):
        """
        time_str format: HH:MM (24 hour)
        """
        self.posts.append({
            "caption": caption,
            "time": time_str,
            "posted": False
        })

        print("Post Scheduled Successfully ✅")

    def start(self):
        print("\n📸 Instagram Scheduler Started...")
        print("User:", self.username)

        while True:

            now = datetime.now().strftime("%H:%M")

            for post in self.posts:

                if post["time"] == now and not post["posted"]:

                    self.publish(post)
                    post["posted"] = True

            time.sleep(30)

    def publish(self, post):
        print("\n🚀 Posting...")
        print("Caption:", post["caption"])
        print("Time:", post["time"])
        print("Status: Posted Successfully ✅")


# ================= MAIN =================

print("===== Instagram Post Scheduler =====")

username = input("Enter Instagram Username: ")

bot = InstagramScheduler(username)


while True:

    print("\n1. Add Post")
    print("2. Start Scheduler")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        caption = input("Enter Caption: ")
        time_str = input("Enter Time (HH:MM): ")

        bot.add_post(caption, time_str)

    elif choice == "2":

        bot.start()

    elif choice == "3":

        print("Goodbye 👋")
        break

    else:
        print("Invalid Choice ❌")
