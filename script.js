/* =========================================================
   SCORPIAN CATEGORY DATA
========================================================= */

const categoryData = {

    technical: {

        title: "Add Technical Work",

        description:
            "Add projects, AI, GenAI, coding, research, experiments or technical talks.",

        sections: [
            "Projects",
            "AI / GenAI",
            "Coding",
            "Research",
            "Experiments",
            "Technical Articles",
            "Technical Talks"
        ]

    },


    nontechnical: {

        title: "Add Non-Technical Work",

        description:
            "Add stories, articles, reflections, observations, experiences or talks.",

        sections: [
            "Stories",
            "Articles",
            "Reflections",
            "Observations",
            "Experiences",
            "Talks"
        ]

    },


    creative: {

        title: "Add Creative Work",

        description:
            "Add designs, photography, videos, presentations and other creative work.",

        sections: [
            "Designs",
            "Photography",
            "Videos",
            "Presentations",
            "Creative Work"
        ]

    },


    research: {

        title: "Add Research",

        description:
            "Record research ideas, papers, literature reviews, experiments and discoveries.",

        sections: [
            "Research Ideas",
            "Papers",
            "Literature Review",
            "Experiments",
            "Discoveries"
        ]

    },


    knowledge: {

        title: "Add Knowledge",

        description:
            "Keep track of things you learn, books you read, questions and ideas.",

        sections: [
            "Books",
            "Notes",
            "Things I Learned",
            "Questions",
            "Ideas"
        ]

    },


    journey: {

        title: "Add Journey Entry",

        description:
            "Record certifications, internships, competitions, events and achievements.",

        sections: [
            "Certifications",
            "Internships",
            "Competitions",
            "Events",
            "Achievements"
        ]

    },


    media: {

        title: "Add Media",

        description:
            "Keep your videos, photographs, presentations and other visual memories.",

        sections: [
            "Videos",
            "Photographs",
            "Presentations",
            "Other Media"
        ]

    },


    ideas: {

        title: "Add Idea or Experiment",

        description:
            "Record unfinished thoughts, observations, experiments and questions.",

        sections: [
            "Ideas",
            "Observations",
            "Experiments",
            "Questions"
        ]

    }

};


/* =========================================================
   OPEN CATEGORY
========================================================= */

function openCategory(category) {

    const panel =
        document.getElementById("contentPanel");

    const title =
        document.getElementById("panelTitle");

    const description =
        document.getElementById("panelDescription");

    const selectedCategory =
        document.getElementById("selectedCategory");

    const categorySelect =
        document.getElementById("categorySelect");


    if (
        !panel ||
        !title ||
        !description ||
        !selectedCategory ||
        !categorySelect
    ) {

        console.error(
            "Scorpian content panel not found."
        );

        return;

    }


    const data =
        categoryData[category];


    if (!data) {

        console.error(
            "Unknown category:",
            category
        );

        return;

    }


    title.textContent =
        data.title;


    description.textContent =
        data.description;


    selectedCategory.value =
        category;


    categorySelect.innerHTML =
        "";


    const defaultOption =
        document.createElement("option");


    defaultOption.value =
        "";


    defaultOption.textContent =
        "Select a section";


    defaultOption.disabled =
        true;


    defaultOption.selected =
        true;


    categorySelect.appendChild(
        defaultOption
    );


    data.sections.forEach(
        function(section) {

            const option =
                document.createElement("option");


            option.value =
                section;


            option.textContent =
                section;


            categorySelect.appendChild(
                option
            );

        }
    );


    panel.classList.add(
        "active"
    );


    document.body.style.overflow =
        "hidden";


    const titleInput =
        document.getElementById(
            "contentTitle"
        );


    if (titleInput) {

        setTimeout(
            function() {

                titleInput.focus();

            },
            100
        );

    }

}


/* =========================================================
   OPEN SPECIFIC SUBSECTION
========================================================= */

