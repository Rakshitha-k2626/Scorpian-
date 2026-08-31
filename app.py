from flask import Flask, render_template, request, redirect, session, jsonify, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

import sqlite3
import os
import uuid
import random
import time
from datetime import timedelta
from xml.sax.saxutils import escape


# ============================================================
# SCORPIAN APPLICATION
# ============================================================

app = Flask(__name__)

app.secret_key = "scorpian_secret_key_change_later"
# ============================================================
# PERSONAL PORTFOLIO
# ============================================================

PORTFOLIO_URL = "YOUR_OFFICIAL_PORTFOLIO_LINK_HERE"

# ============================================================
# SESSION CONFIGURATION
# ============================================================

# Keep the user logged in for 30 days
app.permanent_session_lifetime = timedelta(days=30)

# Make Flask sessions permanent
app.config["SESSION_PERMANENT"] = True

# Prevent JavaScript from reading the session cookie
app.config["SESSION_COOKIE_HTTPONLY"] = True

# Helps protect the session cookie
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"


# ============================================================
# CONFIGURATION
# ============================================================

DATABASE_NAME = "database.db"

UPLOAD_FOLDER = os.path.join(
    "static",
    "uploads"
)

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
    "gif",
    "webp",
    "mp4",
    "webm",
    "mov",
    "pdf",
    "ppt",
    "pptx",
    "doc",
    "docx"
}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# ============================================================
# CREATE UPLOAD DIRECTORY
# ============================================================

os.makedirs(
    os.path.join(
        app.root_path,
        UPLOAD_FOLDER
    ),
    exist_ok=True
)


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_db():

    database_path = os.path.join(
        app.root_path,
        DATABASE_NAME
    )

    connection = sqlite3.connect(
        database_path
    )

    connection.row_factory = sqlite3.Row

    return connection


# ============================================================
# DATABASE CREATION
# ============================================================

def create_database():

    connection = get_db()

    # ========================================================
    # USERS
    # ========================================================

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            created_at
            TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)


    # ========================================================
    # CONTENT
    # ========================================================

    connection.execute("""
        CREATE TABLE IF NOT EXISTS content (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER NOT NULL,

            category TEXT NOT NULL,

            subsection TEXT NOT NULL,

            title TEXT NOT NULL,

            description TEXT,

            language TEXT,

            media_filename TEXT,

            media_type TEXT,

            created_at
            TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id)
            REFERENCES users(id)

        )
    """)


    # ========================================================
    # CONTENT MIGRATION
    # ========================================================

    columns = connection.execute(
        "PRAGMA table_info(content)"
    ).fetchall()


    column_names = [
        column["name"]
        for column in columns
    ]


    if "media_filename" not in column_names:

        connection.execute("""
            ALTER TABLE content
            ADD COLUMN media_filename TEXT
        """)


    if "media_type" not in column_names:

        connection.execute("""
            ALTER TABLE content
            ADD COLUMN media_type TEXT
        """)


    connection.commit()

    connection.close()


# ============================================================
# FILE VALIDATION
# ============================================================

def allowed_file(filename):

    if not filename:
        return False

    if "." not in filename:
        return False

    extension = filename.rsplit(
        ".",
        1
    )[1].lower()

    return extension in ALLOWED_EXTENSIONS


# ============================================================
# SCORPIAN ANIMAL BADGES
# ============================================================

