# To Do List

A simple task list built with Vue 3 + Bootstrap-Vue. Add, edit, complete, and delete tasks.

**Live:** https://iamsorenl.github.io/ToDoList/

## Storage

The live site persists tasks in the browser's `localStorage`, so your list is
scoped to the device/browser you're using — no login, no server, no sync.

A Flask backend (`backend/main.py`) is kept in the repo as the original reference
implementation for local dev. It stores tasks in an in-memory list and has the
same CRUD semantics as the localStorage version. It is **not** used by the
deployed site.

## Run locally

### Frontend only (matches the live site)

```bash
cd frontend/frontend
npm install
npm run serve
# → http://localhost:8080
```

### With the Flask backend

The Flask version is not wired to the current frontend; restore the axios calls
in `src/components/ToDoList.vue` (see git history for the original) if you want
to run against it.

```bash
cd backend
pip install -r requirements.txt
python main.py
# → http://localhost:5000
```

## Deploy

On every push to `main`, `.github/workflows/deploy.yml` runs
`npm run build` inside `frontend/frontend/` and publishes `dist/` to GitHub
Pages. `publicPath` in `vue.config.js` is set to `/ToDoList/` for production
so asset URLs resolve under the repo subpath, and a `404.html` copy of
`index.html` is generated so deep links (e.g. `/ToDoList/shark`) don't break.

## Contact

- Email: iamsorenl@gmail.com
- LinkedIn: https://www.linkedin.com/in/soren-larsen-46a57118b/
