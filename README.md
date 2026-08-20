# Cloud & DevOps Portfolio

A personal portfolio website for Dawid Bronikowski, built as a modern cloud and DevOps-focused landing page. The project showcases skills, certifications, and professional growth across AWS, Azure, and Google Cloud Platform, while demonstrating a strong interest in automation, infrastructure as code, and CI/CD.

## Overview

This project is a front-end portfolio designed to present a cloud engineering profile with a long-term multi-cloud focus. While AWS is currently a major part of the site, the project is intended to evolve over time to reflect broader learning and hands-on experience in Azure and Google Cloud Platform.

The site is built with plain HTML and CSS, making it lightweight, fast, and easy to host on static cloud infrastructure.

## Features

- Responsive single-page portfolio layout
- About section explaining the cloud and DevOps journey
- Skills section covering AWS, Azure, Google Cloud, DevOps, programming, and operating systems
- Projects area highlighting cloud-focused work and portfolio pieces
- Contact section with email link
- Static site design suitable for hosting on cloud providers such as AWS S3, Azure Static Web Apps, or Google Cloud storage
- Local utilities for validation and site maintenance

## Tech Stack

- HTML5
- CSS3
- Python 3
- BeautifulSoup 4
- Ruff (linting and formatting checks)
- Multi-cloud learning and portfolio focus:
  - AWS
  - Azure
  - Google Cloud Platform

## Project Structure

- `index.html` – main portfolio page
- `css/styles.css` – styling and layout
- `images/` – image assets
- `scripts/check.bat` – Windows validation script for linting and formatting
- `scripts/update_last_update.py` – updates the footer date in the HTML
- `README.md` – project documentation
- `LICENSE` – project license information

## Local Development

To view the site locally:

1. Clone the repository.
2. Open `index.html` directly in a browser, or serve the project with a local web server.
3. From the project root, run:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

## Validation Script

A helper script is included for local quality checks:

```bat
scripts\check.bat
```

This script runs Ruff linting and formatting checks and pauses at the end so the result can be reviewed.

## Updating the Footer Date

The footer date can be refreshed with:

```bash
python scripts/update_last_update.py
```

This script updates the `lastupdate-time` field in the page using BeautifulSoup.

## Deployment

This site is designed as a static website and is suitable for deployment on cloud hosting platforms. While AWS is the current foundation, the project is planned to grow alongside Azure and Google Cloud workflows.

Typical deployment options include:

1. AWS S3 static website hosting
2. Azure Static Web Apps
3. Google Cloud storage hosting
4. Optional CDN or custom domain integration

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For inquiries or collaboration:

- Email: dawid.bronikowski@outlook.com
- GitHub: https://github.com/Dron3xx

## Notes

This repository is a personal portfolio and learning project focused on cloud engineering, automation, and DevOps. It currently highlights AWS while intentionally leaving room to expand into Azure and Google Cloud over time as the profile and experience grow.