SCORPIAN_BADGES = [

    {
        "animal": "🦂",
        "title": "The Scorpion",
        "description":
            "Observant, resilient and quietly powerful. You notice what others miss."
    },

    {
        "animal": "🦋",
        "title": "The Butterfly",
        "description":
            "Curious, adaptive and constantly transforming through new experiences."
    },

    {
        "animal": "🐝",
        "title": "The Bee",
        "description":
            "Creative, productive and always building something meaningful."
    },

    {
        "animal": "🐞",
        "title": "The Ladybug",
        "description":
            "Small but significant, bringing curiosity and balance wherever you go."
    },

    {
        "animal": "🐜",
        "title": "The Ant",
        "description":
            "Persistent and strategic. Small steps become remarkable results."
    },

    {
        "animal": "🐅",
        "title": "The Tiger",
        "description":
            "Independent, focused and confident enough to follow your own path."
    },

    {
        "animal": "🦁",
        "title": "The Lion",
        "description":
            "Bold, expressive and willing to take responsibility for your journey."
    },

    {
        "animal": "🐘",
        "title": "The Elephant",
        "description":
            "Thoughtful, intelligent and deeply connected to memory and experience."
    },

    {
        "animal": "🦊",
        "title": "The Fox",
        "description":
            "Clever, adaptable and always searching for another way forward."
    },

    {
        "animal": "🐺",
        "title": "The Wolf",
        "description":
            "Independent yet connected, balancing individuality with meaningful relationships."
    },

    {
        "animal": "🦅",
        "title": "The Eagle",
        "description":
            "Visionary and observant, always looking at the bigger picture."
    },

    {
        "animal": "🦉",
        "title": "The Owl",
        "description":
            "Reflective, patient and naturally drawn toward deeper understanding."
    },

    {
        "animal": "🐬",
        "title": "The Dolphin",
        "description":
            "Intelligent, social and naturally curious about the world around you."
    },

    {
        "animal": "🐢",
        "title": "The Turtle",
        "description":
            "Patient and persistent. You understand that meaningful progress takes time."
    },

    {
        "animal": "🦚",
        "title": "The Peacock",
        "description":
            "Creative, expressive and unafraid to let your individuality be seen."
    },

    {
        "animal": "🐙",
        "title": "The Octopus",
        "description":
            "Flexible, intelligent and capable of handling many ideas at once."
    },

    {
        "animal": "🐧",
        "title": "The Penguin",
        "description":
            "Determined, adaptable and stronger than you may initially appear."
    },

    {
        "animal": "🦄",
        "title": "The Unicorn",
        "description":
            "Imaginative, unconventional and always looking beyond ordinary possibilities."
    }

]


# ============================================================
# BADGE STORAGE
# ============================================================

def store_current_badge(
    badge_number,
    badge_index
):

    session["badge_number"] = badge_number

    session["badge_index"] = badge_index

    session.modified = True


# ============================================================
# GET CURRENT BADGE
# ============================================================

def get_current_badge():

    badge_index = session.get(
        "badge_index"
    )

    if badge_index is None:

        return None

    try:

        badge_index = int(
            badge_index
        )

    except:

        return None


    if badge_index < 0:

        return None


    if badge_index >= len(
        SCORPIAN_BADGES
    ):

        return None


    return SCORPIAN_BADGES[
        badge_index
    ]


# ============================================================
# SCORPIAN STATISTICS
# ============================================================

def get_scorpian_stats(user_id):

    connection = get_db()


    total_entries = connection.execute("""
        SELECT COUNT(*)
        FROM content
        WHERE user_id = ?
    """, (
        user_id,
    )).fetchone()[0]


    connection.close()


    rank = total_entries // 6

    achievement_coins = total_entries // 6

    entries_into_current_rank = (
        total_entries % 6
    )


    if total_entries < 6:

        next_rank_in = (
            6 - total_entries
        )

    else:

        next_rank_in = (
            6 - entries_into_current_rank
        )

        if entries_into_current_rank == 0:

            next_rank_in = 6


    if rank == 0:

        rank_name = "Starting Scorpian"

    else:

        rank_name = (
            "Scorpian Rank "
            + str(rank)
        )


    return {

        "total_entries":
            total_entries,

        "rank":
            rank,

        "rank_name":
            rank_name,

        "achievement_coins":
            achievement_coins,

        "entries_into_current_rank":
            entries_into_current_rank,

        "next_rank_in":
            next_rank_in

    }


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    logged_in = "user_id" in session

    username = session.get(
        "username",
        None
    )

    scorpian_link = None

    if username:

        scorpian_link = url_for(
            "scorpian_profile",
            username=username
        )

    return render_template(

        "index.html",

        logged_in=logged_in,

        username=username,

        scorpian_link=scorpian_link,

        portfolio_url=PORTFOLIO_URL

    )

