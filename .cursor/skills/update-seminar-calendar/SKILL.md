---
name: update-seminar-calendar
description: >-
  Add or update CSIT HDR seminar listings on the GitHub Pages calendar from
  pasted email announcements. Use when the user pastes a seminar/thesis/review
  announcement, asks to update the website or calendar, mentions Confirmation of
  Candidature, candidature review, CoC review, thesis defence, HDR seminar, or _data/seminars.yml
  in Adelaide-CSIT-GRC.
---

# Update seminar calendar

Publish student-facing seminar listings by editing **only** [`_data/seminars.yml`](../../_data/seminars.yml). Do not change `_layouts/`, `_includes/`, or CSS unless the user asks to change site design.

Full field reference: [`AGENTS.md`](../../AGENTS.md). Live site: <https://ht-timchen.github.io/Adelaide-CSIT-GRC/>

## Workflow

1. **Classify** the announcement → pick `type` (see table below).
2. **Extract** fields from the pasted text (see parsing rules).
3. **Edit** `_data/seminars.yml`: add a new list item or update an existing one by `id`.
4. **Keep** entries sorted by `date` ascending (earliest first).
5. **Validate**: `python3 scripts/validate_seminars.py` (use repo `.venv` if present: `.venv/bin/python scripts/validate_seminars.py`).
6. **Tell the user** whether the event is upcoming or past (compare `date` to today, Adelaide), and that they must **commit and push to `main`** for the public site to update.

Do not commit unless the user asks.

## Announcement type → YAML `type`

| Phrases in email / notice | `type` value |
|---------------------------|--------------|
| Confirmation of Candidature, CoC review, candidature review | `candidature_review` |
| Thesis defence, thesis defense, public seminar (thesis) | `thesis_defence` |
| HDR seminar, seminar series, student presentation (series) | `hdr_seminar` |
| Panel, workshop, special session, invited talk (series) | `special` |

When unsure between `candidature_review` and `thesis_defence`, prefer **`candidature_review`** for CoC / confirmation wording.

## Parsing pasted announcements

### Thesis-format (`candidature_review`, `thesis_defence`)

Look for these labels (case-insensitive, colon optional):

| Email label | YAML field |
|-------------|------------|
| Candidate | `candidate` |
| Supervisor | `supervisor` |
| Title | `title` |
| Abstract | `abstract` (multi-line; use `\|` block scalar) |
| Date, Date and Time | `date` + `time` (see dates below) |
| Microsoft Teams, Teams meeting, Meeting Link (teams.microsoft.com) | `teams_url` |
| Zoom (zoom.us) | `zoom_url` |
| Location, Room, Venue | `location` (optional) |

**Required:** one of `teams_url` or `zoom_url` for thesis-format entries.

**`id`:** `{type}-{yyyy-mm-dd}-{familyname}` lowercase, e.g. `candidature-review-2026-05-13-ye`.

### Event-format (`hdr_seminar`, `special`)

| Email label | YAML field |
|-------------|------------|
| Speaker, Presenter | `speaker` |
| Title | `title` |
| Date / time | `date`, `time` |
| Location, Room | `location` |
| Abstract, Description | `abstract` |
| Link, Join online | `online_url` |

## Date and time rules

- Australian emails often use **DD/MM/YYYY** (e.g. `Wed 13/05/2026`) → store `date: 2026-05-13` (ISO).
- Ranges like `10:00 AM - 11:00 AM` → `time: "10:00–11:00"` (en dash) or start time only `"10:00"`.
- Times are **Adelaide local**; no timezone conversion in YAML.
- After adding, note if `date` is before today → event appears under **Past seminars** on the site.

## YAML templates

### Candidature review / CoC (from email)

```yaml
  - id: candidature-review-2026-05-13-ye
    type: candidature_review
    candidate: "Ziyang Ye"
    supervisor: "Prof Olaf Maennel"
    date: 2026-05-13
    time: "10:00–11:00"
    title: "Full title here"
    abstract: |
      First paragraph...

      Second paragraph...
    teams_url: "https://teams.microsoft.com/meet/..."
    status: scheduled
```

### Thesis defence

```yaml
  - id: thesis-defence-2026-08-01-smith
    type: thesis_defence
    candidate: "Jane Smith"
    supervisor: "Prof. Wei Zhang"
    date: 2026-08-01
    time: "14:00"
    title: "Thesis title"
    abstract: |
      Abstract text.
    teams_url: "https://teams.microsoft.com/..."
    status: scheduled
```

### HDR seminar

```yaml
  - id: hdr-2026-06-03-taylor
    type: hdr_seminar
    title: "Talk title"
    speaker: "Sam Taylor"
    date: 2026-06-03
    time: "14:00"
    location: "Ingkarni Wardli, Level 4"
    abstract: |
      Brief description.
    status: scheduled
```

## Update vs cancel vs complete

| User intent | Action |
|-------------|--------|
| New announcement | Add new item with unique `id` |
| Wrong details | Edit same `id` in place |
| Cancelled | Set `status: cancelled` (keep entry until date passes) |
| Mistaken listing | Remove the YAML block entirely |
| Already happened | `status: completed` optional; past dates auto-archive on the site |

## Validation errors

- Thesis type missing `teams_url`/`zoom_url` → add the meeting link from the email.
- Duplicate `id` → change slug or merge into existing entry.
- Run `scripts/validate_seminars.py` after every edit.

## Example

See [examples.md](examples.md) for a full pasted email → YAML mapping (Ziyang Ye CoC review).
