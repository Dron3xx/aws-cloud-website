# Portfolio project explanation

This file explains how the portfolio website is structured, how its interactive project section works, and how the local maintenance and validation tools fit together.

## 1) Main HTML document

The website is defined in `index.html` and uses standard HTML5 elements:

- `header` contains the page title.
- `main` contains the About, skills, certifications, and projects sections.
- `footer` contains the contact link and last-updated metadata.

The page is a static document. It does not require a backend, database, build step, or JavaScript framework.

### Responsive metadata

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

What this does:

- sets the document character encoding to UTF-8
- makes the layout use the device width on phones and tablets

Why this matters:

- prevents text and symbols from being decoded incorrectly
- allows the responsive CSS rules to work on smaller screens

## 2) About section

The `about` section introduces the portfolio owner and links to the public GitHub profile.

```html
<section id="about" class="home">
    <p><a href="https://github.com/Dron3xx" target="_blank" class="btn">View my GitHub</a></p>
    <p>I'm an aspiring Cloud & DevOps Engineer with a passion for AWS, automation, IaC and continuous integration.</p>
</section>
```

What this does:

- provides a short professional introduction
- gives visitors a direct link to the GitHub profile
- identifies the section for navigation and styling with `id="about"` and `class="home"`

## 3) Skills and certifications

The `skiedu` section places technical skills beside education and certifications.

The skills are grouped into four categories:

- Cloud: AWS, Azure, and Google Cloud Platform
- DevOps: Docker, GitHub Actions, and Terraform
- Programming: Python and Bash
- Operating systems: Linux and Windows

The page uses Devicon classes for technology icons. The Devicon stylesheet is loaded from jsDelivr in the document head, so the icons are supplied by the external CDN rather than stored in this repository.

The certifications panel links to the Credly profile for the AWS Educate badges.

## 4) Project list

Projects are represented as list items inside the `projects` section.

Each project item contains:

- a project name
- a short description
- a list of technologies
- a status
- a link to the corresponding GitHub repository

The current projects are the AWS portfolio website, Stiukov, and the Terraform project. Adding a project normally means adding another `li.project-item` with the same internal structure.

## 5) Project carousel

The project list is made scrollable by `js/projectscroll.js`.

```javascript
const left = document.getElementById("arrow-left");
const right = document.getElementById("arrow-right");
const projectMove = document.getElementById("project-move");
```

What this does:

- finds the two navigation controls
- finds the project carousel container
- finds the project `ul` inside that container

The script exits safely with a warning if one of the expected elements is missing. This keeps the rest of the page usable when the carousel markup is incomplete.

### Moving between projects

The script measures the first project item, including its margins, to calculate one scroll step. Clicking the left or right control changes the current project index and scrolls the list by that step.

The carousel also:

- clamps the index so it cannot move before the first or after the last project
- updates arrow visibility at the beginning and end of the list
- centers the list when all projects fit without scrolling
- recalculates its position after the browser is resized
- responds to manual scrolling by updating the controls

This keeps the controls synchronized with both button navigation and direct touch or mouse scrolling.

## 6) Styling and layout

The visual design is stored in `css/styles.css` and is loaded by the HTML document.

The stylesheet controls:

- page typography, colors, spacing, and borders
- the responsive layout for the skills and education panels
- project item dimensions and horizontal scrolling
- the appearance and positioning of the carousel arrows
- mobile layout changes

The stylesheet is versioned in the link URL with `?v=3`. Changing this value can help browsers fetch a new stylesheet after a deployment when an older cached copy is still being used.

## 7) Footer metadata update

The footer includes a `time` element with the `lastupdate-time` id:

```html
<time id="lastupdate-time" datetime="2026-08-03">
    03/08/2026
</time>
```

`scripts/update_last_update.py` updates both values using the current UTC date.

What the script does:

- reads `index.html` relative to the script location
- parses the document with BeautifulSoup
- finds the `time` element by id
- updates its ISO `datetime` attribute and displayed date
- writes the parsed HTML back to `index.html`

Run it from the project root with:

```bash
python scripts/update_last_update.py
```

The script logs a warning instead of changing the file when the expected element is not present.

## 8) Validation tools

`scripts/check.bat` is the Windows validation helper.

It runs:

- Ruff linting and formatting checks for Python files
- Biome checks for the JavaScript directory

The batch file stops when a check fails and returns a non-zero exit code. This makes it suitable for running locally before committing changes.

The JavaScript dependency is declared in `package.json`:

```json
{
  "devDependencies": {
    "@biomejs/biome": "2.5.10"
  }
}
```

Install the Node dependency before running the Biome check:

```bash
npm install
```

## 9) Local development

Because the site is static, it can be opened directly in a browser. A local HTTP server is useful when testing it in an environment that restricts local file access:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## 10) Deployment model

The project produces no server-side output. The deployable content is the repository's static HTML, CSS, JavaScript, and image files.

The site can therefore be hosted by:

- an AWS S3 bucket configured for static website hosting
- Azure Static Web Apps
- Google Cloud Storage
- another static hosting provider or CDN

The public entry point is `index.html`, and all referenced assets must remain available at their relative paths after deployment.

## 11) Overall result

The final site presents a cloud and DevOps portfolio as a lightweight responsive page:

- visitors read the introduction and skills
- visitors review projects and open their repositories
- the project list can be browsed with arrows or direct scrolling
- the footer provides contact information and update metadata
- local scripts support repeatable date updates and quality checks
