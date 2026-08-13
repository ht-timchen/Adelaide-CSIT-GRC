# Agent guide: seminar calendar

This repository publishes a seminar calendar via **GitHub Pages**. To add or update public seminar listings, **only edit** [`_data/seminars.yml`](_data/seminars.yml). Do not edit HTML layouts, CSS, or generated pages unless explicitly asked to change the site design.

Live site (after deployment): <https://ht-timchen.github.io/Adelaide-CSIT-GRC/>

## Quick workflow (pasted announcement)

When the user pastes an email notice and asks to update the website:

1. Read the project skill: [`.cursor/skills/update-seminar-calendar/SKILL.md`](.cursor/skills/update-seminar-calendar/SKILL.md) (parsing rules, type mapping, examples).
2. Map **Confirmation of Candidature** / CoC review → `candidature_review`; thesis defence → `thesis_defence`; GRS series talk → `hdr_seminar`.
3. Parse **DD/MM/YYYY** dates as Australian format → ISO `YYYY-MM-DD` in YAML.
4. Add or update one item in `_data/seminars.yml`; run `python3 scripts/validate_seminars.py`.
5. Remind the user to push to `main` for GitHub Pages to rebuild (do not commit unless asked).

## Seminar types

| `type` value       | Use for                                      | Format        |
|--------------------|----------------------------------------------|---------------|
| `candidature_review` | Candidature review                         | Thesis block  |
| `thesis_defence`   | Thesis defence (public seminar)              | Thesis block  |
| `hdr_seminar`      | Regular GRS series presentation              | Event card    |
| `special`          | Special sessions (panels, workshops, etc.)   | Event card    |

## Common fields (all types)

| Field    | Required | Notes |
|----------|----------|-------|
| `id`     | Yes      | Unique slug: `{type}-{yyyy-mm-dd}-{short-name}` (lowercase, hyphens) |
| `type`   | Yes      | One of the values in the table above |
| `date`   | Yes      | ISO date `YYYY-MM-DD` |
| `time`   | Yes      | 24-hour local Adelaide time, e.g. `"14:00"` |
| `title`  | Yes      | Talk or event title |
| `status` | Yes      | `scheduled`, `cancelled`, or `completed` |
| `image`  | No       | Optional banner: site path under `assets/seminars/`, e.g. `"/assets/seminars/special-2026-06-16-ml-universe.jpg"` |
| `image_alt` | No    | Alt text for the image (defaults to `title` if omitted) |

Keep entries sorted by `date` ascending.

### Optional banner image

1. Save the image file in [`assets/seminars/`](assets/seminars/) (JPEG, PNG, or WebP; use the seminar `id` as the filename when possible).
2. Add `image: "/assets/seminars/{filename}"` to the seminar entry in `_data/seminars.yml`.
3. Optionally set `image_alt` for accessibility.

The image appears on the event card (home, seminars, GRS series, and past pages). Omit `image` for text-only listings.

## Thesis announcement format

Use for `candidature_review` and `thesis_defence`. Fields match the standard email notice:

| YAML field     | Display label              | Required |
|----------------|----------------------------|----------|
| `candidate`    | **Candidate:**             | Yes      |
| `supervisor`   | **Supervisor:**            | Yes      |
| `title`        | **Title:**                 | Yes      |
| `abstract`     | **Abstract:**              | Yes (use `\|` for multi-line) |
| `teams_url`    | **Microsoft Teams meeting:** | Provide **either** `teams_url` **or** `zoom_url` |
| `zoom_url`     | **Zoom:**                  | Provide **either** `teams_url` **or** `zoom_url` |
| `location`     | **Location:**              | Optional (in-person detail) |

`date` and `time` are combined on the page as **Date and Time:**.

### Template: thesis defence

```yaml
  - id: thesis-defence-2026-08-01-familyname
    type: thesis_defence
    candidate: "Full Name"
    supervisor: "Prof. Supervisor Name"
    date: 2026-08-01
    time: "14:00"
    title: "Thesis title here"
    abstract: |
      Abstract text. Multiple paragraphs are fine.
    teams_url: "https://teams.microsoft.com/l/meetup-join/..."
    status: scheduled
```

### Template: candidature review

```yaml
  - id: candidature-review-2026-07-15-familyname
    type: candidature_review
    candidate: "Full Name"
    supervisor: "Dr. Supervisor Name"
    date: 2026-07-15
    time: "10:30"
    title: "Proposed research program title"
    abstract: |
      Summary of the proposed research and milestones.
    zoom_url: "https://uniadelaide.zoom.us/j/..."
    status: scheduled
```

## GRS and special session format

| YAML field   | Required | Notes |
|--------------|----------|-------|
| `speaker`    | Yes      | Presenter name(s) |
| `location`   | Yes      | Room or `"Online"` |
| `abstract`   | Recommended | Multi-line talk description |
| `bio`        | Optional | Speaker biography (shown under **Bio:**) |
| `online_url` | Optional | Generic join link |

### GRS Series (program table)

Sessions that belong to the fortnightly **GRS Series** should include:

- `series: hdr-2026` — groups rows on the [GRS series](/grs-series) page
- `session_number: 1` — week/session number (e.g. 1–16)
- `ideas: "..."` — short coordinator notes shown in the program table

Student presentation weeks may have **one or two** talks. Give each speaker their own YAML entry with the **same** `date`, `time`, `location`, and `session_number`; the program table merges them into one week row, while session details still show separate cards.

One-off GRS talks (not part of the series) omit `series` and appear on the main Seminars page.

### Template: GRS seminar

```yaml
  - id: hdr-2026-07-20-familyname
    type: hdr_seminar
    title: "Talk title"
    speaker: "Student Name"
    date: 2026-07-20
    time: "14:00"
    location: "Ingkarni Wardli, Level 4 seminar room"
    abstract: |
      Brief description of the talk.
    bio: |
      Short speaker biography.
    status: scheduled
```

### Template: special session

```yaml
  - id: special-2026-09-05-panel-title
    type: special
    title: "Session title"
    speaker: "Panel / organiser name"
    date: 2026-09-05
    time: "14:00"
    location: "Ingkarni Wardli, Level 4"
    abstract: |
      What the session covers.
    status: scheduled
```

## Workflows

### Add a new seminar

1. Open `_data/seminars.yml`.
2. Add a new list item under `seminars:` using the correct template.
3. Ensure `id` is unique and `date`/`time` are correct (Adelaide local).
4. Run validation: `python3 scripts/validate_seminars.py` (if available locally).

### Cancel a seminar

Set `status: cancelled` and keep the entry until the date has passed. Do not delete unless the listing was added in error.

### After a seminar has occurred

Set `status: completed` or leave as `scheduled`; entries with `date` before today automatically appear in the **Past seminars** section.

### Remove a mistaken entry

Delete the entire YAML block for that `id`.

## Do not edit

- `_layouts/`, `_includes/`, `assets/css/` — site chrome (unless changing design)
- `Seminar/*.xlsx` — internal planning only; not the public calendar
- `Doc/` — handbook PDFs

## Validation

CI runs `scripts/validate_seminars.py` on push. Fix any reported errors before merging.
