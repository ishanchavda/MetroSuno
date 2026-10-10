# MetroSuno

MetroSuno is an offline-first prototype for GDG Metro Hackathon problem PS-07, **Every Complaint Heard**.

## Current working version (v5)

The app supports passenger, emergency passenger, metro operator, and admin/site-manager journeys. The clean local URL is `http://127.0.0.1:8000/`; no query-string version is required.

## Demo credentials

Use these credentials during judging:

| Role | Login | Password | Access |
|---|---|---|---|
| Passenger | `judge@example.com` | `pass1234` | Submit and track complaints |
| Metro operator | `operator` | `metro123` | Triage complaints and update statuses |
| Admin / site manager | `admin` | `admin123` | Demo staff-management login; operator accounts are admin-managed |

Passenger registration is available on the login screen. Passengers can create their own account. Operators do not self-register; in the production design, the admin/site manager provisions operator accounts.

### Passenger

- Passenger login
- Emergency passenger login for rapid safety reporting
- Complaint submission in English, Hindi, Gujarati, or Gujlish
- Local spam protection for duplicates, links, repeated characters, and very short reports
- Complaint reference number
- Status tracking: Received, In progress, and Resolved

### Metro operator

- Operator ID and PIN login
- Multilingual complaint inbox
- Department routing and urgency scoring
- Department queues for Safety, Cleanliness, Fare/Ticketing, Lifts/Escalators, and Staff Behaviour
- Status updates that passengers can see in the prototype
- Offline queue and simulated synchronization

## Run locally

```bash
cd metrosuno
python3 server.py
```

Open http://127.0.0.1:8000/.

For a clean login demonstration, use a private browser window or run this in the browser console:

```js
localStorage.removeItem('metrosuno-session')
location.reload()
```

## Demo sequence

1. Choose Passenger login and submit a complaint.
2. Note the complaint reference number and Received status.
3. Log out and choose Operator login.
4. Find the complaint in the operator inbox.
5. Change its status to In progress or Resolved.
6. Log out and return to the passenger view to show the updated status.
7. Use Emergency passenger login to demonstrate rapid safety reporting.

## Offline design

The web app runs from the Python server and persists shared complaints and demo users in `metrosuno.sqlite3` through local REST endpoints. The browser still keeps an offline-friendly local queue and the service worker caches the interface. The login and role separation are hackathon controls; production deployment should add HTTPS, hashed passwords, backend sessions, role-based access control, audit logging, rate limiting, and encrypted backups.
