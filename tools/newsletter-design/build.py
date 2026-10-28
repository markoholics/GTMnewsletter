#!/usr/bin/env python3
"""Build the black, white and grey newsletter design for one issue.

Usage: python3 tools/newsletter-design/build.py newsletter-drafts/YYYY-MM-DD/issue.json

Reads issue.json plus 03-article-linkedin.html in the same folder and writes
design-bw/ (images, images/src, newsletter-bw.html). See DESIGN.md.
"""
import base64, html, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
E = lambda s: html.escape(s, quote=False)

def tpl(name):
    return open(os.path.join(HERE, 'templates', name)).read()

def fill(t, **kw):
    for k, v in kw.items():
        t = t.replace('{{%s}}' % k, v)
    left = re.findall(r'\{\{(\w+)\}\}', t)
    if left:
        raise SystemExit('Unfilled placeholders: %s' % left)
    return t

def main(cfg_path):
    cfg = json.load(open(cfg_path))
    folder = os.path.dirname(os.path.abspath(cfg_path))
    out = os.path.join(folder, 'design-bw')
    img = os.path.join(out, 'images'); src = os.path.join(img, 'src')
    os.makedirs(src, exist_ok=True)
    name, byline = cfg['name'], cfg['byline']
    jobs = []
    def page(fname, text, w, h, png=None, scale=1, typ='png'):
        p = os.path.join(src, fname); open(p, 'w').write(text)
        jobs.append(dict(html=p, out=os.path.join(img, png or fname.replace('.html', '.png')), w=w, h=h, scale=scale, type=typ))

    page('cover.html', fill(tpl('cover.html'), title=E(cfg['title']), cover_sub=E(cfg['cover_sub']), byline=E(byline), cover_tags=E(cfg['cover_tags']), name=E(name)), 1280, 720)
    i = cfg['insight']
    page('insight-card.html', fill(tpl('insight-card.html'), number=E(i['number']), text=E(i['text']), source=E(i['source']), label=E(i.get('label', 'By the numbers'))), 1200, 628)
    q = cfg['quote']
    page('quote-card.html', fill(tpl('quote-card.html'), text=E(q['text']), attribution=E(q['attribution']), label=E(q.get('label', 'Worth pinning above your desk'))), 1200, 628)
    f = cfg['framework']
    items = ''.join('<div class="col"><div class="h mono"><span>Step</span><span>%02d</span></div><div class="b"><h3>%s</h3><div class="q">%s</div><div class="e">%s</div></div></div>\n' % (n + 1, E(x['name']), E(x['question']), E(x['example'])) for n, x in enumerate(f['items']))
    page('framework.html', fill(tpl('framework.html'), title=E(f['title']), subtitle=E(f['subtitle']), footer=E(f['footer']), items=items), 1200, 628)
    d = cfg.get('diagram')
    if d:
        def panel(label, nodes, note, hl=None, dashed=()):
            cells = []
            for n, t in enumerate(nodes):
                cls = 'n' + (' hl' if n == hl else '') + (' dash' if n in dashed else '')
                if n: cells.append('<div class="a">&rarr;</div>')
                cells.append('<div class="%s">%s</div>' % (cls, E(t)))
            return '<div class="p"><div class="h mono blk"><span>%s</span><span>Illustration</span></div><div class="flow">%s</div><div class="note">%s</div></div>' % (E(label), ''.join(cells), E(note))
        panels = panel(d['before_label'], d['before_nodes'], d['before_note'], dashed=d.get('before_dashed', [])) + panel(d['after_label'], d['after_nodes'], d['after_note'], hl=d.get('after_highlight'))
        page('before-after.html', fill(tpl('before-after.html'), panels=panels, footnote=E(d['footnote'])), 1200, 628)
    nc = cfg.get('news_cover')
    if nc:
        variants = [dict(nc)] + [dict(nc, **a) for a in nc.get('alts', [])]
        for n, v in enumerate(variants):
            fn = 'news-cover' + ('' if n == 0 else '-alt%d' % n)
            page(fn + '.html', fill(tpl('news-cover.html'), name=E(name), kicker=E(v.get('kicker', 'Breaking')), dateline=E(v.get('dateline', cfg['date_display'])), headline=E(v['headline']), deck=E(v['deck']), byline=E(byline), tags=E(v.get('tags', cfg.get('cover_tags', ''))), size=str(v.get('size', 72))), 1280, 720)
    page('newsletter-cover.html', fill(tpl('newsletter-cover.html'), name=E(name), tagline=E(cfg['tagline'])), 1280, 720, png='newsletter-cover.jpg', scale=2, typ='jpeg')

    jp = os.path.join(src, 'jobs.json'); json.dump(jobs, open(jp, 'w'))
    env = dict(os.environ, NODE_PATH=os.environ.get('NODE_PATH', '/opt/node22/lib/node_modules'))
    subprocess.check_call(['node', os.path.join(HERE, 'render.js'), jp], env=env)
    os.remove(jp)

    # Review and share page
    def uri(fn):
        return 'data:image/png;base64,' + base64.b64encode(open(os.path.join(img, fn), 'rb').read()).decode()
    alts = cfg['alts']
    article = open(os.path.join(folder, '03-article-linkedin.html')).read().split('\n')[2:]  # drop standfirst and byline lines
    article = '\n'.join(article)
    chrome = '<figure><div class="chrome"><span class="dots"><i></i><i></i><i></i></span><span class="lab">%s</span></div><img src="%s" alt="%s"></figure>'
    def fig(m):
        fn = m.group(2)
        return chrome % ('Image %s / %s' % (m.group(1), fn), uri(fn), E(alts[fn]))
    article = re.sub(r'<p><em>\[Image (\d): (\S+)\. Upload from the images folder\. Alt text: [^\]]+\]</em></p>', lambda m: fig(m) if m.group(2) != 'cover.png' else '', article)
    if d:
        marker = d['insert_before']
        if marker not in article:
            raise SystemExit('diagram.insert_before text not found in article: %s' % marker)
        article = article.replace(marker, chrome % ('Illustration / before-after.png', uri('before-after.png'), E(alts['before-after.png'])) + '\n' + marker, 1)
    html_out = fill(tpl('../page_template.html'), page_title=E(cfg['page_title']), name=E(name), tagline=E(cfg['tagline']), title=E(cfg['title']), standfirst=E(cfg['standfirst']), byline=E(byline), date_display=E(cfg['date_display']), article=article)
    open(os.path.join(out, 'newsletter-bw.html'), 'w').write(html_out)
    print('Built', out)

if __name__ == '__main__':
    main(sys.argv[1])
