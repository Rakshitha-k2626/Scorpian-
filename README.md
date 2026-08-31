# 🦂 Scorpian

### Your Work. Your World.

**Scorpian** is a personal digital space designed to collect, organize, manage, and showcase everything you create — from technical projects and AI experiments to writing, research, creative work, achievements, and ideas.

Instead of keeping different parts of your journey scattered across folders, documents, platforms, and notes, Scorpian brings them together into one personal space.

---

## ✨ Why Scorpian?

A person's journey is more than just a list of projects.

It includes experiments that worked, ideas that didn't, things they learned, articles they wrote, designs they created, achievements they earned, and experiences that shaped them.

**Scorpian is built around that idea.**

> **Your work is not just a portfolio. It is a journey.**

---

## 🚀 Features

### 🔐 Personal Account

* User registration
* Secure password hashing
* Login and logout
* Session-based authentication
* Personal dashboard

### 📚 Personal Work Collection

Create and organize entries such as:

* 💻 Technical projects
* 🤖 AI & ML experiments
* ✍️ Writing
* 🎨 Creative work
* 🔬 Research
* 💡 Ideas
* 🏆 Achievements
* 📸 Media
* 📖 Learning experiences

### 📁 Media Uploads

Scorpian supports attaching different types of files to your entries, including:

* Images
* Videos
* PDFs
* Presentations
* Documents

Uploaded files are stored with unique filenames to avoid collisions.

### 📊 Personal Dashboard

The dashboard provides an overview of your Scorpian journey, including:

* Total entries
* Media entries
* Categories
* Languages used
* Most-used category
* Recent work

### ✏️ Content Management

Users can:

* Add new entries
* Edit existing entries
* Delete entries
* Attach media
* Organize work using categories and subsections

### 🦂 Scorpian Identity System

Scorpian includes a unique identity system that generates an animal-based identity badge.

Possible identities include:

🦂 Scorpion
🦋 Butterfly
🐝 Bee
🐞 Ladybug
🐜 Ant
🐅 Tiger
🦁 Lion
🐘 Elephant
🦊 Fox
🐺 Wolf
🦅 Eagle
🦉 Owl

Each identity represents different characteristics such as curiosity, resilience, creativity, adaptability, persistence, leadership, intelligence, or vision.

### 🏆 Rank & Achievement System

Your Scorpian grows as you add more work.

The system tracks:

* Scorpian entries
* Rank
* Achievement Coins
* Progress toward the next rank
* Unique badge number

### 🪪 Downloadable Identity Badge

After discovering an identity, users can generate a personalized Scorpian badge containing:

* Animal identity
* Identity title
* Description
* Username
* Badge number
* Scorpian rank
* Achievement Coins
* Total entries
* Scorpian profile information

The badge can be downloaded as an SVG file.

### 🌐 Public Scorpian Profile

Each user can have a public Scorpian profile displaying their collected work.

Example:

```text
/scorpian-profile/username
```

This allows a user's Scorpian journey to be viewed as a personal digital showcase.

---

# 🛠️ Technology Stack

### Backend

* Python
* Flask

### Database

* SQLite

### Frontend

* HTML5
* CSS3
* JavaScript

### Security

* Werkzeug password hashing
* Flask sessions
* Secure file handling

### File Handling

* Werkzeug `secure_filename`
* UUID-based unique filenames

---

# 📂 Project Structure

```text
Scorpian-/
│
├── app.py
├── database.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── public.html
│   ├── edit_content.html
│   └── scorpian_item.html
│
└── static/
    │
    ├── css/
    │   └── style.css
    │
    └── uploads/
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/Rakshitha-k2626/Scorpian-.git
```

## 2. Enter the project directory

```bash
cd Scorpian-
```

## 3. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Run Scorpian

```bash
python app.py
```

The application will start locally at:

```text
http://127.0.0.1:5000
```

---

# 🔑 How It Works

```text
                    ┌─────────────────┐
                    │     SCORPIAN    │
                    └────────┬────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
           Register/Login            Explore Home
                │
                ▼
          Personal Dashboard
                │
        ┌───────┼────────┐
        │       │        │
        ▼       ▼        ▼
      Create   Edit    Delete
       Work    Work     Work
        │
        ▼
    Organize Content
        │
        ▼
   Scorpian Identity
        │
        ▼
   Animal Badge + Rank
        │
        ▼
  Public Scorpian Profile
```

---

# 🦂 Scorpian Identity Concept

The animal identity is not intended to classify a person permanently.

Instead, it is a playful representation of the characteristics associated with their Scorpian identity.

For example:

| Identity     | Represents                 |
| ------------ | -------------------------- |
| 🦂 Scorpion  | Resilience & observation   |
| 🦋 Butterfly | Transformation & curiosity |
| 🐝 Bee       | Productivity & creativity  |
| 🐜 Ant       | Persistence & strategy     |
| 🐅 Tiger     | Independence & focus       |
| 🦁 Lion      | Confidence & leadership    |
| 😘 Elephant  | Memory & intelligence      |
| 🦊 Fox       | Adaptability & cleverness  |
| 🐺 Wolf      | Independence & connection  |
| 🦅 Eagle     | Vision & perspective       |
| 🦉 Owl       | Reflection & understanding |

---

# 🎯 Project Goals

Scorpian was created with several goals:

* Create a personal space for different types of work
* Combine technical and non-technical achievements
* Encourage documenting the learning journey
* Provide a personalized digital identity
* Make project organization easier
* Experiment with gamification
* Build a portfolio-like personal experience

---

# 🔮 Future Improvements

Possible future versions of Scorpian could include:

* ☁️ Cloud database
* 🌐 Production deployment
* 📱 Mobile application
* 🔎 Advanced search
* 🏷️ Tags and filters
* 📈 Advanced analytics
* 🎨 More customizable profiles
* 🪪 Improved badge designs
* 📤 Social sharing
* 🔗 Custom Scorpian profile URLs
* 🤖 AI-powered content organization
* 🧠 AI-generated insights about a user's learning journey

---

# 📸 Screenshots

Add screenshots of your application here.

Example:

```text
screenshots/
├── home.png
├── dashboard.png
├── identity.png
└── profile.png
```

Then display them using:

```markdown
![Scorpian Home](screenshots/home.png)
```

---

# 👩‍💻 Developer

### Rakshitha K.

Computer Science & Design Student
Interested in Artificial Intelligence, research, creative technology, and building meaningful digital experiences.

### Connect

**GitHub:**
https://github.com/Rakshitha-k2626

**LinkedIn:**
https://www.linkedin.com/in/rakshitha-k-63718332b/

---

# 📌 Project Status

**Development:** Completed
**Core Features:** Implemented
**Deployment:** Not currently deployed

Scorpian is currently maintained as a personal project and learning experience.

---

## 🦂 Final Thought

Scorpian isn't designed to ask:

> **"What have you achieved?"**

It asks:

> **"What have you created, explored, learned, and become along the way?"**

**Your work. Your world. Your Scorpian. 🦂**
