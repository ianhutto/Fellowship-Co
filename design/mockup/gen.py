# Generates Home-Desktop.dc.html and Home-Phone.dc.html (v6) from one component + icon set.
SP = '/tmp/claude-0/-home-claude/8a7925b3-9b44-5f65-9407-753277b31ecf/scratchpad'
B = {  # blob ids
    'hero': 'ec120d63a990880c64be4cd005a9e09f', 'wedding': 'fc479f54c7846dba94acb40147225491',
    'corporate': '3914911ac755f6ed8879e6dd3314d4a1', 'celebrations': '85dae0eb63902cfc4328eddac87654d6',
    'review': '408227baac01fcfb0a0c3eef7d129064', 'cafe': '9d492a23a7c242329723e9551446220b',
    'cta': '95640a2121fb8ca7374796634c84f583'}
def blob(k): return f'/_blob/{B[k]}'

# ---------- Fellowship line icon set (original; 24 grid, 1.75 stroke, round) ----------
P = {
 'phone': '<path d="M5 4h3l2 5-2.5 1.5a11 11 0 0 0 6 6L15 14l5 2v3a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
 'pin': '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'cal': '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
 'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
 'arrowl': '<path d="M19 12H5M11 6l-6 6 6 6"/>',
 'chev': '<path d="M6 9l6 6 6-6"/>',
 'rings': '<circle cx="9" cy="14.5" r="5.5"/><circle cx="15" cy="14.5" r="5.5"/><path d="M10 6l2-3 2 3-2 2z"/>',
 'brief': '<rect x="3" y="7.5" width="18" height="12.5" rx="2.5"/><path d="M9 7.5V6a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1.5M3 13h18M11 13v2h2v-2"/>',
 'party': '<path d="M12 3a5.5 5.5 0 0 1 5.5 5.5c0 3.8-2.8 7-5.5 7s-5.5-3.2-5.5-7A5.5 5.5 0 0 1 12 3z"/><path d="M11 15.5h2l-1 1.8zM12 17.3c0 1.7-2 2-2 3.7"/>',
 'cup': '<path d="M4 9h13v4.5A5.5 5.5 0 0 1 11.5 19h-2A5.5 5.5 0 0 1 4 13.5z"/><path d="M17 10.5h1.2a2.8 2.8 0 0 1 0 5.6H16.5M8 3.5c0 1.4 1 1.4 1 2.8M12 3.5c0 1.4 1 1.4 1 2.8"/>',
 'store': '<path d="M4.5 10.5V20h15v-9.5M3 10.5 5 4h14l2 6.5z"/><path d="M10 20v-5h4v5"/>',
 'tag': '<path d="M3.5 12.2V4.5a1 1 0 0 1 1-1h7.7l8.3 8.3-8.7 8.7z"/><circle cx="8" cy="8" r="1.5"/>',
 'check': '<path d="M5 12.5l4.5 4.5L19 7"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3.5 7l8.5 6 8.5-6"/>',
 'ig': '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".6" fill="currentColor"/>',
 'fb': '<path d="M15.5 8H17V4.6h-2.3C12.2 4.6 11 6.1 11 8.5v2H8.5V14H11v6.5h3.4V14H17l.5-3.5h-3.1V8.8c0-.5.3-.8 1.1-.8z"/>',
 'pause': '<path d="M9 6v12M15 6v12"/>',
 'shield': '<path d="M12 3l7 3v5.5c0 4.3-3 7.8-7 9.5-4-1.7-7-5.2-7-9.5V6z"/><path d="M8.8 12l2.3 2.3 4.2-4.6"/>',
}
def ic(name, size=20, sw=1.75, extra=''):
    return (f'<svg class="ic" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"{extra}>{P[name]}</svg>')
QUOTE = lambda w: f'<svg width="{w}" height="{int(w*0.75)}" viewBox="0 0 40 30" fill="#B5532C" aria-hidden="true"><path d="M3 30V18C3 8.5 8 2.3 16.5 0l2.2 4.2C13.4 6.3 11.3 9.6 11 14h7.5v16zM23 30V18c0-9.5 5-15.7 13.5-18l2.2 4.2c-5.3 2.1-7.4 5.4-7.7 9.8h7.5v16z"/></svg>'
STAR = '<path d="M12 3.2l2.7 5.5 6 .9-4.35 4.25 1.03 6-5.38-2.83-5.38 2.83 1.03-6L3.3 9.6l6-.9z"/>'
def stars(size=16, color='#B5532C'):
    one = f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="{color}" aria-hidden="true">{STAR}</svg>'
    return f'<span class="stars" role="img" aria-label="5 out of 5 stars">{one*5}</span>'
def swash(word, color='#E08A5E'):
    # hand-drawn underline under a key word (Fellowship emphasis device)
    return (f'<span class="sw">{word}<svg viewBox="0 0 200 14" preserveAspectRatio="none" aria-hidden="true">'
            f'<path d="M3 10.5C38 4.5 86 3 128 5.2c26 1.4 48 3.4 69-.8" fill="none" stroke="{color}" stroke-width="4.5" stroke-linecap="round"/></svg></span>')
def ph(text='Placeholder', pos='right: 12px; top: 12px;'):
    return f'<div class="ph" style="{pos}">{text}</div>'
def rings_bg(style):
    # faint concentric cup-ring motif (original background graphic)
    return (f'<svg aria-hidden="true" style="position: absolute; {style} pointer-events: none;" viewBox="0 0 400 400" fill="none" stroke="#E2D2BF" stroke-width="1.2">'
            '<circle cx="200" cy="200" r="198"/><circle cx="200" cy="200" r="168" stroke-dasharray="2 7"/><circle cx="200" cy="200" r="138"/>'
            '<circle cx="214" cy="190" r="120" stroke-opacity=".6"/></svg>')

