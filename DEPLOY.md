# Deploy Orbis Visuals

Recommended path: Render Web Service.

## 1. Domain

Buy or control `orbisvisuals.com` from a registrar such as Namecheap, GoDaddy, Squarespace Domains, or Cloudflare Registrar.

## 2. Videos

The site uses YouTube embeds for the intro and portfolio videos. Local MP4 copies are ignored by Git and do not need to be uploaded.

## 3. Render settings

Create a new Render Web Service from the repository.

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`

## 4. Custom domain

In Render, open the service settings and add:

- `orbisvisuals.com`
- `www.orbisvisuals.com`

Then copy the DNS records Render gives you into your domain registrar's DNS settings. After DNS updates, verify the domain in Render.
