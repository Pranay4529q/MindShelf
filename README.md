# MindShelf

A personal, single-owner thought journal built with React, TypeScript, FastAPI, and PostgreSQL.

## Deploy with GitHub + Render

1. Create a free PostgreSQL database at https://neon.tech and copy its connection URL.
2. In Render, select **New → Blueprint**, connect this repository and apply `render.yaml`.
3. In the backend service set `DATABASE_URL` to your Neon URL, changing `postgresql://` to `postgresql+psycopg://`. Set `OWNER_USERNAME` and a long unique `OWNER_PASSWORD`.
4. Set `FRONTEND_ORIGIN` in the backend to your actual frontend URL, e.g. `https://mindshelf-web.onrender.com`.
5. Set `VITE_API_URL` in the frontend to your actual backend URL, e.g. `https://mindshelf-api.onrender.com`, and redeploy the frontend to rebuild with that value.
6. Open your frontend URL, sign in and create your first thought.

The backend automatically runs Alembic migrations on startup. Only Brain Dump is implemented in this first release. Render's free backend may sleep when inactive.

**Privacy:** Never commit passwords or database URLs. This repository is public, but your entries are stored in PostgreSQL and the API requires owner credentials over HTTPS. The app uses simple HTTP Basic authentication with credentials kept in browser-tab memory; use a private device and a strong password.