CSS = """
body{margin:0;background:#FAF6F0;font-family:'Figtree',system-ui,sans-serif;color:#1C1410}
a{color:#1C1410}
.d{font-family:'Bricolage Grotesque',sans-serif;font-weight:700}
.ic{display:inline-block;flex-shrink:0}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;border-radius:999px;text-decoration:none;font-weight:600;white-space:nowrap}
.bp{background:#B5532C;color:#FFFFFF}
.bd{background:#1C1410;color:#FAF6F0}
.bo{border:1.5px solid #1C1410;color:#1C1410}
.bl{border:1.5px solid rgba(250,246,240,.55);color:#FAF6F0}
.cue{display:flex;align-items:center;gap:10px;font-size:14px;font-weight:600;letter-spacing:.02em;color:#1C1410}
.cue b{color:#B5532C;font-weight:700}.cue i{display:block;width:28px;height:1.5px;background:#B5532C}
.cue.dk{color:#FAF6F0}.cue.dk b{color:#E08A5E}.cue.dk i{background:#E08A5E}
.ph{position:absolute;font-size:10px;letter-spacing:.02em;color:#FAF6F0;background:rgba(28,20,16,.55);padding:3px 7px;border-radius:4px}
.badge{position:absolute;display:flex;align-items:center;justify-content:center;border-radius:50%;background:#FAF6F0;color:#B5532C;box-shadow:0 4px 14px rgba(28,20,16,.22)}
.tile{display:flex;align-items:center;justify-content:center;border-radius:12px;background:#F1E8DC;color:#B5532C;flex-shrink:0}
.lnk{display:inline-flex;align-items:center;gap:8px;font-weight:600;text-decoration:none;color:#1C1410}
.stars{display:inline-flex;gap:2px}
.sw{position:relative;white-space:nowrap;display:inline-block}
.sw svg{position:absolute;left:-2%;width:104%;bottom:-.1em;height:.2em;overflow:visible}
.card{background:#FFFDF9;border:1px solid #EADFD1;border-radius:16px}
.av{display:flex;align-items:center;justify-content:center;border-radius:50%;background:#F1E8DC;color:#8A6A52;font-weight:700;flex-shrink:0}
.pill{display:inline-flex;align-items:center;border:1px solid #E6D9C8;border-radius:999px;color:#6B5A4C}
.soc{display:flex;align-items:center;justify-content:center;border-radius:50%;border:1.5px solid #D8C8B5;color:#1C1410}
.dot{width:8px;height:8px;border-radius:50%;background:#D8C8B5}
.mq{display:flex;align-items:center;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent);mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent)}
.mq span.n{white-space:nowrap;color:#8A7867}
.ctl{display:inline-flex;align-items:center;gap:6px;border-radius:999px;font-weight:600;border:none;cursor:pointer;font-family:'Figtree',sans-serif}
"""