function openSubsection(
    category,
    subsection
) {

    const panel =
        document.getElementById(
            "contentPanel"
        );


    const title =
        document.getElementById(
            "panelTitle"
        );


    const description =
        document.getElementById(
            "panelDescription"
        );


    const selectedCategory =
        document.getElementById(
            "selectedCategory"
        );


    const categorySelect =
        document.getElementById(
            "categorySelect"
        );


    if (
        !panel ||
        !title ||
        !description ||
        !selectedCategory ||
        !categorySelect
    ) {

        console.error(
            "Scorpian content panel not found."
        );

        return;

    }


    const data =
        categoryData[category];


    if (!data) {

        console.error(
            "Unknown category:",
            category
        );

        return;

    }


    title.textContent =
        "Add " + subsection;


    description.textContent =
        data.description;


    selectedCategory.value =
        category;


    categorySelect.innerHTML =
        "";


    const option =
        document.createElement(
            "option"
        );


    option.value =
        subsection;


    option.textContent =
        subsection;


    option.selected =
        true;


    categorySelect.appendChild(
        option
    );


    panel.classList.add(
        "active"
    );


    document.body.style.overflow =
        "hidden";


    const titleInput =
        document.getElementById(
            "contentTitle"
        );


    if (titleInput) {

        setTimeout(
            function() {

                titleInput.focus();

            },
            100
        );

    }

}


/* =========================================================
   CLOSE CATEGORY
========================================================= */

function closeCategory() {

    const panel =
        document.getElementById(
            "contentPanel"
        );


    if (!panel) {

        return;

    }


    panel.classList.remove(
        "active"
    );


    document.body.style.overflow =
        "";


    const form =
        panel.querySelector(
            "form"
        );


    if (form) {

        form.reset();

    }


    const selectedCategory =
        document.getElementById(
            "selectedCategory"
        );


    if (selectedCategory) {

        selectedCategory.value =
            "";

    }

}


/* =========================================================
   RUN SCORPIAN — IDENTITY BADGES
========================================================= */

const scorpianBadges = [

    {
        animal: "🦂",
        title: "The Scorpion",
        description:
            "Observant, resilient and quietly powerful. You notice what others miss.",
        link:
            "https://animaldiversity.org/accounts/Scorpiones/"
    },

    {
        animal: "🦋",
        title: "The Butterfly",
        description:
            "Curious, adaptive and constantly transforming through new experiences.",
        link:
            "https://www.si.edu/spotlight/buginfo/butterfly"
    },

    {
        animal: "🐝",
        title: "The Bee",
        description:
            "Creative, productive and always building something meaningful.",
        link:
            "https://www.si.edu/spotlight/buginfo/bee"
    },

    {
        animal: "🐞",
        title: "The Ladybug",
        description:
            "Small but significant — bringing curiosity and balance wherever you go.",
        link:
            "https://www.si.edu/spotlight/buginfo/ladybug"
    },

    {
        animal: "🐜",
        title: "The Ant",
        description:
            "Persistent and strategic. Small steps become remarkable results.",
        link:
            "https://animaldiversity.org/accounts/Formicidae/"
    },

    {
        animal: "🐅",
        title: "The Tiger",
        description:
            "Independent, focused and confident enough to follow your own path.",
        link:
            "https://www.iucnredlist.org/species/15955/214862019"
    },

    {
        animal: "🦁",
        title: "The Lion",
        description:
            "Bold, expressive and willing to take responsibility for your journey.",
        link:
            "https://www.iucnredlist.org/species/15951/115130419"
    },

    {
        animal: "🐘",
        title: "The Elephant",
        description:
            "Thoughtful, intelligent and deeply connected to memory and experience.",
        link:
            "https://www.iucnredlist.org/species/181008073/181022663"
    },

    {
        animal: "🦊",
        title: "The Fox",
        description:
            "Clever, adaptable and always searching for another way forward.",
        link:
            "https://animaldiversity.org/accounts/Vulpes_vulpes/"
    },

    {
        animal: "🐺",
        title: "The Wolf",
        description:
            "Independent yet connected, balancing individuality with meaningful relationships.",
        link:
            "https://www.iucnredlist.org/species/3746/197362031"
    },

    {
        animal: "🦅",
        title: "The Eagle",
        description:
            "Visionary and observant, always looking at the bigger picture.",
        link:
            "https://www.iucnredlist.org/"
    },

    {
        animal: "🦉",
        title: "The Owl",
        description:
            "Reflective, patient and naturally drawn toward deeper understanding.",
        link:
            "https://www.si.edu/spotlight/buginfo/owl"
    }

];



/* =========================================================
   RUN SCORPIAN — CONNECTED TO FLASK
========================================================= */