# ============================================================
# REGISTER
# ============================================================

@app.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if "user_id" in session:

        return redirect(
            "/dashboard"
        )


    message = ""


    if request.method == "POST":

        username = request.form.get(
            "username",
            ""
        ).strip()


        email = request.form.get(
            "email",
            ""
        ).strip().lower()


        password = request.form.get(
            "password",
            ""
        )


        if (
            not username
            or not email
            or not password
        ):

            message = (
                "Please fill all fields."
            )

            return render_template(
                "register.html",
                message=message
            )


        if len(password) < 6:

            message = (
                "Password must contain at least 6 characters."
            )

            return render_template(
                "register.html",
                message=message
            )


        connection = get_db()


        try:

            # ------------------------------------------------
            # EMAIL CHECK
            # ------------------------------------------------

            existing_email = connection.execute(
                """
                SELECT id
                FROM users
                WHERE LOWER(email) = ?
                """,
                (email,)
            ).fetchone()


            if existing_email:

                message = (
                    "This email is already registered."
                )

                connection.close()

                return render_template(
                    "register.html",
                    message=message
                )


            # ------------------------------------------------
            # USERNAME CHECK
            # ------------------------------------------------

            existing_username = connection.execute(
                """
                SELECT id
                FROM users
                WHERE LOWER(username) = ?
                """,
                (username.lower(),)
            ).fetchone()


            if existing_username:

                message = (
                    "This username is already taken."
                )

                connection.close()

                return render_template(
                    "register.html",
                    message=message
                )


            # ------------------------------------------------
            # HASH PASSWORD
            # ------------------------------------------------

            hashed_password = (
                generate_password_hash(
                    password
                )
            )


            # ------------------------------------------------
            # CREATE USER
            # ------------------------------------------------

            connection.execute(
                """
                INSERT INTO users
                (
                    username,
                    email,
                    password
                )
                VALUES (?, ?, ?)
                """,
                (
                    username,
                    email,
                    hashed_password
                )
            )


            connection.commit()

            connection.close()


            return redirect(
                "/login"
            )


        except Exception as error:

            connection.close()

            print(
                "REGISTER ERROR:",
                error
            )


            message = (
                "Unable to create your Scorpian."
            )


    return render_template(
        "register.html",
        message=message
    )


# ============================================================
# LOGIN
# ============================================================

@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    # --------------------------------------------------------
    # IF ALREADY LOGGED IN
    # --------------------------------------------------------

    if "user_id" in session:

        return redirect(
            "/dashboard"
        )


    message = ""


    if request.method == "POST":

        email = request.form.get(
            "email",
            ""
        ).strip().lower()


        password = request.form.get(
            "password",
            ""
        )


        # ----------------------------------------------------
        # VALIDATION
        # ----------------------------------------------------

        if (
            not email
            or not password
        ):

            message = (
                "Please enter your email and password."
            )

            return render_template(
                "login.html",
                message=message
            )


        connection = get_db()


        user = connection.execute(
            """
            SELECT
                id,
                username,
                email,
                password
            FROM users
            WHERE LOWER(email) = ?
            """,
            (email,)
        ).fetchone()


        connection.close()


        # ----------------------------------------------------
        # USER NOT FOUND
        # ----------------------------------------------------

        if user is None:

            message = (
                "Invalid email or password."
            )

            return render_template(
                "login.html",
                message=message
            )


        # ----------------------------------------------------
        # CHECK PASSWORD
        # ----------------------------------------------------

        try:

            password_valid = (
                check_password_hash(
                    user["password"],
                    password
                )
            )

        except Exception as error:

            print(
                "PASSWORD CHECK ERROR:",
                error
            )

            password_valid = False


        # ----------------------------------------------------
        # SUCCESSFUL LOGIN
        # ----------------------------------------------------

        if password_valid:

            # Clear any old session data
            session.clear()


            # Store logged-in user
            session["user_id"] = (
                user["id"]
            )


            session["username"] = (
                user["username"]
            )


            # Make session persistent
            session.permanent = True


            session.modified = True


            return redirect(
                "/dashboard"
            )


        # ----------------------------------------------------
        # FAILED LOGIN
        # ----------------------------------------------------

        message = (
            "Invalid email or password."
        )


    return render_template(
        "login.html",
        message=message
    )


