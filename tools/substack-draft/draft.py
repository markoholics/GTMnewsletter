#!/usr/bin/env python3
"""Save a newsletter issue to Substack as a DRAFT. It never publishes or emails.

Usage:
  python3 tools/substack-draft/draft.py newsletter-drafts/YYYY-MM-DD --dry-run   # build and report, no network
  python3 tools/substack-draft/draft.py newsletter-drafts/YYYY-MM-DD --check     # log in and name the publication, no writes
  python3 tools/substack-draft/draft.py newsletter-drafts/YYYY-MM-DD             # create the draft

Environment:
  SUBSTACK_COOKIES          the browser cookie string for substack.com (must include substack.sid)
  SUBSTACK_PUBLICATION_URL  e.g. https://previouslyingtm.substack.com

Reads 02-article.md and issue.json from the folder. Images come from design-bw/images/.
This script imports only draft creation calls. publish_draft, schedule_draft and
prepublish_draft are deliberately never used.
"""
import json, os, re, sys

def build(folder):
    cfg = json.load(open(os.path.join(folder, 'issue.json')))
    lines = open(os.path.join(folder, '02-article.md')).read().split('\n')
    img_dir = os.path.join(folder, 'design-bw', 'images')
    if not os.path.isdir(img_dir):
        img_dir = os.path.join(folder, 'images')
    out, skipped_title, images = [], False, []
    for l in lines:
        s = l.strip()
        if s.startswith('**DRAFT'):
            continue
        if s.startswith('# ') and not skipped_title:
            skipped_title = True
            continue
        if s.startswith('*A long read') or s.startswith('*By '):
            continue
        m = re.match(r'\[IMAGE (\d+): ([^,]+), (.+)\]$', s)
        if m:
            fn, alt = m.group(2).strip(), m.group(3).strip()
            if fn == 'cover.png':
                continue  # the cover is set in Substack's post settings, not the body
            path = os.path.join(img_dir, fn)
            images.append(path)
            out.append('![%s](%s)' % (alt, path))
            continue
        out.append(l)
    md = '\n'.join(out)
    d = cfg.get('diagram')
    if d and os.path.exists(os.path.join(img_dir, 'before-after.png')):
        marker = re.sub(r'^<p>', '', d['insert_before'])
        if marker not in md:
            raise SystemExit('diagram.insert_before text not found in 02-article.md: %s' % marker)
        path = os.path.join(img_dir, 'before-after.png')
        images.append(path)
        md = md.replace(marker, '![%s](%s)\n\n%s' % (cfg['alts']['before-after.png'], path, marker), 1)
    missing = [p for p in images if not os.path.exists(p)]
    if missing:
        raise SystemExit('Missing image files: %s' % missing)
    return cfg['title'], cfg['standfirst'], md, images

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    flags = {a for a in sys.argv[1:] if a.startswith('--')}
    if len(args) != 1:
        raise SystemExit(__doc__)
    title, subtitle, md, images = build(args[0])
    if '--dry-run' in flags:
        print('DRY RUN. Title: %s\nSubtitle: %s\nBody: %d words, %d images\n' % (title, subtitle, len(md.split()), len(images)))
        for p in images:
            print('  image:', p)
        return
    cookies, pub = os.environ.get('SUBSTACK_COOKIES'), os.environ.get('SUBSTACK_PUBLICATION_URL')
    if not cookies or not pub:
        raise SystemExit('SUBSTACK_COOKIES and SUBSTACK_PUBLICATION_URL must be set. Nothing was sent.')
    from substack import Api
    try:
        api = Api(cookies_string=cookies, publication_url=pub, timeout=60)
    except Exception as e:
        raise SystemExit('Substack login failed (%s). The session cookie has probably expired: Mohammad must refresh SUBSTACK_COOKIES.' % e)
    print('Logged in. Publication:', api.publication_url)
    if '--check' in flags:
        return
    existing = [x for x in (api.get_drafts() or []) if (x.get('draft_title') or x.get('title')) == title]
    if existing:
        print('A draft titled "%s" already exists (id %s). Not creating a duplicate.' % (title, existing[0].get('id')))
        return
    res = api.create_draft_from_markdown(title=title, subtitle=subtitle, markdown=md, audience='everyone', prepublish=False, publish=False)
    draft = res['draft']
    print('Draft saved (not published). id: %s' % draft.get('id'))
    print('Edit it at: %s/publish/post/%s' % (pub.rstrip('/'), draft.get('id')))

if __name__ == '__main__':
    main()