async function runScorpian() {

    const button =
        document.getElementById(
            "runScorpianButton"
        );

    const label =
        document.querySelector(
            ".run-label"
        );

    const identitySection =
        document.getElementById(
            "identitySection"
        );

    const identityAnimal =
        document.getElementById(
            "identityAnimal"
        );

    const identityTitle =
        document.getElementById(
            "identityTitle"
        );

    const identityDescription =
        document.getElementById(
            "identityDescription"
        );

    const identityNumber =
        document.getElementById(
            "identityNumber"
        );

    const officialInfoLink =
        document.getElementById(
            "officialInfoLink"
        );
    const downloadBadgeButton =
    document.getElementById(
        "downloadBadgeButton"
    );

if (downloadBadgeButton) {

    downloadBadgeButton.href =
        data.download_link || "#";

}
const rankElement =
    document.getElementById(
        "identityRank"
    );

const coinsElement =
    document.getElementById(
        "identityCoins"
    );


if (rankElement) {

    rankElement.textContent =
        data.rank_name;

}


if (coinsElement) {

    coinsElement.textContent =
        "🪙 " +
        data.achievement_coins +
        " Achievement Coins";

}

    /* =====================================================
       CHECK REQUIRED ELEMENTS
    ===================================================== */

    if (
        !button ||
        !identitySection ||
        !identityAnimal ||
        !identityTitle ||
        !identityDescription ||
        !identityNumber ||
        !officialInfoLink
    ) {

        console.error(
            "Scorpian identity elements not found."
        );

        return;

    }


    /* =====================================================
       LOADING STATE
    ===================================================== */

    button.disabled = true;

    button.classList.add(
        "running"
    );


    if (label) {

        label.textContent =
            "GENERATING IDENTITY...";

    }


    /* =====================================================
       SMALL ANIMATION DELAY
    ===================================================== */

    await new Promise(
        function(resolve) {

            setTimeout(
                resolve,
                700
            );

        }
    );


    try {

        /* =================================================
           CALL FLASK
        ================================================= */

        const response =
            await fetch(
                "/run-scorpian",
                {
                    method: "GET",
                    headers: {
                        "Accept":
                            "application/json"
                    }
                }
            );


        /* =================================================
           CHECK SERVER RESPONSE
        ================================================= */

        if (!response.ok) {

            throw new Error(
                "Server returned HTTP " +
                response.status
            );

        }


        const data =
            await response.json();


        /* =================================================
           CHECK FLASK DATA
        ================================================= */

        if (!data.success) {

            throw new Error(
                "Scorpian identity generation failed."
            );

        }


        /* =================================================
           UPDATE IDENTITY
        ================================================= */

        identityAnimal.textContent =
            data.animal || "🦂";


        identityTitle.textContent =
            data.title || "The Scorpion";


        identityDescription.textContent =
            data.description || "";


        identityNumber.textContent =
            "BADGE #" +
            data.badge_number;


        officialInfoLink.href =
            data.official_link || "#";


        /* =================================================
           SHOW IDENTITY
        ================================================= */

        identitySection.classList.add(
            "identity-visible"
        );


        /*
         * Some versions of the CSS may use
         * badge-visible instead.
         *
         * Adding both is harmless and makes
         * the display compatible.
         */

        identitySection.classList.add(
            "badge-visible"
        );


        /* =================================================
           BUTTON SUCCESS
        ================================================= */

        if (label) {

            label.textContent =
                "SCORPIAN READY";

        }


        /* =================================================
           SCROLL TO IDENTITY
        ================================================= */

        setTimeout(
            function() {

                identitySection.scrollIntoView({
                    behavior: "smooth",
                    block: "center"
                });

            },
            150
        );


    }

    catch (error) {

        console.error(
            "SCORPIAN ERROR:",
            error
        );


        if (label) {

            label.textContent =
                "TRY AGAIN";

        }


        alert(
            "Unable to generate your Scorpian identity. Please try again."
        );

    }


    /* =====================================================
       RESTORE BUTTON
    ===================================================== */

    button.disabled = false;

    button.classList.remove(
        "running"
    );

}

/* =========================================================
   CARD MOUSE EFFECT
========================================================= */

function enableCardEffects() {

    const cards =
        document.querySelectorAll(
            ".content-card"
        );


    cards.forEach(
        function(card) {

            card.addEventListener(
                "mousemove",
                function(event) {

                    const rect =
                        card.getBoundingClientRect();


                    const x =
                        event.clientX -
                        rect.left;


                    const y =
                        event.clientY -
                        rect.top;


                    const centerX =
                        rect.width / 2;


                    const centerY =
                        rect.height / 2;


                    const rotateX =
                        (y - centerY) / 35;


                    const rotateY =
                        (centerX - x) / 35;


                    card.style.transform =
                        `
                        perspective(700px)
                        rotateX(${rotateX}deg)
                        rotateY(${rotateY}deg)
                        translateY(-5px)
                        `;

                }
            );


            card.addEventListener(
                "mouseleave",
                function() {

                    card.style.transform =
                        "";

                }
            );

        }
    );

}