def page(title, width, body):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&amp;family=Figtree:wght@400;500;600&amp;display=swap" rel="stylesheet">
<style>{CSS}</style>
</helmet>
<div style="width: {width}px; height: __H__px; box-sizing: border-box; background: #FAF6F0; color: #1C1410; display: flex; flex-direction: column; overflow: hidden;">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{width},"height":__H__}}}}'>
class Component extends DCLogic {{
renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''

CARDS = [
 ('wedding', 'rings', 'Weddings', 'Swap the open bar for an espresso bar.', 'A coffee bar gives guests something to gather around at cocktail hour.', 'Plan your wedding coffee', 'Placeholder: latte held in two hands'),
 ('corporate', 'brief', 'Corporate', 'Say thank you in lattes.', 'Americanos, cappuccinos and chai for your team, right where they work.', 'Book for your team', 'Placeholder: friends working over coffee'),
 ('celebrations', 'party', 'Celebrations', 'Coffee for the grown-ups. Cocoa for the kids.', "Showers, birthdays and appreciation days. If the cart fits, we'll be there.", 'Plan your party', 'Placeholder: hot cocoa with marshmallows'),
]
PRESS = ['Community Impact', 'WhatNow Houston']
BEAN = '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" style="flex-shrink:0"><ellipse cx="12" cy="12" rx="7" ry="9.5" transform="rotate(35 12 12)" fill="#D2B79B"/><path d="M8.5 5.5c3 3.5 3.5 9 7 13" stroke="#FAF6F0" stroke-width="1.6" fill="none" stroke-linecap="round" transform="rotate(0 12 12)"/></svg>'

# =============================== DESKTOP ===============================
def desktop():
    W = 1200
    h = []
    # 1 utility bar
    h.append(f'''<!-- 1 Utility bar -->
<div style="background: #1C1410; color: #F1E6D8;">
<div style="width: {W}px; margin: 0 auto; height: 44px; display: flex; align-items: center; justify-content: space-between; font-size: 13px; letter-spacing: 0.02em;">
<span style="display: flex; align-items: center; gap: 8px;">{ic('clock',15)} Coffee catering for Houston events · Café open today until [6 PM]</span>
<div style="display: flex; gap: 28px;"><span style="display: flex; align-items: center; gap: 7px;">{ic('pin',15)} 3434 FM 1092, Missouri City</span><a href="#" style="color: #F1E6D8; text-decoration: none; font-weight: 600; display: flex; align-items: center; gap: 7px;">{ic('phone',15)} (832) 427-7363</a></div>
</div>
</div>''')
    # header
    h.append(f'''<!-- Header -->
<div style="background: #FAF6F0; border-bottom: 1px solid #E6D9C8;">
<div style="width: {W}px; margin: 0 auto; height: 84px; display: flex; align-items: center; justify-content: space-between;">
<div class="d" style="font-size: 30px; letter-spacing: -0.03em;">Fellowship<span style="color: #B5532C;">.</span></div>
<div style="display: flex; align-items: center; gap: 36px; font-size: 16px; font-weight: 500;">
<a href="#" style="text-decoration: none;">About</a>
<a href="#" style="text-decoration: none; display: flex; align-items: center; gap: 4px;">Services {ic('chev',16,2)}</a>
<a href="#" style="text-decoration: none; display: flex; align-items: center; gap: 4px;">Resources {ic('chev',16,2)}</a>
<a href="#" class="btn bp" style="padding: 13px 22px; font-size: 15px;">Get a quote {ic('cal',17)}</a>
</div>
</div>
</div>''')
    # hero
    h.append(f'''<!-- 2 Hero -->
<div style="position: relative; height: 760px; background: #2B1F18; overflow: hidden; color: #FAF6F0;">
<img src="{blob('hero')}" alt="Placeholder: milk being poured into a latte" style="position: absolute; top: 0; left: 34%; width: 80%; height: 100%; object-fit: cover; object-position: 40% 62%; -webkit-mask-image: linear-gradient(90deg, transparent 0%, #000 28%); mask-image: linear-gradient(90deg, transparent 0%, #000 28%);">
<div style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(28,20,16,1) 0%, rgba(28,20,16,0.85) 38%, rgba(28,20,16,0) 70%);"></div>
{ph('Placeholder · hero video', 'right: 24px; top: 20px;')}
<div style="position: relative; width: {W}px; height: 100%; margin: 0 auto; box-sizing: border-box; padding: 80px 0 48px; display: flex; flex-direction: column; justify-content: center; gap: 16px;">
<div style="display: flex; align-items: center; gap: 10px; font-size: 15px; font-weight: 600; letter-spacing: 0.02em; color: #E9B48F;">Mobile espresso bar <span style="width: 4px; height: 4px; border-radius: 50%; background: #E08A5E;"></span> Houston &amp; Missouri City</div>
<h1 class="d" style="margin: 0; font-size: 84px; line-height: 0.96; letter-spacing: -0.04em; max-width: 620px; text-wrap: balance;">Your event, with a coffee shop in the room.</h1>
<p style="margin: 8px 0 0; font-size: 20px; line-height: 1.5; max-width: 520px; color: #EADBCB;">A full espresso bar and friendly baristas for weddings, offices and celebrations. We set up, serve and clean up.</p>
<div style="display: flex; gap: 16px; align-items: center; margin-top: 16px;">
<a href="#" class="btn bp" style="padding: 18px 30px; font-size: 17px;">Get a quote {ic('cal',18)}</a>
<a href="#" class="btn bl" style="padding: 17px 28px; font-size: 17px;">See the menu {ic('arrow',18)}</a>
</div>
</div>
<button type="button" class="ctl" aria-label="Pause background video" style="position: absolute; right: 24px; bottom: 24px; background: rgba(250,246,240,0.14); color: #FAF6F0; padding: 9px 14px; font-size: 13px;">{ic('pause',14,2.2)} Pause</button>
</div>''')
    # trust strip (marquee)
    names = ''.join(f'<span class="n d" style="font-size: 26px; letter-spacing: -0.02em;">{n}</span>{BEAN}' for n in PRESS*4)
    h.append(f'''<!-- 3 Trust strip: marquee with pause -->
<div style="background: #F3ECE2; border-bottom: 1px solid #E6D9C8;">
<div style="width: {W}px; margin: 0 auto; padding: 48px 0; display: flex; flex-direction: column; align-items: center; gap: 24px;">
<span style="font-size: 14px; font-weight: 600; letter-spacing: 0.02em; color: #6B5A4C;">Serving Houston since 2021 · As featured in [confirm]</span>
<div style="display: flex; align-items: center; gap: 32px; width: 100%;">
<div class="mq" style="gap: 44px; flex-grow: 1;">{names}</div>
<button type="button" class="ctl" aria-label="Pause logo scroll" style="width: 36px; height: 36px; justify-content: center; background: #FAF6F0; color: #6B5A4C; border: 1px solid #E6D9C8;">{ic('pause',14,2.2)}</button>
</div>
</div>
</div>''')
    # what we do + cards
    cards = ''
    for key, icon, label, title, body, link, alt in CARDS:
        cards += f'''<div class="card" style="overflow: hidden; display: flex; flex-direction: column;">
<div style="position: relative; height: 300px;"><img src="{blob(key)}" alt="{alt}" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;">{ph()}<div class="badge" style="left: 20px; bottom: -24px; width: 52px; height: 52px;">{ic(icon,24)}</div></div>
<div style="padding: 44px 28px 28px; display: flex; flex-direction: column; gap: 12px; flex-grow: 1;">
<div style="font-size: 13px; font-weight: 600; color: #8A6A52;">{label}</div>
<h3 class="d" style="margin: 0; font-size: 28px; line-height: 1.08; letter-spacing: -0.025em; text-wrap: balance; hyphens: manual;">{title}</h3>
<p style="margin: 0; font-size: 16px; line-height: 1.6; color: #4E3F34; flex-grow: 1;">{body}</p>
<div style="border-top: 1px solid #EADFD1; padding-top: 18px; margin-top: 8px;"><a href="#" class="lnk" style="font-size: 15px;">{link} {ic('arrow',17)}</a></div>
</div>
</div>
'''
    h.append(f'''<!-- 4 What we do: intro + three cards -->
<div style="position: relative; background: linear-gradient(180deg, #FAF6F0 0%, #F1E8DC 38%, #F1E8DC 100%); overflow: hidden;">
<div style="position: relative; width: {W}px; margin: 0 auto; padding: 80px 0; display: flex; flex-direction: column; gap: 56px;">
<div style="display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 24px; align-items: center;">
<div style="grid-column: span 5; display: flex; flex-direction: column; gap: 16px; padding-right: 24px;">
<div class="cue"><b>01</b><i></i>What we do</div>
<h2 class="d" style="margin: 0; font-size: 56px; line-height: 1; letter-spacing: -0.035em;">A coffee shop that shows up.</h2>
<p style="margin: 0; font-size: 18px; line-height: 1.6; color: #4E3F34;">Espresso, lattes, chai, matcha and hot cocoa, made to order by our baristas. Hot or iced, with dairy-free milks. We bring the bar, the beans and the people who know what to do with them.</p>
<div style="margin-top: 8px;"><a href="#" class="btn bo" style="padding: 15px 24px; font-size: 16px;">See the menu {ic('arrow',17)}</a></div>
</div>
<div style="grid-column: span 7; position: relative; height: 400px; border-radius: 16px; overflow: hidden; background: #8C6A4F;">
<img src="{blob('review')}" alt="Placeholder: latte on a wooden table" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;">{ph()}
<div style="position: absolute; left: 20px; bottom: 20px; display: flex; align-items: center; gap: 10px; background: rgba(250,246,240,0.94); border-radius: 999px; padding: 8px 16px 8px 8px; font-size: 14px; font-weight: 600;"><span class="tile" style="width: 32px; height: 32px; border-radius: 50%;">{ic('cup',17)}</span>Hot or iced · dairy-free milks</div>
</div>
</div>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px;">
{cards}</div>
</div>
</div>''')
    # difference + stat tiles
    def stat(icon, label, fig, dark=False):
        bg = 'background: #B5532C; color: #FFFFFF; border: none;' if dark else ''
        tile = f'<span class="tile" style="width: 48px; height: 48px;{" background: rgba(255,255,255,0.16); color: #FFFFFF;" if dark else ""}">{ic(icon,24)}</span>'
        lc = '#FFF3EA' if dark else '#6B5A4C'
        return f'''<div class="card" style="{bg} padding: 28px; display: flex; justify-content: space-between; align-items: flex-end; min-height: 172px; box-sizing: border-box;">
<div style="display: flex; flex-direction: column; justify-content: space-between; align-self: stretch;">{tile}<div style="font-size: 15px; color: {lc};">{label}</div></div>
<div style="text-align: right;">{fig}</div>
</div>'''
    FIG = 'font-size: 64px; line-height: 1; letter-spacing: -0.04em;'
    price = f'<div class="d" style="{FIG}">[$X]</div>'
    h.append(f'''<!-- 6 Difference: inset band + stat tiles -->
<div style="width: {W}px; margin: 0 auto; padding: 80px 0; display: flex; flex-direction: column; gap: 24px;">
<div style="position: relative; border-radius: 20px; overflow: hidden; background: #1C1410; color: #FAF6F0; padding: 72px 64px; display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 24px; align-items: end;">
<img src="{blob('cafe')}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.55;">
<div style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(20,12,8,0.92) 0%, rgba(20,12,8,0.5) 100%);"></div>
<div style="position: relative; grid-column: span 7; display: flex; flex-direction: column; gap: 18px;">
<div class="cue dk"><b>02</b><i></i>Why Fellowship</div>
<h2 class="d" style="margin: 0; font-size: 72px; line-height: 1; letter-spacing: -0.04em;">A real café, on wheels<span style="color: #E08A5E;">.</span></h2>
</div>
<div style="position: relative; grid-column: span 5; display: flex; flex-direction: column; gap: 20px; align-items: flex-start;">
<p style="margin: 0; font-size: 18px; line-height: 1.6; color: #E4D3C1;">Fellowship started as a coffee cart in 2021 and opened a café in Missouri City in 2024. Every event gets the same coffee and care as the shop.</p>
<a href="#" class="btn bp" style="padding: 16px 26px; font-size: 16px;">Get a quote {ic('cal',17)}</a>
</div>
{ph('Placeholder', 'right: 16px; top: 16px;')}
</div>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px;">
{stat('cal', 'Serving Houston events since', f'<div class="d" style="{FIG}">2021</div>')}
{stat('tag', 'Mobile bookings from<br><span style="font-size: 13px; opacity: 0.8;">Price: owner to confirm</span>', price, dark=True)}
{stat('store', 'Our Missouri City café opened', f'<div class="d" style="{FIG}">2024</div>')}
</div>
</div>''')
    # reviews
    def rcard(ev):
        return f'''<div class="card" style="padding: 28px; display: flex; flex-direction: column; gap: 18px; box-sizing: border-box;">
<div style="display: flex; justify-content: space-between; align-items: center;"><span style="display: flex; align-items: center; gap: 8px; font-size: 14px; color: #6B5A4C;"><span class="av" style="width: 26px; height: 26px; font-size: 11px;">{ic('shield',15)}</span>[Rating source] review</span>{stars(15)}</div>
{QUOTE(34)}
<p style="margin: 0; font-size: 19px; line-height: 1.55; flex-grow: 1;">[Owner-supplied review, with permission.]</p>
<div style="border-top: 1px solid #EADFD1; padding-top: 18px; display: flex; align-items: center; justify-content: space-between;"><span style="display: flex; align-items: center; gap: 12px;"><span class="av" style="width: 40px; height: 40px; font-size: 15px;">[N]</span><strong style="font-size: 15px;">[Name]</strong></span><span class="pill" style="padding: 5px 12px; font-size: 13px;">{ev}</span></div>
</div>'''
    h.append(f'''<!-- 7 Reviews -->
<div style="border-top: 1px solid #E6D9C8;">
<div style="width: {W}px; margin: 0 auto; padding: 80px 0; display: flex; flex-direction: column; gap: 32px;">
<div style="display: flex; justify-content: space-between; align-items: flex-end;">
<div style="display: flex; flex-direction: column; gap: 16px;"><div class="cue"><b>03</b><i></i>Kind words</div>
<h2 class="d" style="margin: 0; font-size: 56px; line-height: 1; letter-spacing: -0.035em;">From people who've had us over.</h2></div>
<div style="display: flex; gap: 10px;">
<button type="button" class="ctl" aria-label="Previous reviews" style="width: 48px; height: 48px; justify-content: center; border: 1.5px solid #1C1410; background: transparent; color: #1C1410;">{ic('arrowl',18)}</button>
<button type="button" class="ctl" aria-label="Next reviews" style="width: 48px; height: 48px; justify-content: center; background: #1C1410; color: #FAF6F0;">{ic('arrow',18)}</button>
</div>
</div>
<div style="display: grid; grid-template-columns: 1fr 1.4fr 1.4fr; gap: 24px;">
<div style="position: relative; overflow: hidden; background: #1C1410; color: #FAF6F0; border-radius: 16px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
<div style="position: absolute; right: -60px; top: -60px; width: 200px; height: 200px; border-radius: 50%; background: radial-gradient(circle, rgba(224,138,94,0.35), rgba(224,138,94,0) 70%);"></div>
<div style="position: relative; display: flex; align-items: center; gap: 12px;"><span style="width: 44px; height: 44px; border-radius: 50%; background: #FAF6F0; color: #B5532C; display: flex; align-items: center; justify-content: center;">{ic('shield',22)}</span><div><div style="font-size: 16px; font-weight: 600;">[Rating source]</div><div style="display: flex; align-items: center; gap: 8px; margin-top: 4px;">{stars(14,'#E08A5E')}<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.06em; color: #D9C9B8;">VERIFIED</span></div></div></div>
<div style="position: relative; border-top: 1px solid rgba(250,246,240,0.16); padding-top: 20px;"><div class="d" style="font-size: 72px; line-height: 1; letter-spacing: -0.04em;">[4.x]</div><div style="font-size: 15px; color: #D9C9B8; margin-top: 8px;">[N] reviews · as of [date]</div></div>
</div>
{rcard('Wedding')}
{rcard('Corporate')}
</div>
<div style="display: flex; justify-content: center; align-items: center; gap: 8px;"><span class="dot" style="width: 24px; border-radius: 4px; background: #1C1410;"></span><span class="dot"></span><span class="dot"></span></div>
</div>
</div>''')
    # CTA
    h.append(f'''<!-- 8 Closing CTA -->
<div style="position: relative; background: #1C1410; color: #FAF6F0; overflow: hidden;">
<img src="{blob('cta')}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.8; object-position: 50% 18%; filter: blur(6px); transform: scale(1.06);">
<div style="position: absolute; inset: 0; background: rgba(20,12,8,0.66);"></div>
<div style="position: absolute; left: -160px; bottom: -220px; width: 620px; height: 620px; border-radius: 50%; background: radial-gradient(circle, rgba(181,83,44,0.38), rgba(181,83,44,0) 68%);"></div>
<div style="position: absolute; right: -120px; top: -200px; width: 560px; height: 560px; border-radius: 50%; background: radial-gradient(circle, rgba(233,180,143,0.22), rgba(233,180,143,0) 68%);"></div>
<div style="position: relative; width: {W}px; margin: 0 auto; padding: 96px 0; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 20px;">
<div class="cue dk"><b>04</b><i></i>Get in touch</div>
<h2 class="d" style="margin: 0; font-size: 80px; line-height: 1; letter-spacing: -0.04em; max-width: 900px; text-wrap: balance;">Let's put coffee on the {swash('guest list.')}</h2>
<p style="margin: 0; font-size: 19px; line-height: 1.5; color: #E4D3C1; text-wrap: balance;">Share the date, headcount and location. We'll send a quote.</p>
<a href="#" class="btn bp" style="margin-top: 12px; padding: 19px 32px; font-size: 17px;">Get a quote {ic('cal',18)}</a>
<div style="font-size: 14px; color: rgba(250,246,240,0.78);">We reply within [owner to confirm]</div>
<div style="display: flex; gap: 28px; margin-top: 12px; font-size: 15px; color: #EADBCB;">
<span style="display: flex; align-items: center; gap: 8px;"><span style="color: #E08A5E; display: flex;">{ic('check',17,2.2)}</span>We set up, serve and clean up</span>
<span style="display: flex; align-items: center; gap: 8px;"><span style="color: #E08A5E; display: flex;">{ic('check',17,2.2)}</span>Hot or iced, dairy-free milks</span>
<span style="display: flex; align-items: center; gap: 8px;"><span style="color: #E08A5E; display: flex;">{ic('check',17,2.2)}</span>Serving [service area]</span>
</div>
</div>
</div>''')
    # footer
    col = lambda title, items: f'<div style="display: flex; flex-direction: column; gap: 12px;"><span style="font-size: 13px; font-weight: 600; letter-spacing: 0.04em; color: #8A7867;">{title}</span>{items}</div>'
    a = lambda t: f'<a href="#" style="text-decoration: none; font-size: 15px; font-weight: 500;">{t}</a>'
    s = lambda t: f'<span style="font-size: 15px; color: #4E3F34;">{t}</span>'
    h.append(f'''<!-- 9 Footer -->
<div style="flex-grow: 1; background: #FAF6F0; position: relative; overflow: hidden;">
<div style="width: {W}px; margin: 0 auto; padding: 48px 0 0; display: flex; flex-direction: column; gap: 48px;">
<div style="display: flex; justify-content: space-between;">
<div style="display: flex; flex-direction: column; gap: 18px; max-width: 300px;">
<div class="d" style="font-size: 34px; letter-spacing: -0.03em;">Fellowship<span style="color: #B5532C;">.</span></div>
<p style="margin: 0; font-size: 16px; line-height: 1.6; color: #4E3F34;">Coffee is better shared. That's the whole idea behind the name.</p>
<div><a href="#" class="btn bp" style="padding: 13px 22px; font-size: 14px;">Get a quote {ic('cal',16)}</a></div>
<div style="display: flex; gap: 10px;"><a href="#" class="soc" aria-label="Instagram" style="width: 40px; height: 40px;">{ic('ig',19)}</a><a href="#" class="soc" aria-label="Facebook" style="width: 40px; height: 40px;">{ic('fb',19)}</a></div>
</div>
<div style="display: flex; gap: 96px;">
{col('SERVICES', a('Weddings')+a('Corporate')+a('Celebrations'))}
{col('RESOURCES', a('Menu')+a('FAQs')+a('The Coffee Shop')+a('About'))}
{col('VISIT THE CAFÉ', f'<span style="display: flex; gap: 8px; color: #4E3F34; font-size: 15px; line-height: 1.5;"><span style="color: #B5532C; margin-top: 1px;">{ic("pin",17)}</span>3434 FM 1092 Rd #350<br>Missouri City, TX 77459</span><span style="display: flex; gap: 8px; align-items: center; color: #4E3F34; font-size: 15px;"><span style="color: #B5532C; display: flex;">{ic("clock",17)}</span>[Hours]</span><span style="display: flex; gap: 8px; align-items: center; font-size: 15px; font-weight: 600;"><span style="color: #B5532C; display: flex;">{ic("phone",17)}</span>(832) 427-7363</span>')}
</div>
</div>
<div class="card" style="padding: 20px 20px 20px 24px; display: flex; align-items: center; justify-content: space-between;">
<div style="display: flex; align-items: center; gap: 16px;"><span style="width: 48px; height: 48px; border-radius: 50%; border: 1.5px solid #E6D9C8; color: #B5532C; display: flex; align-items: center; justify-content: center;">{ic('mail',22)}</span><div class="d" style="font-size: 22px; letter-spacing: -0.02em;">Coffee news, now and then</div></div>
<div style="display: flex; gap: 8px; width: 420px;"><label style="flex-grow: 1; display: flex;"><span style="position: absolute; left: -9999px;">Email</span><input type="email" placeholder="Your email" style="width: 100%; border: 1px solid #E6D9C8; background: #FAF6F0; border-radius: 999px; padding: 13px 18px; font: 15px 'Figtree', sans-serif;"></label><button type="button" class="ctl bd" style="padding: 0 22px; font-size: 14px;">Sign up</button></div>
</div>
<div style="display: flex; justify-content: space-between; border-top: 1px solid #E6D9C8; padding-top: 24px; font-size: 14px; color: #6B5A4C;">
<span>© 2026 Fellowship Coffee Co.</span><span style="display: flex; gap: 24px;"><a href="#" style="color: #6B5A4C;">Privacy</a><a href="#" style="color: #6B5A4C;">Contact</a></span>
</div>
</div>
<div class="d" aria-hidden="true" style="width: {W}px; margin: 16px auto 0; text-indent: -14px; font-size: 236px; line-height: 1; letter-spacing: -0.055em; color: #EFE4D6; white-space: nowrap; height: 190px; overflow: hidden;">Fellowship<span style="color: #EBCDBC;">.</span></div>
</div>''')
    return page('Fellowship home, desktop v6', 1440, '\n\n'.join(h))

# =============================== PHONE ===============================
def phone():
    h = []
    h.append(f'''<div style="background: #1C1410; color: #F1E6D8; height: 36px; display: flex; align-items: center; justify-content: center; gap: 10px; font-size: 12px;">
<span style="display: flex; align-items: center; gap: 6px;">{ic('clock',13)} Café open today until [6 PM]</span><span style="opacity: 0.4;">·</span><a href="#" style="color: #F1E6D8; text-decoration: none; font-weight: 600; display: flex; align-items: center; gap: 6px;">{ic('phone',13)} (832) 427-7363</a>
</div>
<div style="height: 64px; box-sizing: border-box; padding: 0 20px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #E6D9C8;">
<div class="d" style="font-size: 24px; letter-spacing: -0.03em;">Fellowship<span style="color: #B5532C;">.</span></div>
<div style="display: flex; align-items: center; gap: 8px;">
<a href="#" class="btn bp" style="padding: 11px 15px; font-size: 13px; gap: 7px;">Get a quote {ic('cal',14)}</a>
<button type="button" aria-label="Open menu" style="width: 44px; height: 44px; border-radius: 50%; border: 1.5px solid #1C1410; background: transparent; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 5px; cursor: pointer;"><span style="width: 16px; height: 1.5px; background: #1C1410;"></span><span style="width: 16px; height: 1.5px; background: #1C1410;"></span></button>
</div>
</div>''')
    h.append(f'''<div style="position: relative; height: 660px; background: #2B1F18; overflow: hidden; color: #FAF6F0;">
<img src="{blob('hero')}" alt="Placeholder: milk being poured into a latte" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 45% 45%;">
<div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(20,12,8,0.2) 0%, rgba(20,12,8,0.72) 40%, rgba(20,12,8,0.94) 100%);"></div>
{ph('Placeholder · hero video', 'left: 12px; top: 12px;')}
<button type="button" class="ctl" aria-label="Pause background video" style="position: absolute; right: 16px; top: 12px; background: rgba(250,246,240,0.14); color: #FAF6F0; padding: 7px 12px; font-size: 12px;">{ic('pause',12,2.2)} Pause</button>
<div style="position: relative; height: 100%; box-sizing: border-box; padding: 160px 20px 48px; display: flex; flex-direction: column; justify-content: flex-end; gap: 16px;">
<div style="display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 600; color: #E9B48F;">Mobile espresso bar <span style="width: 4px; height: 4px; border-radius: 50%; background: #E08A5E;"></span> Houston</div>
<h1 class="d" style="margin: 0; font-size: 46px; line-height: 0.98; letter-spacing: -0.035em; text-wrap: balance;">Your event, with a coffee shop in the room.</h1>
<p style="margin: 0; font-size: 16px; line-height: 1.5; color: #EADBCB;">A full espresso bar and friendly baristas for weddings, offices and celebrations.</p>
<a href="#" class="btn bp" style="margin-top: 8px; padding: 17px; font-size: 16px;">Get a quote {ic('cal',17)}</a>
<a href="#" class="btn bl" style="padding: 16px; font-size: 16px;">See the menu {ic('arrow',17)}</a>
</div>
</div>''')
    names = ''.join(f'<span class="n d" style="font-size: 19px; letter-spacing: -0.02em;">{n}</span>{BEAN}' for n in PRESS*4)
    h.append(f'''<div style="background: #F3ECE2; border-bottom: 1px solid #E6D9C8; padding: 48px 0; display: flex; flex-direction: column; align-items: center; gap: 18px;">
<span style="font-size: 12px; font-weight: 600; color: #6B5A4C;">Serving Houston since 2021 · As featured in [confirm]</span>
<div class="mq" style="gap: 28px; width: 100%; padding-left: 20px;">{names}</div>
<button type="button" class="ctl" aria-label="Pause logo scroll" style="background: #FAF6F0; color: #6B5A4C; border: 1px solid #E6D9C8; padding: 7px 12px; font-size: 12px;">{ic('pause',12,2.2)} Pause</button>
</div>''')
    cards = ''
    for key, icon, label, title, body, link, alt in CARDS:
        cards += f'''<div class="card" style="overflow: hidden;"><div style="position: relative; height: 220px;"><img src="{blob(key)}" alt="{alt}" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;">{ph('Placeholder','right: 10px; top: 10px;')}<div class="badge" style="left: 18px; bottom: -22px; width: 46px; height: 46px;">{ic(icon,22)}</div></div>
<div style="padding: 36px 20px 20px; display: flex; flex-direction: column; gap: 8px;"><div style="font-size: 13px; font-weight: 600; color: #8A6A52;">{label}</div><h3 class="d" style="margin: 0; font-size: 24px; line-height: 1.1; letter-spacing: -0.02em; text-wrap: balance; hyphens: manual;">{title}</h3><p style="margin: 0; font-size: 15px; line-height: 1.55; color: #4E3F34;">{body}</p><div style="border-top: 1px solid #EADFD1; padding-top: 14px; margin-top: 6px;"><a href="#" class="lnk" style="font-size: 15px;">{link} {ic('arrow',16)}</a></div></div></div>
'''
    h.append(f'''<div style="position: relative; overflow: hidden; background: linear-gradient(180deg, #FAF6F0 0%, #F1E8DC 22%, #F1E8DC 100%);">
<div style="position: relative; padding: 40px 20px; display: flex; flex-direction: column; gap: 16px;">
<div class="cue" style="font-size: 13px;"><b>01</b><i></i>What we do</div>
<h2 class="d" style="margin: 0; font-size: 38px; line-height: 1; letter-spacing: -0.03em;">A coffee shop that shows up.</h2>
<p style="margin: 0; font-size: 16px; line-height: 1.6; color: #4E3F34;">Espresso, lattes, chai, matcha and hot cocoa, made to order by our baristas. Hot or iced, with dairy-free milks.</p>
<div style="position: relative; height: 260px; border-radius: 14px; overflow: hidden; margin-top: 8px;"><img src="{blob('review')}" alt="Placeholder: latte on a wooden table" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;">{ph('Placeholder','right: 10px; top: 10px;')}<div style="position: absolute; left: 12px; bottom: 12px; display: flex; align-items: center; gap: 8px; background: rgba(250,246,240,0.94); border-radius: 999px; padding: 6px 12px 6px 6px; font-size: 12px; font-weight: 600;"><span class="tile" style="width: 26px; height: 26px; border-radius: 50%;">{ic('cup',14)}</span>Hot or iced · dairy-free milks</div></div>
<a href="#" class="btn bo" style="align-self: flex-start; padding: 13px 20px; font-size: 15px;">See the menu {ic('arrow',16)}</a>
<div style="display: flex; flex-direction: column; gap: 20px; margin-top: 24px;">
{cards}</div>
</div>
</div>''')
    FIG = 'font-size: 48px; line-height: 1; letter-spacing: -0.04em;'
    def stat(icon, label, fig, dark=False):
        bg = 'background: #B5532C; color: #FFFFFF; border: none;' if dark else ''
        t = ' background: rgba(255,255,255,0.16); color: #FFFFFF;' if dark else ''
        return f'<div class="card" style="{bg} padding: 20px; display: flex; align-items: center; gap: 16px;"><span class="tile" style="width: 44px; height: 44px;{t}">{ic(icon,22)}</span><div style="flex-grow: 1; font-size: 14px; color: {"#FFF3EA" if dark else "#6B5A4C"};">{label}</div><div style="text-align: right;">{fig}</div></div>'
    price = f'<div class="d" style="{FIG}">[$X]</div>'
    h.append(f'''<div style="padding: 40px 20px; display: flex; flex-direction: column; gap: 16px;">
<div style="position: relative; border-radius: 16px; overflow: hidden; background: #1C1410; color: #FAF6F0; padding: 36px 24px; display: flex; flex-direction: column; gap: 16px;">
<img src="{blob('cafe')}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.5;">
<div style="position: absolute; inset: 0; background: rgba(20,12,8,0.62);"></div>
<div class="cue dk" style="position: relative; font-size: 13px;"><b>02</b><i></i>Why Fellowship</div>
<h2 class="d" style="position: relative; margin: 0; font-size: 42px; line-height: 1.02; letter-spacing: -0.035em;">A real café, on wheels<span style="color: #E08A5E;">.</span></h2>
<p style="position: relative; margin: 0; font-size: 15px; line-height: 1.6; color: #E4D3C1;">Fellowship started as a coffee cart in 2021 and opened a café in Missouri City in 2024.</p>
<a href="#" class="btn bp" style="position: relative; padding: 15px; font-size: 15px;">Get a quote {ic('cal',16)}</a>
</div>
{stat('cal','Serving Houston events since', f'<div class="d" style="{FIG}">2021</div>')}
{stat('tag','Mobile bookings from<br><span style="font-size: 12px; opacity: 0.8;">Price: owner to confirm</span>', price, True)}
{stat('store','Our Missouri City café opened', f'<div class="d" style="{FIG}">2024</div>')}
</div>''')
    h.append(f'''<div style="border-top: 1px solid #E6D9C8; padding: 40px 20px; display: flex; flex-direction: column; gap: 20px;">
<div class="cue" style="font-size: 13px;"><b>03</b><i></i>Kind words</div>
<h2 class="d" style="margin: 0; font-size: 30px; line-height: 1.04; letter-spacing: -0.03em; text-wrap: balance;">From people who've had us over.</h2>
<div style="position: relative; overflow: hidden; background: #1C1410; color: #FAF6F0; border-radius: 14px; padding: 22px; display: flex; justify-content: space-between; align-items: center;">
<div style="position: absolute; right: -50px; top: -50px; width: 160px; height: 160px; border-radius: 50%; background: radial-gradient(circle, rgba(224,138,94,0.35), rgba(224,138,94,0) 70%);"></div>
<div style="position: relative; display: flex; align-items: center; gap: 12px;"><span style="width: 40px; height: 40px; border-radius: 50%; background: #FAF6F0; color: #B5532C; display: flex; align-items: center; justify-content: center;">{ic('shield',20)}</span><div><div style="font-size: 14px; font-weight: 600;">[Rating source]</div><div style="display: flex; align-items: center; gap: 6px; margin-top: 4px;">{stars(12,'#E08A5E')}<span style="font-size: 10px; font-weight: 600; letter-spacing: 0.06em; color: #D9C9B8;">VERIFIED</span></div><div style="font-size: 12px; color: #D9C9B8; margin-top: 4px;">[N] reviews · [date]</div></div></div>
<div class="d" style="position: relative; font-size: 44px; line-height: 1; letter-spacing: -0.04em;">[4.x]</div>
</div>
<div class="card" style="padding: 22px; display: flex; flex-direction: column; gap: 14px;">
<div style="display: flex; justify-content: space-between; align-items: center;"><span style="font-size: 13px; color: #6B5A4C;">[Rating source] review</span>{stars(14)}</div>
{QUOTE(28)}
<p style="margin: 0; font-size: 17px; line-height: 1.55;">[Owner-supplied review, with permission.]</p>
<div style="border-top: 1px solid #EADFD1; padding-top: 14px; display: flex; align-items: center; justify-content: space-between;"><span style="display: flex; align-items: center; gap: 10px;"><span class="av" style="width: 36px; height: 36px; font-size: 13px;">[N]</span><strong style="font-size: 14px;">[Name]</strong></span><span class="pill" style="padding: 4px 10px; font-size: 12px;">Wedding</span></div>
</div>
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="display: flex; gap: 8px;"><span class="dot" style="width: 22px; border-radius: 4px; background: #1C1410;"></span><span class="dot"></span><span class="dot"></span></div>
<div style="display: flex; gap: 8px;"><button type="button" class="ctl" aria-label="Previous review" style="width: 44px; height: 44px; justify-content: center; border: 1.5px solid #1C1410; background: transparent; color: #1C1410;">{ic('arrowl',17)}</button><button type="button" class="ctl" aria-label="Next review" style="width: 44px; height: 44px; justify-content: center; background: #1C1410; color: #FAF6F0;">{ic('arrow',17)}</button></div>
</div>
</div>''')
    chk = lambda t: f'<span style="display: flex; align-items: center; gap: 8px;"><span style="color: #E08A5E; display: flex;">{ic("check",15,2.2)}</span>{t}</span>'
    h.append(f'''<div style="position: relative; background: #1C1410; color: #FAF6F0; overflow: hidden;">
<img src="{blob('cta')}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.8; object-position: 50% 18%; filter: blur(6px); transform: scale(1.06);">
<div style="position: absolute; inset: 0; background: rgba(20,12,8,0.66);"></div>
<div style="position: absolute; left: -140px; bottom: -160px; width: 420px; height: 420px; border-radius: 50%; background: radial-gradient(circle, rgba(181,83,44,0.4), rgba(181,83,44,0) 68%);"></div>
<div style="position: relative; padding: 48px 20px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 16px;">
<div class="cue dk" style="font-size: 13px;"><b>04</b><i></i>Get in touch</div>
<h2 class="d" style="margin: 0; font-size: 44px; line-height: 1.02; letter-spacing: -0.035em;">Let's put coffee on the {swash('guest list.')}</h2>
<p style="margin: 0; font-size: 15px; line-height: 1.5; color: #E4D3C1; text-wrap: balance;">Share the date, headcount and location. We'll send a quote.</p>
<a href="#" class="btn bp" style="align-self: stretch; margin-top: 8px; padding: 17px; font-size: 16px;">Get a quote {ic('cal',17)}</a>
<div style="font-size: 13px; color: rgba(250,246,240,0.78);">We reply within [owner to confirm]</div>
<div style="display: flex; flex-direction: column; align-items: flex-start; gap: 8px; font-size: 14px; color: #EADBCB; margin-top: 4px;">{chk('We set up, serve and clean up')}{chk('Hot or iced, dairy-free milks')}{chk('Serving [service area]')}</div>
</div>
</div>''')
    a = lambda t: f'<a href="#" style="text-decoration: none; font-size: 15px; font-weight: 500;">{t}</a>'
    h.append(f'''<div style="flex-grow: 1; position: relative; overflow: hidden;">
<div style="padding: 48px 20px 0; display: flex; flex-direction: column; gap: 28px;">
<div class="d" style="font-size: 28px; letter-spacing: -0.03em;">Fellowship<span style="color: #B5532C;">.</span></div>
<p style="margin: 0; font-size: 15px; line-height: 1.6; color: #4E3F34;">Coffee is better shared. That's the whole idea behind the name.</p>
<div style="display: flex; gap: 10px; align-items: center;"><a href="#" class="btn bp" style="padding: 12px 20px; font-size: 14px;">Get a quote {ic('cal',15)}</a><a href="#" class="soc" aria-label="Instagram" style="width: 40px; height: 40px;">{ic('ig',18)}</a><a href="#" class="soc" aria-label="Facebook" style="width: 40px; height: 40px;">{ic('fb',18)}</a></div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 32px;">
<div style="display: flex; flex-direction: column; gap: 10px;"><span style="font-size: 12px; font-weight: 600; letter-spacing: 0.04em; color: #8A7867;">SERVICES</span>{a('Weddings')}{a('Corporate')}{a('Celebrations')}</div>
<div style="display: flex; flex-direction: column; gap: 10px;"><span style="font-size: 12px; font-weight: 600; letter-spacing: 0.04em; color: #8A7867;">RESOURCES</span>{a('Menu')}{a('FAQs')}{a('The Coffee Shop')}{a('About')}</div>
</div>
<div style="display: flex; flex-direction: column; gap: 10px; font-size: 15px; color: #4E3F34;"><span style="font-size: 12px; font-weight: 600; letter-spacing: 0.04em; color: #8A7867;">VISIT THE CAFÉ</span><span style="display: flex; gap: 8px;"><span style="color: #B5532C;">{ic('pin',17)}</span>3434 FM 1092 Rd #350, Missouri City, TX 77459</span><span style="display: flex; gap: 8px; align-items: center;"><span style="color: #B5532C; display: flex;">{ic('clock',17)}</span>[Hours]</span></div>
<div class="card" style="padding: 20px; display: flex; flex-direction: column; gap: 14px;">
<div style="display: flex; align-items: center; gap: 12px;"><span style="width: 42px; height: 42px; border-radius: 50%; border: 1.5px solid #E6D9C8; color: #B5532C; display: flex; align-items: center; justify-content: center;">{ic('mail',20)}</span><div class="d" style="font-size: 19px; letter-spacing: -0.02em;">Coffee news, now and then</div></div>
<div style="display: flex; gap: 8px;"><label style="flex-grow: 1; display: flex;"><span style="position: absolute; left: -9999px;">Email</span><input type="email" placeholder="Your email" style="width: 100%; border: 1px solid #E6D9C8; background: #FAF6F0; border-radius: 999px; padding: 12px 16px; font: 15px 'Figtree', sans-serif;"></label><button type="button" class="ctl bd" style="padding: 0 18px; font-size: 14px;">Sign up</button></div>
</div>
<div style="border-top: 1px solid #E6D9C8; padding-top: 16px; display: flex; justify-content: space-between; font-size: 13px; color: #6B5A4C;"><span>© 2026 Fellowship Coffee Co.</span><a href="#" style="color: #6B5A4C;">Privacy</a></div>
</div>
<div class="d" aria-hidden="true" style="margin: 20px 0 0 18px; font-size: 70px; line-height: 1; letter-spacing: -0.055em; color: #EFE4D6; white-space: nowrap; height: 66px; overflow: hidden;">Fellowship<span style="color: #EBCDBC;">.</span></div>
</div>''')
    return page('Fellowship home, phone v6', 390, '\n\n'.join(h))

if __name__ == '__main__':
    open(f'{SP}/style/project/Home-Desktop.dc.html', 'w').write(desktop())
    open(f'{SP}/style/project/Home-Phone.dc.html', 'w').write(phone())
    print('generated')
