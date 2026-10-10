# MetroSuno

Offline-first multilingual complaint triage prototype for GDG Metro Hacks PS-07.

## Run locally

```bash
cd metrosuno
python3 server.py
```

Open http://127.0.0.1:8000 in a browser.

## Demo script

1. Show the seeded multilingual inbox and department queues.
2. Click **New complaint** and use the Gujlish example.
3. Click **Analyze & route complaint** to show local classification.
4. Save it to the offline queue; the counter increases immediately.
5. Click **Sync queue** to simulate connectivity returning.
6. Refresh the page to show that complaints persist in local storage.

The core triage runs in the browser with no API calls. A service worker caches the interface for repeat offline use; localStorage stores the complaint queue.