# ============================================================
# DASHBOARD
# ============================================================

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:

        return redirect(
            "/login"
        )


    connection = get_db()


    content = connection.execute("""
        SELECT *
        FROM content
        WHERE user_id = ?
        ORDER BY created_at DESC
    """, (
        session["user_id"],
    )).fetchall()


    total_entries = connection.execute("""
        SELECT COUNT(*)
        FROM content
        WHERE user_id = ?
    """, (
        session["user_id"],
    )).fetchone()[0]


    media_count = connection.execute("""
        SELECT COUNT(*)
        FROM content
        WHERE user_id = ?
        AND media_filename IS NOT NULL
        AND media_filename != ''
    """, (
        session["user_id"],
    )).fetchone()[0]


    category_count = connection.execute("""
        SELECT COUNT(
            DISTINCT category
        )
        FROM content
        WHERE user_id = ?
    """, (
        session["user_id"],
    )).fetchone()[0]


    language_count = connection.execute("""
        SELECT COUNT(
            DISTINCT language
        )
        FROM content
        WHERE user_id = ?
        AND language IS NOT NULL
        AND language != ''
    """, (
        session["user_id"],
    )).fetchone()[0]


    most_used_category = connection.execute("""
        SELECT
            category,
            COUNT(*) AS total
        FROM content
        WHERE user_id = ?
        GROUP BY category
        ORDER BY total DESC
        LIMIT 1
    """, (
        session["user_id"],
    )).fetchone()


    connection.close()


    stats = get_scorpian_stats(
        session["user_id"]
    )


    return render_template(

        "dashboard.html",

        username=session["username"],

        content=content,

        total_entries=total_entries,

        media_count=media_count,

        category_count=category_count,

        language_count=language_count,

        most_used_category=most_used_category,

        rank=stats["rank"],

        rank_name=stats["rank_name"],

        achievement_coins=stats[
            "achievement_coins"
        ],

        next_rank_in=stats[
            "next_rank_in"
        ]

    )


# ============================================================
# SAVE CONTENT
# ============================================================