/* =========================================================
   FORM VALIDATION
========================================================= */

function enableFormValidation() {

    const form =
        document.querySelector(
            "#contentPanel form"
        );


    if (!form) {

        return;

    }


    form.addEventListener(
        "submit",
        function(event) {

            const category =
                document.getElementById(
                    "selectedCategory"
                );


            const subsection =
                document.getElementById(
                    "categorySelect"
                );


            const title =
                document.getElementById(
                    "contentTitle"
                );


            const description =
                document.getElementById(
                    "description"
                );


            if (
                !category ||
                !category.value
            ) {

                event.preventDefault();

                alert(
                    "Please select a category."
                );

                return;

            }


            if (
                !subsection ||
                !subsection.value
            ) {

                event.preventDefault();

                alert(
                    "Please select a sub-section."
                );

                return;

            }


            if (
                !title ||
                !title.value.trim()
            ) {

                event.preventDefault();

                alert(
                    "Please enter a title."
                );

                return;

            }


            if (
                !description ||
                !description.value.trim()
            ) {

                event.preventDefault();

                alert(
                    "Please enter a description."
                );

                return;

            }

        }
    );

}


/* =========================================================
   PHASE 2 — CATEGORY FILTER
========================================================= */

function enableCollectionFilters() {

    const categoryButtons =
        document.querySelectorAll(
            ".filter-button"
        );

    const cards =
        document.querySelectorAll(
            ".collection-card"
        );

    const subsectionContainer =
        document.getElementById(
            "subsectionFilters"
        );


    if (
        !categoryButtons.length ||
        !cards.length ||
        !subsectionContainer
    ) {

        return;

    }


    categoryButtons.forEach(
        function(button) {

            button.addEventListener(
                "click",
                function() {

                    categoryButtons.forEach(
                        function(item) {

                            item.classList.remove(
                                "active"
                            );

                        }
                    );


                    button.classList.add(
                        "active"
                    );


                    const category =
                        button.dataset.filter;


                    filterCollection(
                        category,
                        "all"
                    );


                    showSubsectionFilters(
                        category
                    );

                }
            );

        }
    );


    function filterCollection(
        category,
        subsection
    ) {

        cards.forEach(
            function(card) {

                const cardCategory =
                    card.dataset.category;


                const cardSubsection =
                    card.dataset.subsection;


                const categoryMatch =
                    category === "all"
                    ||
                    cardCategory === category;


                const subsectionMatch =
                    subsection === "all"
                    ||
                    cardSubsection === subsection;


                if (
                    categoryMatch &&
                    subsectionMatch
                ) {

                    card.style.display =
                        "";

                }

                else {

                    card.style.display =
                        "none";

                }

            }
        );

    }


    function showSubsectionFilters(
        category
    ) {

        subsectionContainer.innerHTML =
            "";


        if (
            category === "all"
        ) {

            return;

        }


        const data =
            categoryData[category];


        if (!data) {

            return;

        }


        const allButton =
            document.createElement(
                "button"
            );


        allButton.type =
            "button";


        allButton.className =
            "subsection-button active";


        allButton.textContent =
            "All " +
            category;


        subsectionContainer.appendChild(
            allButton
        );


        allButton.addEventListener(
            "click",
            function() {

                subsectionContainer
                    .querySelectorAll(
                        ".subsection-button"
                    )
                    .forEach(
                        function(button) {

                            button.classList.remove(
                                "active"
                            );

                        }
                    );


                allButton.classList.add(
                    "active"
                );


                filterCollection(
                    category,
                    "all"
                );

            }
        );


        data.sections.forEach(
            function(section) {

                const button =
                    document.createElement(
                        "button"
                    );


                button.type =
                    "button";


                button.className =
                    "subsection-button";


                button.textContent =
                    section;


                subsectionContainer.appendChild(
                    button
                );


                button.addEventListener(
                    "click",
                    function() {

                        subsectionContainer
                            .querySelectorAll(
                                ".subsection-button"
                            )
                            .forEach(
                                function(item) {

                                    item.classList.remove(
                                        "active"
                                    );

                                }
                            );


                        button.classList.add(
                            "active"
                        );


                        filterCollection(
                            category,
                            section
                        );

                    }
                );

            }
        );

    }

}


