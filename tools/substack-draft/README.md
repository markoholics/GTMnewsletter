# Save the weekly issue to Substack as a draft

`draft.py` creates a Substack **draft** from `02-article.md` and `issue.json`, uploading the images from `design-bw/images/`. It never publishes, schedules or emails: only the draft creation calls of `python-substack` are used.

## One-off setup (Mohammad)
1. In a browser logged in to Substack, open developer tools, Application (or Storage), Cookies, `https://substack.com`.
2. Copy the cookie values (at least `substack.sid`) as one string: `substack.sid=...; substack.lli=...`.
3. In the routine's environment settings add two secrets:
   - `SUBSTACK_COOKIES` = that string
   - `SUBSTACK_PUBLICATION_URL` = `https://<your-publication>.substack.com`
4. The cookie gives full access to the account. Never paste it into chat, a file or a commit. Logging out of Substack everywhere revokes it.
5. Cookies expire. When a run reports "Substack login failed", paste a fresh cookie into `SUBSTACK_COOKIES`.

## Weekly step (after the pull request is open and the review email is sent)
```
pip install -r tools/substack-draft/requirements.txt
python3 tools/substack-draft/draft.py newsletter-drafts/YYYY-MM-DD --check   # optional: confirm login
python3 tools/substack-draft/draft.py newsletter-drafts/YYYY-MM-DD
```
Re-running is safe: if a draft with the same title exists it is left alone.

After saving, open the draft in Substack and set the cover image (`design-bw/images/newsletter-cover.jpg`) and check the layout before publishing by hand.
