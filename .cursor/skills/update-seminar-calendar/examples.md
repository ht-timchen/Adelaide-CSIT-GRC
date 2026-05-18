# Example: pasted email → YAML

## Input (user paste)

```
Dear All,

We have one Confirmation of Candidature Review below. You are welcome to attend.

Candidate: Ziyang Ye
Date: Wed 13/05/2026 10:00 AM - 11:00 AM
Supervisor: Prof Olaf Maennel
Title:Towards Secure and Robust Visual Intelligence: ...
Abstract: Vision Foundation Models are increasingly...

Meeting Link:https://teams.microsoft.com/meet/43679131191974?p=...
```

## Classification

- "Confirmation of Candidature Review" → `type: initial_review`
- Teams link → `teams_url`

## Output entry

```yaml
  - id: initial-review-2026-05-13-ye
    type: initial_review
    candidate: "Ziyang Ye"
    supervisor: "Prof Olaf Maennel"
    date: 2026-05-13
    time: "10:00–11:00"
    title: "Towards Secure and Robust Visual Intelligence: Adversarial Robustness in Vision Foundation Models"
    abstract: |
      Vision Foundation Models are increasingly becoming the backbone...
    teams_url: "https://teams.microsoft.com/meet/43679131191974?p=VNm7XZhoNDkqJ8DnhW"
    status: scheduled
```

## Agent notes

- `13/05/2026` is 13 May 2026 (DD/MM/YYYY), not 5 December.
- Family name `ye` used in `id` slug.
- If today is after 2026-05-13, tell the user the listing will appear under **Past seminars**.