/* =========================================================
   PHASE 2 — SCORPIAN SEARCH
========================================================= */

function enableScorpianSearch() {

    const searchInput =
        document.getElementById(
            "scorpianSearch"
        );


    const clearButton =
        document.getElementById(
            "clearSearch"
        );


    const resultCount =
        document.getElementById(
            "searchResultCount"
        );


    const cards =
        document.querySelectorAll(
            ".collection-card"
        );


    if (
        !searchInput ||
        !cards.length
    ) {

        return;

    }


    function searchCollection() {

        const searchTerm =
            searchInput.value
                .trim()
                .toLowerCase();


        let visibleCount =
            0;


        cards.forEach(
            function(card) {

                const title =
                    (
                        card.dataset.title
                        || ""
                    ).toLowerCase();


                const description =
                    (
                        card.dataset.description
                        || ""
                    ).toLowerCase();


                const category =
                    (
                        card.dataset.category
                        || ""
                    ).toLowerCase();


                const subsection =
                    (
                        card.dataset.subsection
                        || ""
                    ).toLowerCase();


                const language =
                    (
                        card.dataset.language
                        || ""
                    ).toLowerCase();


                const searchableText =
                    title
                    + " "
                    + description
                    + " "
                    + category
                    + " "
                    + subsection
                    + " "
                    + language;


                if (
                    !searchTerm
                    ||
                    searchableText.includes(
                        searchTerm
                    )
                ) {

                    card.style.display =
                        "";

                    visibleCount++;

                }

                else {

                    card.style.display =
                        "none";

                }

            }
        );


        updateSearchCount(
            searchTerm,
            visibleCount
        );

    }


    function updateSearchCount(
        searchTerm,
        count
    ) {

        if (!resultCount) {

            return;

        }


        if (!searchTerm) {

            resultCount.textContent =
                "";

            return;

        }


        if (count === 0) {

            resultCount.textContent =
                "No Scorpian entries found.";

        }

        else if (count === 1) {

            resultCount.textContent =
                "1 entry found.";

        }

        else {

            resultCount.textContent =
                count +
                " entries found.";

        }

    }


    searchInput.addEventListener(
        "input",
        searchCollection
    );


    if (clearButton) {

        clearButton.addEventListener(
            "click",
            function() {

                searchInput.value =
                    "";

                searchCollection();

                searchInput.focus();

            }
        );

    }

}


/* =========================================================
   COLLECTION SEARCH + FILTER + SORT
========================================================= */