@app.route(
    "/save-content",
    methods=["POST"]
)
def save_content():

    if "user_id" not in session:

        return redirect(
            "/login"
        )


    category = request.form.get(
        "category",
        ""
    ).strip()


    subsection = request.form.get(
        "subsection",
        ""
    ).strip()


    title = request.form.get(
        "title",
        ""
    ).strip()


    description = request.form.get(
        "description",
        ""
    ).strip()


    language = request.form.get(
        "language",
        "English"
    ).strip()


    if (
        not category
        or not subsection
        or not title
    ):

        return redirect(
            "/dashboard"
        )


    media_filename = None

    media_type = None


    media = request.files.get(
        "media"
    )


    if media and media.filename:

        if allowed_file(
            media.filename
        ):

            original_filename = (
                secure_filename(
                    media.filename
                )
            )


            unique_filename = (

                str(session["user_id"])

                + "_"

                + str(uuid.uuid4())

                + "_"

                + original_filename

            )


            media_path = os.path.join(

                app.root_path,

                UPLOAD_FOLDER,

                unique_filename

            )


            media.save(
                media_path
            )


            media_filename = (
                unique_filename
            )


            media_type = (
                media.mimetype
            )


    connection = get_db()


    connection.execute("""
        INSERT INTO content
        (
            user_id,
            category,
            subsection,
            title,
            description,
            language,
            media_filename,
            media_type
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        session["user_id"],

        category,

        subsection,

        title,

        description,

        language,

        media_filename,

        media_type

    ))


    connection.commit()

    connection.close()


    return redirect(
        "/dashboard"
    )


# ============================================================
# EDIT CONTENT
# ============================================================

@app.route(
    "/edit-content/<int:content_id>",
    methods=["GET", "POST"]
)
def edit_content(content_id):

    if "user_id" not in session:

        return redirect(
            "/login"
        )


    connection = get_db()


    item = connection.execute("""
        SELECT *
        FROM content

        WHERE id = ?

        AND user_id = ?

    """, (

        content_id,

        session["user_id"]

    )).fetchone()


    if not item:

        connection.close()

        return redirect(
            "/dashboard"
        )


    if request.method == "POST":

        title = request.form.get(
            "title",
            ""
        ).strip()


        description = request.form.get(
            "description",
            ""
        ).strip()


        subsection = request.form.get(
            "subsection",
            ""
        ).strip()


        language = request.form.get(
            "language",
            "English"
        ).strip()


        if (
            title
            and subsection
        ):

            connection.execute("""
                UPDATE content

                SET
                    title = ?,
                    description = ?,
                    subsection = ?,
                    language = ?

                WHERE id = ?

                AND user_id = ?

            """, (

                title,

                description,

                subsection,

                language,

                content_id,

                session["user_id"]

            ))


            connection.commit()


        connection.close()


        return redirect(
            "/dashboard"
        )


    connection.close()


    return render_template(
        "edit_content.html",
        item=item
    )


# ============================================================
# DELETE CONTENT
# ============================================================

@app.route(
    "/delete-content/<int:content_id>",
    methods=["POST"]
)
def delete_content(content_id):

    if "user_id" not in session:

        return redirect(
            "/login"
        )


    connection = get_db()


    item = connection.execute("""
        SELECT *
        FROM content

        WHERE id = ?

        AND user_id = ?

    """, (

        content_id,

        session["user_id"]

    )).fetchone()


    if item:

        if item["media_filename"]:

            media_path = os.path.join(

                app.root_path,

                UPLOAD_FOLDER,

                item["media_filename"]

            )


            if os.path.exists(
                media_path
            ):

                os.remove(
                    media_path
                )


        connection.execute("""
            DELETE FROM content

            WHERE id = ?

            AND user_id = ?

        """, (

            content_id,

            session["user_id"]

        ))


        connection.commit()


    connection.close()


    return redirect(
        "/dashboard"
    )


# ============================================================
# PUBLIC SCORPIAN
# ============================================================

@app.route("/public")
def public():

    if "user_id" not in session:

        return redirect(
            "/login"
        )


    connection = get_db()


    content = connection.execute("""
        SELECT *
        FROM content

        WHERE user_id = ?

        ORDER BY created_at DESC

    """, (
        session["user_id"],
    )).fetchall()


    category_rows = connection.execute("""
        SELECT DISTINCT category

        FROM content

        WHERE user_id = ?

        ORDER BY category

    """, (
        session["user_id"],
    )).fetchall()


    categories = [
        row["category"]
        for row in category_rows
    ]


    projects_count = connection.execute("""
        SELECT COUNT(*)

        FROM content

        WHERE user_id = ?

        AND subsection = ?

    """, (

        session["user_id"],

        "Projects"

    )).fetchone()[0]


    connection.close()


    stats = get_scorpian_stats(
        session["user_id"]
    )


    current_badge = get_current_badge()


    return render_template(

        "public.html",

        username=session["username"],

        content=content,

        categories=categories,

        projects_count=projects_count,

        total_entries=stats[
            "total_entries"
        ],

        rank=stats[
            "rank"
        ],

        rank_name=stats[
            "rank_name"
        ],

        achievement_coins=stats[
            "achievement_coins"
        ],

        current_badge=current_badge

    )


# ============================================================
# PUBLIC SCORPIAN PROFILE
# ============================================================

@app.route(
    "/scorpian-profile/<username>"
)
def scorpian_profile(username):

    connection = get_db()


    user = connection.execute("""
        SELECT
            id,
            username
        FROM users
        WHERE username = ?

    """, (
        username,
    )).fetchone()


    if not user:

        connection.close()

        return (
            "Scorpian not found.",
            404
        )


    content = connection.execute("""
        SELECT *
        FROM content

        WHERE user_id = ?

        ORDER BY created_at DESC

    """, (
        user["id"],
    )).fetchall()


    category_rows = connection.execute("""
        SELECT DISTINCT category

        FROM content

        WHERE user_id = ?

        ORDER BY category

    """, (
        user["id"],
    )).fetchall()


    categories = [
        row["category"]
        for row in category_rows
    ]


    projects_count = connection.execute("""
        SELECT COUNT(*)

        FROM content

        WHERE user_id = ?

        AND subsection = ?

    """, (

        user["id"],

        "Projects"

    )).fetchone()[0]


    connection.close()


    stats = get_scorpian_stats(
        user["id"]
    )


    current_badge = None


    if (
        "user_id" in session
        and session["user_id"] == user["id"]
    ):

        current_badge = get_current_badge()


    return render_template(

        "public.html",

        username=user["username"],

        content=content,

        categories=categories,

        projects_count=projects_count,

        total_entries=stats[
            "total_entries"
        ],

        rank=stats[
            "rank"
        ],

        rank_name=stats[
            "rank_name"
        ],

        achievement_coins=stats[
            "achievement_coins"
        ],

        current_badge=current_badge

    )


# ============================================================
# VIEW SINGLE SCORPIAN ITEM
# ============================================================

@app.route(
    "/scorpian/<int:content_id>"
)
def view_scorpian_item(content_id):

    if "user_id" not in session:

        return redirect(
            "/login"
        )


    connection = get_db()


    item = connection.execute("""
        SELECT *
        FROM content

        WHERE id = ?

        AND user_id = ?

    """, (

        content_id,

        session["user_id"]

    )).fetchone()


    connection.close()


    if not item:

        return redirect(
            "/public"
        )


    return render_template(

        "scorpian_item.html",

        item=item,

        username=session["username"]

    )


# ============================================================
# RUN SCORPIAN
# ============================================================

@app.route(
    "/run-scorpian"
)
def run_scorpian():

    if "user_id" not in session:

        return jsonify({

            "success": False,

            "message":
                "Please login first."

        }), 401


    stats = get_scorpian_stats(
        session["user_id"]
    )


    # --------------------------------------------------------
    # PREVIOUS ANIMAL
    # --------------------------------------------------------

    previous_badge_index = session.get(
        "badge_index"
    )


    available_indexes = list(
        range(
            len(SCORPIAN_BADGES)
        )
    )


    # --------------------------------------------------------
    # REMOVE PREVIOUS ANIMAL
    # --------------------------------------------------------

    if (
        previous_badge_index is not None
        and len(available_indexes) > 1
    ):

        try:

            previous_badge_index = int(
                previous_badge_index
            )


            if (
                previous_badge_index
                in available_indexes
            ):

                available_indexes.remove(
                    previous_badge_index
                )

        except:

            pass


    # --------------------------------------------------------
    # SELECT NEW ANIMAL
    # --------------------------------------------------------

    badge_index = random.choice(
        available_indexes
    )


    badge = SCORPIAN_BADGES[
        badge_index
    ]


    # --------------------------------------------------------
    # BADGE NUMBER
    # --------------------------------------------------------

    badge_number = int(
        time.time() * 1000
    ) % 1000000


    # --------------------------------------------------------
    # SAVE BADGE
    # --------------------------------------------------------

    store_current_badge(
        badge_number,
        badge_index
    )


    # --------------------------------------------------------
    # OFFICIAL PROFILE
    # --------------------------------------------------------

    official_link = url_for(

        "scorpian_profile",

        username=session["username"],

        _external=True

    )


    # --------------------------------------------------------
    # DOWNLOAD
    # --------------------------------------------------------

    download_link = url_for(

        "download_badge",

        badge_number=badge_number,

        _external=True

    )


    return jsonify({

        "success": True,

        "animal":
            badge["animal"],

        "title":
            badge["title"],

        "description":
            badge["description"],

        "badge_number":
            badge_number,

        "official_link":
            official_link,

        "download_link":
            download_link,

        "total_entries":
            stats["total_entries"],

        "rank":
            stats["rank"],

        "rank_name":
            stats["rank_name"],

        "achievement_coins":
            stats["achievement_coins"],

        "next_rank_in":
            stats["next_rank_in"]

    })


# ============================================================
# DOWNLOAD BADGE
# ============================================================

@app.route(
    "/download-badge/<int:badge_number>"
)
def download_badge(badge_number):

    if "user_id" not in session:

        return redirect(
            "/login"
        )


    badge = get_current_badge()


    if badge is None:

        badge_index = (
            badge_number
            % len(SCORPIAN_BADGES)
        )


        badge = SCORPIAN_BADGES[
            badge_index
        ]


    stats = get_scorpian_stats(
        session["user_id"]
    )


    username = session.get(
        "username",
        "Scorpian Owner"
    )


    official_link = url_for(

        "scorpian_profile",

        username=username,

        _external=True

    )


    safe_username = escape(
        username
    )


    safe_title = escape(
        badge["title"]
    )


    safe_description = escape(
        badge["description"]
    )


    safe_official_link = escape(
        official_link
    )


    # ========================================================
    # SVG
    # ========================================================

    svg = f"""<?xml version="1.0" encoding="UTF-8"?>

<svg
    xmlns="http://www.w3.org/2000/svg"
    width="1200"
    height="800"
    viewBox="0 0 1200 800">

    <defs>

        <linearGradient
            id="background"
            x1="0%"
            y1="0%"
            x2="100%"
            y2="100%">

            <stop
                offset="0%"
                stop-color="#ffffff"/>

            <stop
                offset="100%"
                stop-color="#eeeeee"/>

        </linearGradient>

    </defs>


    <rect
        width="1200"
        height="800"
        rx="45"
        fill="url(#background)"/>


    <rect
        x="25"
        y="25"
        width="1150"
        height="750"
        rx="35"
        fill="none"
        stroke="#111111"
        stroke-width="4"/>


    <text
        x="600"
        y="100"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="34"
        font-weight="bold"
        fill="#111111">

        SCORPIAN

    </text>


    <text
        x="600"
        y="145"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="20"
        fill="#666666">

        PERSONAL ACHIEVEMENT BADGE

    </text>


    <text
        x="600"
        y="260"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="110">

        {badge["animal"]}

    </text>


    <text
        x="600"
        y="350"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="48"
        font-weight="bold"
        fill="#111111">

        {safe_title}

    </text>


    <text
        x="600"
        y="400"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="22"
        fill="#444444">

        {safe_description}

    </text>


    <text
        x="600"
        y="475"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="28"
        font-weight="bold"
        fill="#111111">

        {safe_username}

    </text>


    <text
        x="600"
        y="520"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="21"
        fill="#555555">

        BADGE #{badge_number}

    </text>


    <text
        x="600"
        y="575"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="28"
        font-weight="bold"
        fill="#111111">

        {stats["rank_name"]}

    </text>


    <text
        x="600"
        y="625"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="22"
        fill="#444444">

        Achievement Coins:
        {stats["achievement_coins"]}

    </text>


    <text
        x="600"
        y="670"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="21"
        fill="#555555">

        {stats["total_entries"]} Scorpian Entries

    </text>


    <text
        x="600"
        y="720"
        text-anchor="middle"
        font-family="Arial, sans-serif"
        font-size="17"
        fill="#777777">

        {safe_official_link}

    </text>

</svg>
"""


    response = app.response_class(

        svg,

        mimetype="image/svg+xml"

    )


    response.headers[
        "Content-Disposition"
    ] = (

        "attachment; "

        "filename=scorpian_badge_"

        + str(badge_number)

        + ".svg"

    )


    return response


# ============================================================
# LOGOUT
# ============================================================

@app.route(
    "/logout"
)
def logout():

    # Completely remove login session

    session.clear()

    return redirect(
        "/"
    )


# ============================================================
# START SCORPIAN
# ============================================================

if __name__ == "__main__":

    create_database()

    app.run(
        debug=True
    )