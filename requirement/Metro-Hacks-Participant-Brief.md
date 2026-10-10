# Metro Hacks - Participant Brief

## Hackathon context

Two-hour hackathon on board the Gujarat Metro. Teams select one problem and build a working prototype before the ride ends. Network coverage may drop, especially underground. Bring datasets, libraries, documentation, maps, and offline AI models in advance.

## Judging criteria

- Relevance to the stated operator or city problem
- Working end-to-end prototype
- Resilience with poor or no network
- Meaningful technical depth and AI usage
- Feasibility, impact, and a realistic public-private partnership model

## Problem statements

| ID | Title | Track | Offline |
|---|---|---|---|
| PS-01 | Winning Back the Empty Seats | Metro Operations | Not required |
| PS-02 | Fix It Before It Breaks | Metro Operations | Not required |
| PS-03 | The Technician in the Tunnel | Metro Operations | Required |
| PS-04 | No Day Is an Average Day | Metro Operations | Not required |
| PS-05 | The Stadium Surge | Metro Operations | Not required |
| PS-06 | Footfall to Revenue | Metro Operations | Not required |
| PS-07 | Every Complaint Heard | Metro Operations | Required |
| PS-08 | One City, One Journey | City Public Transport | Not required |
| PS-09 | Clear the Exit | City Public Transport | Required |
| PS-10 | Diversions Without Disruption | City Public Transport | Not required |
| PS-11 | Beat the Heat | City Public Transport | Not required |
| PS-12 | Monsoon Mode | City Public Transport | Not required |
| PS-13 | The Two-Minute Morning Brief | City Public Transport | Not required |

## Selected project: PS-07

Build an offline tool that accepts Gujarati, Hindi, English, and mixed Gujlish complaints; routes them to Safety, Cleanliness, Fare, Lifts/Escalators, or Staff Behaviour; assigns urgency; drafts a reply in the complainant's language; stores cases locally; and syncs when connectivity returns.

## MetroSuno security provisions

- Passenger self-registration and login for raising and tracking complaints.
- Emergency passenger login for rapid safety reporting during incidents.
- Operator login for triage and status updates.
- Admin/site-manager login for the demo; operator accounts are admin-managed and cannot self-register.
- Local-first storage so reports are not lost offline.
- Spam protection for duplicates, links, repeated characters, and empty/too-short reports.
- Human review remains available for blocked reports; filters do not silently delete submissions.

## Judge demo credentials

| Role | Login | Password |
|---|---|---|
| Passenger | `judge@example.com` | `pass1234` |
| Metro operator | `operator` | `metro123` |
| Admin / site manager | `admin` | `admin123` |

Run the app with `python3 server.py` from the `metrosuno` directory and open `http://127.0.0.1:8000/`.