function enableCollectionSearch() {

    const searchInput =
        document.getElementById(
            "collectionSearch"
        );


    const categoryFilter =
        document.getElementById(
            "categoryFilter"
        );


    const subsectionFilter =
        document.getElementById(
            "subsectionFilter"
        );


    const sortCollection =
        document.getElementById(
            "sortCollection"
        );


    const collectionGrid =
        document.querySelector(
            ".collection-grid"
        );


    const noResults =
        document.getElementById(
            "noSearchResults"
        );


    if (!collectionGrid) {

        return;

    }


    function updateSubsectionOptions() {

        if (!subsectionFilter) {

            return;

        }


        const selectedCategory =
            categoryFilter
                ? categoryFilter.value
                : "all";


        const cards =
            Array.from(
                collectionGrid.querySelectorAll(
                    ".collection-card"
                )
            );


        const subsections =
            new Set();


        cards.forEach(
            function(card) {

                const category =
                    (
                        card.dataset.category
                        || ""
                    ).toLowerCase();


                const subsection =
                    card.dataset.subsection
                    || "";


                if (
                    selectedCategory === "all"
                    ||
                    category === selectedCategory
                ) {

                    if (subsection) {

                        subsections.add(
                            subsection
                        );

                    }

                }

            }
        );


        subsectionFilter.innerHTML =
            "";


        const allOption =
            document.createElement(
                "option"
            );


        allOption.value =
            "all";


        allOption.textContent =
            "All Subsections";


        subsectionFilter.appendChild(
            allOption
        );


        Array.from(subsections)
            .sort()
            .forEach(
                function(subsection) {

                    const option =
                        document.createElement(
                            "option"
                        );


                    option.value =
                        subsection;


                    option.textContent =
                        subsection;


                    subsectionFilter.appendChild(
                        option
                    );

                }
            );

    }


    function updateCollection() {

        const searchText =
            searchInput
                ? searchInput.value
                    .toLowerCase()
                    .trim()
                : "";


        const selectedCategory =
            categoryFilter
                ? categoryFilter.value
                : "all";


        const selectedSubsection =
            subsectionFilter
                ? subsectionFilter.value
                : "all";


        const sortType =
            sortCollection
                ? sortCollection.value
                : "newest";


        const cards =
            Array.from(
                collectionGrid.querySelectorAll(
                    ".collection-card"
                )
            );


        let visibleCards =
            0;


        /* =================================================
           FILTER
        ================================================= */

        cards.forEach(
            function(card) {

                const searchableText =
                    (
                        card.dataset.search
                        || ""
                    ).toLowerCase();


                const cardCategory =
                    (
                        card.dataset.category
                        || ""
                    ).toLowerCase();


                const cardSubsection =
                    (
                        card.dataset.subsection
                        || ""
                    ).toLowerCase();


                const matchesSearch =
                    searchableText.includes(
                        searchText
                    );


                const matchesCategory =
                    selectedCategory === "all"
                    ||
                    cardCategory ===
                    selectedCategory;


                const matchesSubsection =
                    selectedSubsection === "all"
                    ||
                    cardSubsection ===
                    selectedSubsection;


                if (
                    matchesSearch &&
                    matchesCategory &&
                    matchesSubsection
                ) {

                    card.style.display =
                        "";

                    visibleCards++;

                }

                else {

                    card.style.display =
                        "none";

                }

            }
        );


        /* =================================================
           SORT
        ================================================= */

        cards.sort(
            function(a, b) {

                if (
                    sortType === "title"
                ) {

                    return (
                        a.dataset.title
                        || ""
                    ).localeCompare(
                        b.dataset.title
                        || ""
                    );

                }


                const dateA =
                    new Date(
                        a.dataset.date || 0
                    );


                const dateB =
                    new Date(
                        b.dataset.date || 0
                    );


                if (
                    sortType === "oldest"
                ) {

                    return dateA - dateB;

                }


                return dateB - dateA;

            }
        );


        cards.forEach(
            function(card) {

                collectionGrid.appendChild(
                    card
                );

            }
        );


        /* =================================================
           NO RESULTS
        ================================================= */

        if (noResults) {

            if (
                visibleCards === 0
            ) {

                noResults.style.display =
                    "block";

            }

            else {

                noResults.style.display =
                    "none";

            }

        }

    }


    if (searchInput) {

        searchInput.addEventListener(
            "input",
            updateCollection
        );

    }


    if (categoryFilter) {

        categoryFilter.addEventListener(
            "change",
            function() {

                updateSubsectionOptions();

                updateCollection();

            }
        );

    }


    if (subsectionFilter) {

        subsectionFilter.addEventListener(
            "change",
            updateCollection
        );

    }


    if (sortCollection) {

        sortCollection.addEventListener(
            "change",
            updateCollection
        );

    }


    updateSubsectionOptions();

    updateCollection();

}


/* =========================================================
   COLLECTION VIEW
========================================================= */

function showCollectionView(view) {

    const grid =
        document.querySelector(
            ".collection-grid"
        );


    const timeline =
        document.getElementById(
            "collectionTimeline"
        );


    const buttons =
        document.querySelectorAll(
            ".view-button"
        );


    if (
        !grid ||
        !timeline
    ) {

        return;

    }


    buttons.forEach(
        function(button) {

            button.classList.remove(
                "active"
            );

        }
    );


    if (
        view === "timeline"
    ) {

        grid.style.display =
            "none";


        timeline.style.display =
            "block";


        if (buttons[1]) {

            buttons[1].classList.add(
                "active"
            );

        }

    }

    else {

        grid.style.display =
            "";


        timeline.style.display =
            "none";


        if (buttons[0]) {

            buttons[0].classList.add(
                "active"
            );

        }

    }

}


/* =========================================================
   PAGE LOAD
========================================================= */

document.addEventListener(
    "DOMContentLoaded",
    function() {

        enableCardEffects();

        enableFormValidation();

        enableCollectionSearch();

        console.log(
            "🦂 Scorpian JavaScript loaded successfully."
        );

    }
);


/* =========================================================
   ESCAPE KEY
========================================================= */

document.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key !== "Escape"
        ) {

            return;

        }


        const panel =
            document.getElementById(
                "contentPanel"
            );


        if (
            panel &&
            panel.classList.contains("active")
        ) {

            closeCategory();

        }

    }
);