
(`rushikeshbhabad-focus-guardian/README.md`) 👇

---

```markdown
# 🧠 Focus Guardian – Distraction Blocker

A simple yet powerful Python tool that helps you **stay focused** by automatically blocking distracting websites (like YouTube, Instagram, Netflix) during your working hours — and unblocking them afterward.

---

## 🚀 Features
✅ Blocks distracting websites during focus hours  
✅ Automatically unblocks them after working hours  
✅ Uses your system’s hosts file (no extra apps needed)  
✅ Customizable site list and time schedule  
✅ Lightweight and beginner-friendly — perfect for Hacktoberfest 🎉  

---

## 🗂️ Folder Structure
```

projects/focus-guardian/
├── main.py
├── blocked_sites.txt
└── README.md

````

---

## ⚙️ How It Works
Focus Guardian edits your system’s `/etc/hosts` file to redirect distracting websites to `127.0.0.1` (localhost) during focus hours.  
After the time window ends, it restores your access automatically.

---

## 🧰 Requirements
- Python 3.x  
- Run the script as **Administrator** (Windows) or with **sudo** (Linux/Mac) since it modifies system files.

---

## 💻 Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/beginner-python-mini-projects-hacktoberfest-2025.git
   cd beginner-python-mini-projects-hacktoberfest-2025/src/rushikeshbhabad-focus-guardian
````

2. **Add sites to block**
   Open `blocked_sites.txt` and list all sites you want to block, e.g.:

   ```
   www.youtube.com
   youtube.com
   www.instagram.com
   instagram.com
   ```

3. **Run the script**

   ```bash
   sudo python3 main.py
   ```

4. **Stop anytime**
   Press `Ctrl + C` to stop the program safely.

---

## 🧩 Example Output

```
🕒 Focus Guardian is running... Press Ctrl+C to stop.
⏰ Working hours (9:00 - 17:00) → Blocking distractions.
🚫 Blocked: www.youtube.com
🚫 Blocked: www.instagram.com
🌙 Non-working hours → Unblocking sites.
✅ All sites unblocked for free browsing.
```

---

## ⚠️ Notes

* **Admin rights are required** because the hosts file is a protected system file.
* Make sure to use correct path for your OS:

  * Windows: `C:\Windows\System32\drivers\etc\hosts`
  * Linux/Mac: `/etc/hosts`
* You can adjust focus hours in the script by editing:

  ```python
  focus_start = 9   # Start at 9 AM
  focus_end = 17    # End at 5 PM
  ```

---

## 📜 License

This project is licensed under the **MIT License**.

---

**Made with 💻 and ☕ by [Rushikesh Bhabad](https://github.com/yourusername)**
for **Hacktoberfest 2025** 🎉

```

---

Would you like me to add a small **“next version” note** section at the end (suggesting future upgrades like a GUI or timer integration) — that looks great in Hacktoberfest PRs?
```
