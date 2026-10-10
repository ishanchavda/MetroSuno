# PS-07 - Every Complaint Heard

## Problem

Passenger complaints arrive through multiple channels and languages, and urgent complaints can get buried. Complaints may be written in Gujarati, Hindi, English, or mixed Gujlish. Station controllers may need to triage them without network access.

## Required outcome

Build an offline-capable tool that:

- Accepts multilingual passenger complaints.
- Classifies each complaint into Safety, Cleanliness, Fare/Ticketing, Lifts/Escalators, or Staff Behaviour.
- Assigns an urgency level.
- Routes complaints to department queues.
- Drafts a reply in the complainant's language.
- Stores complaints locally when offline.
- Synchronizes when connectivity returns.

## MetroSuno implementation

- Passenger login and self-registration.
- Emergency passenger login for rapid safety reports.
- Metro staff login for triage and status updates.
- Admin/site-manager login for admin-managed staff access.
- Passenger status tracking: Received, In progress, and Resolved.
- Spam controls for duplicate complaints, links, repeated characters, and very short submissions.
- SQLite-backed web API with browser offline fallback.

## Acceptance demo

1. Passenger logs in and submits a multilingual complaint.
2. The complaint receives a reference number and starts as `Received`.
3. Operator logs in and sees the complaint in the correct department queue.
4. Operator changes the status to `In progress` and then `Resolved`.
5. Passenger can see the updated status.
6. Emergency passenger login can submit a safety report.
7. The app remains usable when the network is unavailable and syncs later.

## Judge credentials

| Role | Login | Password |
|---|---|---|
| Passenger | `judge@example.com` | `pass1234` |
| Metro operator | `operator` | `metro123` |
| Admin / site manager | `admin` | `admin123` |
