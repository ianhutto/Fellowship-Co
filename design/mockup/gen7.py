# v7 — Night Owl architecture + component inventory, Fellowship's REAL brand styling
# (from fellowshipcoffeetx.com: black/white + stone #F0F0EA, Inter Tight + Montserrat caps,
#  square black buttons, their wordmark logo, their own cart + café photography)
import sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/8a7925b3-9b44-5f65-9407-753277b31ecf/scratchpad/render')
from gen import P, ic, STAR, QUOTE
SP = '/tmp/claude-0/-home-claude/8a7925b3-9b44-5f65-9407-753277b31ecf/scratchpad'
A = {
 'cart_best': 'c6b16c4aec09a8396b03fd91cd0f6ff5', 'cart_rancilio': 'a8c47a9a9d10ab2bebb8bc4d2dec3b83',
 'cart_indoor': '283b31919141597bbce668aa3053eb68', 'cart_barista': 'e24b2c8b36c5fd2f96ee1914285d4527',
 'onsite': 'b9d6d91b19f361790b88650222611a7c', 'cup_hand': '66ee383ffba160443b0225267afaba2d',
 'f18': 'a37a2b4cbc81736d14fc887d0f7c3172', 'f20': 'bc72c6c4b5defcd8d5a81ca544ac5ee9',
 'f41': '808d63fc4895001e45424e0043231cf8', 'f65': 'ac119f7a76ee7fd4ff6c6eba1381f140',
 'f68': '82345e7407a7852dd150254340314d34', 'f72': '45d33c685246729de6963134d9142801',
 'f93': '326277ed1ceeab8be0c5d0bf879d58aa', 'logo_k': '8f6cd4f5ffddb8a9a6042d340919b243',
 'logo_w': '9b5ffc86baf980c18e28e3e74a460d71'}
def u(k): return f'/_blob/{A[k]}'

INK, STONE, LINE, MUTED, LEATHER = '#111111', '#F0F0EA', '#E2DFD6', '#57534B', '#7A4B2C'

def stars(size=15, color=LEATHER):
    one = f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="{color}" aria-hidden="true">{STAR}</svg>'
    return f'<span class="stars" role="img" aria-label="5 out of 5 stars">{one*5}</span>'
def logo(h, white=False, extra=''):
    return f'<img src="{u("logo_w" if white else "logo_k")}" alt="Fellowship Coffee Co." style="height: {h}px; width: auto; display: block;{extra}">'
def cue(n, label, dark=False):
    return f'<div class="cue{" dk" if dark else ""}"><b>{n}</b><i></i>{label}</div>'
def btn(label, kind='bk', icon='cal', pad='17px 26px', size=12):
    return f'<a href="#" class="b {kind}" style="padding: {pad}; font-size: {size}px;">{label} {ic(icon,16,1.8)}</a>'

CSS = f"""
body{{margin:0;background:#FFFFFF;font-family:'Inter Tight',system-ui,sans-serif;color:{INK}}}
a{{color:{INK}}}
.h{{font-family:'Inter Tight',sans-serif;font-weight:500;letter-spacing:-0.03em}}
.h em{{font-style:italic;font-weight:400;letter-spacing:-0.025em}}
.m{{font-family:'Montserrat',sans-serif}}
.lab{{font-family:'Montserrat',sans-serif;font-weight:600;font-size:11px;letter-spacing:.2em;text-transform:uppercase}}
.ic{{display:inline-block;flex-shrink:0}}
.b{{display:inline-flex;align-items:center;justify-content:center;gap:10px;font-family:'Montserrat',sans-serif;font-weight:600;letter-spacing:.14em;text-transform:uppercase;text-decoration:none;border-radius:2px;white-space:nowrap}}
.bk{{background:{INK};color:#FFFFFF}}
.bw{{background:#FFFFFF;color:{INK}}}
.bo{{border:1px solid {INK};color:{INK}}}
.bol{{border:1px solid rgba(255,255,255,.6);color:#FFFFFF}}
.cue{{display:flex;align-items:center;gap:12px;font-family:'Montserrat',sans-serif;font-weight:600;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:{INK}}}
.cue b{{color:{INK};font-weight:700}}.cue i{{display:block;width:32px;height:1px;background:{INK}}}
.cue.dk{{color:#FFFFFF}}.cue.dk b{{color:#FFFFFF}}.cue.dk i{{background:rgba(255,255,255,.6)}}
.card{{background:#FFFFFF;border:1px solid {LINE};border-radius:8px}}
.badge{{position:absolute;display:flex;align-items:center;justify-content:center;border-radius:50%;background:#FFFFFF;color:{INK};box-shadow:0 6px 18px rgba(17,17,17,.18)}}
.tile{{display:flex;align-items:center;justify-content:center;border-radius:6px;background:{STONE};color:{INK};flex-shrink:0}}
.lnk{{display:inline-flex;align-items:center;gap:8px;font-family:'Montserrat',sans-serif;font-weight:600;font-size:12px;letter-spacing:.14em;text-transform:uppercase;text-decoration:none;color:{INK}}}
.stars{{display:inline-flex;gap:2px}}
.av{{display:flex;align-items:center;justify-content:center;border-radius:50%;background:{STONE};color:{MUTED};font-weight:600;flex-shrink:0}}
.pill{{display:inline-flex;align-items:center;border:1px solid {LINE};border-radius:999px;color:{MUTED};font-family:'Montserrat',sans-serif;font-weight:500;letter-spacing:.04em}}
.soc{{display:flex;align-items:center;justify-content:center;border-radius:50%;border:1px solid #CFCBC0;color:{INK}}}
.dot{{width:8px;height:8px;border-radius:50%;background:#D4D0C6}}
.mq{{display:flex;align-items:center;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent);mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent)}}
.mq span.n{{white-space:nowrap;color:#7C776C;font-family:'Inter Tight',sans-serif;font-weight:600;letter-spacing:-0.02em}}
.ctl{{display:inline-flex;align-items:center;gap:6px;border-radius:999px;border:none;cursor:pointer;font-family:'Montserrat',sans-serif;font-weight:600;letter-spacing:.08em;text-transform:uppercase}}
.chk{{display:flex;align-items:center;gap:10px}}
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
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:ital,wght@0,300..700;1,400..600&amp;family=Montserrat:wght@400..700&amp;display=swap" rel="stylesheet">
<style>{CSS}</style>
</helmet>
<div style="width: {width}px; height: __H__px; box-sizing: border-box; background: #FFFFFF; color: {INK}; display: flex; flex-direction: column; overflow: hidden;">
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

# ---------------- shared copy (COPY.md v1.1, verbatim) ----------------
H1 = 'Your event, with a coffee shop <em>in the room.</em>'
HERO_SUB = 'A full espresso bar and friendly baristas for weddings, offices and celebrations, from our café in Missouri City. We set up, serve and clean up. You enjoy the party.'
WWD_BODY = 'Espresso, lattes, chai, matcha and hot cocoa, made to order by our baristas. Hot or iced, with dairy-free milks. We bring the bar, the beans and the people who know what to do with them.'
CARDS = [
 ('f93', 'rings', 'Weddings', 'Cocktail hour, with a latte in hand.', 'A coffee bar gives guests something to gather around while the photos wrap up.', 'Plan your wedding coffee', 'The Fellowship coffee cart set up with espresso machine and syrups', '50% 72%'),
 ('cart_indoor', 'brief', 'Corporate', 'The break room, upgraded.', 'Americanos, cappuccinos and chai for your team, right where they work.', 'Book for your team', 'Fellowship coffee cart in a glass office lobby', '52% 82%'),
 ('cart_best', 'party', 'Celebrations', 'Showers, birthdays and every excuse in between.', "If the cart fits, we'll be there. And the kids get their own hot cocoa bar.", 'Plan your party', 'Barista making drinks at the Fellowship cart at an outdoor event', '50% 18%'),
]
PRESS = ['Community Impact', 'WhatNow Houston']
DIFF_BODY = 'Fellowship started as a coffee cart in 2021 and opened a café in Missouri City in 2024. Every event gets the same coffee and care as the shop.'
BENEFITS = ['We set up, serve and clean up', 'Hot or iced, with dairy-free milks', 'Serving [service area]']
SEP = '<span style="flex-shrink: 0; display: inline-block; width: 5px; height: 5px; border-radius: 50%; background: #B9B4A8;"></span>'

# =============================== DESKTOP ===============================
def desktop():
    W = 1200; h = []
    h.append(f'''<!-- 1 Utility bar -->
<div style="background: {INK}; color: #EDEBE4;">
<div class="m" style="width: {W}px; margin: 0 auto; height: 40px; display: flex; align-items: center; justify-content: space-between; font-size: 12px; font-weight: 500; letter-spacing: 0.04em;">
<span style="display: flex; align-items: center; gap: 8px;">{ic('clock',14)} Café open today until [hours]</span>
<div style="display: flex; gap: 28px;"><span style="display: flex; align-items: center; gap: 7px;">{ic('pin',14)} 3434 FM 1092, Missouri City</span><a href="#" style="color: #FFFFFF; text-decoration: none; font-weight: 600; display: flex; align-items: center; gap: 7px;">{ic('phone',14)} (832) 427-7363</a></div>
</div>
</div>''')
    h.append(f'''<!-- Header -->
<div style="background: #FFFFFF; border-bottom: 1px solid {LINE};">
<div style="width: {W}px; margin: 0 auto; height: 84px; display: flex; align-items: center; justify-content: space-between;">
<a href="#" aria-label="Fellowship Coffee Co. home">{logo(30)}</a>
<div class="m" style="display: flex; align-items: center; gap: 36px; font-size: 14px; font-weight: 500;">
<a href="#" style="text-decoration: none;">About</a>
<a href="#" style="text-decoration: none; display: flex; align-items: center; gap: 4px;">Services {ic('chev',15,1.8)}</a>
<a href="#" style="text-decoration: none; display: flex; align-items: center; gap: 4px;">Resources {ic('chev',15,1.8)}</a>
{btn('Get a quote','bk','cal','14px 20px',11)}
</div>
</div>
</div>''')
    h.append(f'''<!-- 2 Hero: the cart, full bleed -->
<div style="position: relative; height: 760px; background: #0E0E0D; overflow: hidden; color: #FFFFFF;">
<img src="{u('cart_rancilio')}" alt="The Fellowship Coffee Co. cart set up at a venue, with espresso machine, grinder and syrups" style="position: absolute; top: 0; left: 16%; width: 84%; height: 100%; object-fit: cover; object-position: 50% 88%; -webkit-mask-image: linear-gradient(90deg, transparent 0%, #000 40%); mask-image: linear-gradient(90deg, transparent 0%, #000 40%);">
<div style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.8) 32%, rgba(0,0,0,0.35) 46%, rgba(0,0,0,0) 58%);"></div>
<div style="position: relative; width: {W}px; height: 100%; margin: 0 auto; box-sizing: border-box; padding: 80px 0 48px; display: flex; flex-direction: column; justify-content: center; gap: 20px;">
<div class="lab" style="display: flex; align-items: center; gap: 10px; color: rgba(255,255,255,0.85);">Mobile espresso bar {SEP} Houston</div>
<h1 class="h" style="margin: 0; font-size: 80px; line-height: 0.98; letter-spacing: -0.028em; max-width: 640px; text-wrap: balance;">{H1}</h1>
<p style="margin: 4px 0 0; font-size: 19px; line-height: 1.55; max-width: 480px; color: #F0EEE8;">{HERO_SUB}</p>
<div style="display: flex; gap: 14px; align-items: center; margin-top: 14px;">
{btn('Get a quote','bw','cal','19px 28px',12)}
{btn('See the menu','bol','arrow','18px 26px',12)}
</div>
</div>
<button type="button" class="ctl" aria-label="Pause background video" style="position: absolute; right: 24px; bottom: 24px; background: rgba(0,0,0,0.45); color: #FFFFFF; padding: 9px 14px; font-size: 11px;">{ic('pause',13,2.2)} Pause</button>
</div>''')
    names = ''.join(f'<span class="n" style="font-size: 26px;">{n}</span>{SEP}' for n in PRESS*4)
    h.append(f'''<!-- 3 Trust strip -->
<div style="background: {STONE};">
<div style="width: {W}px; margin: 0 auto; padding: 48px 0; display: flex; flex-direction: column; align-items: center; gap: 24px;">
<span class="lab" style="color: {MUTED};">Serving Houston since 2021 · As featured in [confirm]</span>
<div class="m" style="display: flex; align-items: center; justify-content: center; gap: 28px;">{SEP.join(f'<a href="#" style="font-size: 15px; font-weight: 600; letter-spacing: 0.16em; text-transform: uppercase; color: {INK}; text-decoration: none;">{n}</a>' for n in PRESS)}</div>
</div>
</div>''')
    h.append(f'''<!-- 4 What we do -->
<div style="width: {W}px; margin: 0 auto; padding: 80px 0; display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 24px; align-items: center;">
<div style="grid-column: span 5; display: flex; flex-direction: column; gap: 18px; padding-right: 32px;">
{cue('01','What we do')}
<h2 class="h" style="margin: 0; font-size: 56px; line-height: 1.02;">A coffee shop that shows up.</h2>
<p style="margin: 0; font-size: 18px; line-height: 1.65; color: {MUTED};">{WWD_BODY}</p>
<div style="margin-top: 10px;">{btn('See the menu','bo','arrow','16px 24px',12)}</div>
</div>
<div style="grid-column: span 7; position: relative; height: 440px; border-radius: 8px; overflow: hidden; background: #E9E6DE;">
<img src="{u('f65')}" alt="A Fellowship barista pouring a latte at the cart" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 12%;">
<div class="m" style="position: absolute; left: 24px; top: 24px; display: flex; align-items: center; gap: 10px; background: rgba(255,255,255,0.95); border-radius: 999px; padding: 8px 18px 8px 8px; font-size: 12px; font-weight: 600; letter-spacing: 0.04em;"><span class="tile" style="width: 32px; height: 32px; border-radius: 50%;">{ic('cup',17)}</span>Hot or iced · dairy-free milks</div>
</div>
</div>''')
    cards = ''
    for key, icon, label, title, body, link, alt, pos in CARDS:
        cards += f'''<div class="card" style="overflow: hidden; display: flex; flex-direction: column;">
<div style="position: relative; height: 400px; background: #E9E6DE;"><img src="{u(key)}" alt="{alt}" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: {pos};"><div class="badge" style="left: 24px; bottom: -24px; width: 50px; height: 50px;">{ic(icon,22,1.6)}</div></div>
<div style="padding: 44px 28px 28px; display: flex; flex-direction: column; gap: 12px; flex-grow: 1;">
<div class="lab" style="color: {MUTED};">{label}</div>
<h3 class="h" style="margin: 0; font-size: 27px; line-height: 1.1; letter-spacing: -0.03em; text-wrap: balance;">{title}</h3>
<p style="margin: 0; font-size: 16px; line-height: 1.6; color: {MUTED}; flex-grow: 1;">{body}</p>
<div style="border-top: 1px solid {LINE}; padding-top: 18px; margin-top: 10px;"><a href="#" class="lnk">{link} {ic('arrow',15,1.8)}</a></div>
</div>
</div>
'''
    def stat(icon, label, fig, dark=False, sub=''):
        bg = f'background: {INK}; color: #FFFFFF; border-color: {INK};' if dark else ''
        t = ' background: rgba(255,255,255,0.1); color: #FFFFFF;' if dark else ''
        lc = '#D8D4CA' if dark else MUTED
        ring = '1px solid rgba(255,255,255,0.7)' if dark else f'1px solid {INK}'
        return f'''<div class="card" style="{bg} padding: 32px; min-height: 200px; display: flex; flex-direction: column; box-sizing: border-box;">
<span style="width: 40px; height: 40px; border-radius: 50%; border: {ring}; display: flex; align-items: center; justify-content: center;">{ic(icon,19,1.6)}</span>
<div class="h" style="font-size: 64px; line-height: 1; letter-spacing: -0.03em; margin-top: 28px;">{fig}</div>
<div style="font-size: 14px; line-height: 1.45; color: {lc}; margin-top: 10px;">{label}{sub}</div>
</div>'''
    h.append(f'''<!-- 5+6 Cards, difference band, stat tiles (one washed section, as on Night Owl) -->
<div style="background: {STONE};">
<div style="width: {W}px; margin: 0 auto; padding: 80px 0; display: flex; flex-direction: column; gap: 24px;">
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px;">
{cards}</div>
<div style="position: relative; border-radius: 8px; overflow: hidden; background: {INK}; color: #FFFFFF; padding: 72px 64px; margin-top: 24px; display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 24px; align-items: end;">
<img src="{u('f68')}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 60% 30%;">
<div style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(0,0,0,0.78) 0%, rgba(0,0,0,0.55) 55%, rgba(0,0,0,0.5) 100%);"></div>
<div style="position: relative; grid-column: span 7; display: flex; flex-direction: column; gap: 20px;">
{cue('02','Why Fellowship',True)}
<h2 class="h" style="margin: 0; font-size: 66px; line-height: 1.02;">A real café,<br><em>on wheels.</em></h2>
</div>
<div style="position: relative; grid-column: span 5; display: flex; flex-direction: column; gap: 22px; align-items: flex-start;">
<p style="margin: 0; font-size: 18px; line-height: 1.6; color: #E9E6DE;">{DIFF_BODY}</p>
{btn('Get a quote','bw','cal','17px 26px',12)}
</div>
</div>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; margin-top: 24px;">
{stat('cal','Serving Houston events since','2021')}
{stat('tag','Mobile bookings from','[$X]',True,'<br><span style="font-size: 13px; color: #A9A499;">Price: owner to confirm</span>')}
{stat('store','Our Missouri City café opened','2024')}
</div>
</div>
</div>''')
    def rcard(ev):
        return f'''<div class="card" style="padding: 28px; display: flex; flex-direction: column; gap: 18px; box-sizing: border-box;">
<div style="display: flex; justify-content: space-between; align-items: center;"><span class="m" style="display: flex; align-items: center; gap: 8px; font-size: 12px; font-weight: 500; color: {MUTED};"><span class="av" style="width: 26px; height: 26px;">{ic('shield',14,1.7)}</span>[Rating source] review</span>{stars(14)}</div>
<div style="margin-top: 6px; opacity: 0.9;">{QUOTE(28).replace('#B5532C', INK)}</div>
<p style="margin: 0; font-size: 19px; line-height: 1.55; flex-grow: 1;">[Owner-supplied review, with permission.]</p>
<div style="border-top: 1px solid {LINE}; padding-top: 18px; display: flex; align-items: center; justify-content: space-between;"><span style="display: flex; align-items: center; gap: 12px;"><span class="av" style="width: 40px; height: 40px; font-size: 14px;">[N]</span><strong style="font-size: 15px; font-weight: 600;">[Name]</strong></span><span class="pill" style="padding: 5px 12px; font-size: 12px;">{ev}</span></div>
</div>'''
    h.append(f'''<!-- 7 Reviews -->
<div style="width: {W}px; margin: 0 auto; padding: 80px 0; display: flex; flex-direction: column; gap: 36px;">
<div style="display: flex; justify-content: space-between; align-items: flex-end;">
<div style="display: flex; flex-direction: column; gap: 18px;">{cue('03','Kind words')}
<h2 class="h" style="margin: 0; font-size: 56px; line-height: 1.02;">From people who've had us over.</h2></div>
<div style="display: flex; gap: 10px;">
<button type="button" class="ctl" aria-label="Previous reviews" style="width: 48px; height: 48px; justify-content: center; border: 1px solid {INK}; background: transparent; color: {INK};">{ic('arrowl',18)}</button>
<button type="button" class="ctl" aria-label="Next reviews" style="width: 48px; height: 48px; justify-content: center; background: {INK}; color: #FFFFFF;">{ic('arrow',18)}</button>
</div>
</div>
<div style="display: grid; grid-template-columns: 1fr 1.4fr 1.4fr; gap: 24px;">
<div style="position: relative; overflow: hidden; background: {STONE}; border-radius: 8px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;">
<div style="display: flex; align-items: center; gap: 12px;"><span style="width: 44px; height: 44px; border-radius: 50%; background: #FFFFFF; color: {INK}; display: flex; align-items: center; justify-content: center;">{ic('shield',21,1.6)}</span><div><div style="font-size: 16px; font-weight: 600;">[Rating source]</div><div style="display: flex; align-items: center; gap: 8px; margin-top: 4px;">{stars(13)}<span class="lab" style="font-size: 10px; color: {MUTED};">Verified</span></div></div></div>
<div style="border-top: 1px solid #DAD6CB; padding-top: 20px;"><div class="h" style="font-size: 72px; line-height: 1; letter-spacing: -0.045em;">[4.x]</div><div style="font-size: 15px; color: {MUTED}; margin-top: 8px;">[N] reviews · as of [date]</div></div>
</div>
{rcard('Wedding')}
{rcard('Corporate')}
</div>
<div style="display: flex; justify-content: center; align-items: center; gap: 8px;"><span class="dot" style="width: 24px; border-radius: 4px; background: {INK};"></span><span class="dot"></span><span class="dot"></span></div>
</div>''')
    chks = ''.join(f'<span class="chk"><span style="color: #FFFFFF; display: flex;">{ic("check",17,2)}</span>{b}</span>' for b in BENEFITS)
    h.append(f'''<!-- 8 Closing CTA -->
<div style="position: relative; background: {INK}; color: #FFFFFF; overflow: hidden;">
<div style="position: absolute; inset: 0; background: #0E0E0E;"></div>
<div style="position: absolute; inset: 0; background: radial-gradient(55% 60% at 50% 45%, rgba(255,255,255,0.07), rgba(255,255,255,0) 70%);"></div>
<div style="position: absolute; left: -180px; bottom: -260px; width: 640px; height: 640px; border-radius: 50%; background: radial-gradient(closest-side, rgba(240,240,234,0.07), rgba(240,240,234,0));"></div>
<div style="position: absolute; right: -160px; top: -240px; width: 600px; height: 600px; border-radius: 50%; background: radial-gradient(closest-side, rgba(217,196,163,0.08), rgba(217,196,163,0));"></div>
<div style="position: relative; width: {W}px; margin: 0 auto; padding: 96px 0; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 22px;">
{cue('04','Get in touch',True)}
<h2 class="h" style="margin: 0; font-size: 76px; line-height: 1; max-width: 880px; text-wrap: balance;">Let's put coffee on the <em>guest list.</em></h2>
<p style="margin: 0; font-size: 19px; line-height: 1.5; color: #E9E6DE;">Share the date, headcount and location. We'll send a quote.</p>
<div style="margin-top: 10px;">{btn('Get a quote','bw','cal','20px 32px',12)}</div>
<div class="m" style="font-size: 12px; font-weight: 500; letter-spacing: 0.06em; color: rgba(255,255,255,0.8);">We reply within [owner to confirm]</div>
<div style="display: flex; gap: 32px; margin-top: 14px; font-size: 15px; color: #F0EEE8;">{chks}</div>
</div>
</div>''')
    col = lambda title, items: f'<div style="display: flex; flex-direction: column; gap: 14px;"><span class="lab" style="color: #8A857B;">{title}</span>{items}</div>'
    a = lambda t: f'<a href="#" style="text-decoration: none; font-size: 15px; font-weight: 500;">{t}</a>'
    h.append(f'''<!-- 9 Footer -->
<div style="flex-grow: 1; background: {STONE}; position: relative; overflow: hidden;">
<div style="width: {W}px; margin: 0 auto; padding: 56px 0 0; display: flex; flex-direction: column; gap: 48px;">
<div style="display: flex; justify-content: space-between;">
<div style="display: flex; flex-direction: column; gap: 20px; max-width: 300px;">
<div>{logo(34)}</div>
<p style="margin: 0; font-size: 16px; line-height: 1.6; color: {MUTED};">Coffee is better shared. That's the whole idea behind the name.</p>
<div>{btn('Get a quote','bk','cal','14px 20px',11)}</div>
<div style="display: flex; gap: 10px;"><a href="#" class="soc" aria-label="Instagram @fellowshipcoffee.co" style="width: 40px; height: 40px;">{ic('ig',18,1.6)}</a><a href="#" class="soc" aria-label="Facebook" style="width: 40px; height: 40px;">{ic('fb',18,1.6)}</a></div>
</div>
<div style="display: flex; gap: 80px;">
{col('Company', a('About')+a('The Coffee Shop'))}
{col('Services', a('Weddings')+a('Corporate')+a('Celebrations'))}
{col('Resources', a('Menu')+a('FAQs')+a('Get a quote'))}
{col('Visit the café', f'<span style="display: flex; gap: 8px; color: {MUTED}; font-size: 15px; line-height: 1.5;"><span style="margin-top: 1px;">{ic("pin",16)}</span>3434 FM 1092 Rd #350<br>Missouri City, TX 77459</span><span style="display: flex; gap: 8px; align-items: center; color: {MUTED}; font-size: 15px;">{ic("clock",16)}[Hours]</span><span style="display: flex; gap: 8px; align-items: center; font-size: 15px; font-weight: 600;">{ic("phone",16)}(832) 427-7363</span>')}
</div>
</div>
<div class="card" style="padding: 20px 20px 20px 24px; display: flex; align-items: center; justify-content: space-between; border-color: #E2DFD6;">
<div style="display: flex; align-items: center; gap: 16px;"><span style="width: 48px; height: 48px; border-radius: 50%; border: 1px solid {LINE}; display: flex; align-items: center; justify-content: center;">{ic('mail',21,1.6)}</span><div class="h" style="font-size: 21px; letter-spacing: -0.02em;">Coffee news and event ideas, now and then.</div></div>
<div style="display: flex; gap: 8px; width: 430px;"><label style="flex-grow: 1; display: flex;"><span style="position: absolute; left: -9999px;">Email</span><input type="email" placeholder="Your email" style="width: 100%; border: 1px solid {LINE}; background: #FAFAF7; border-radius: 2px; padding: 14px 16px; font: 15px 'Inter Tight', sans-serif;"></label><button type="button" class="b bk" style="border: none; padding: 0 22px; font-size: 11px; cursor: pointer;">Sign up</button></div>
</div>
<div class="m" style="display: flex; justify-content: space-between; border-top: 1px solid #DAD6CB; padding-top: 24px; font-size: 12px; color: {MUTED};">
<span>© 2026 Fellowship Coffee Co.</span><span style="display: flex; gap: 24px;"><a href="#" style="color: {MUTED};">Privacy</a><a href="#" style="color: {MUTED};">Instagram @fellowshipcoffee.co</a></span>
</div>
</div>
<div aria-hidden="true" style="width: {W}px; margin: 40px auto 0; height: 150px; overflow: hidden; opacity: 0.07;"><img src="{u('logo_k')}" alt="" style="width: 100%; height: auto; display: block;"></div>
</div>''')
    return page('Fellowship home, desktop v7', 1440, '\n\n'.join(h))

# =============================== PHONE ===============================
def phone():
    h = []
    h.append(f'''<div class="m" style="background: {INK}; color: #EDEBE4; height: 36px; display: flex; align-items: center; justify-content: center; gap: 10px; font-size: 11px; font-weight: 500; letter-spacing: 0.03em;">
<span style="display: flex; align-items: center; gap: 6px;">{ic('clock',13)} Open until [hours]</span><span style="opacity: 0.4;">·</span><a href="#" style="color: #FFFFFF; text-decoration: none; font-weight: 600; display: flex; align-items: center; gap: 6px;">{ic('phone',13)} (832) 427-7363</a>
</div>
<div style="height: 64px; box-sizing: border-box; padding: 0 20px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid {LINE};">
{logo(21)}
<div style="display: flex; align-items: center; gap: 8px;">
<a href="#" class="b bk" style="padding: 12px 13px; font-size: 10px; gap: 7px;">Quote {ic('cal',14,1.8)}</a>
<button type="button" aria-label="Open menu" style="width: 44px; height: 44px; border-radius: 2px; border: 1px solid {INK}; background: transparent; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 5px; cursor: pointer;"><span style="width: 16px; height: 1.5px; background: {INK};"></span><span style="width: 16px; height: 1.5px; background: {INK};"></span></button>
</div>
</div>''')
    h.append(f'''<div style="position: relative; background: #0E0E0D; color: #FFFFFF;">
<div style="position: relative; height: 470px; overflow: hidden;"><img src="{u('cart_best')}" alt="The Fellowship Coffee Co. cart at an event, with a barista making drinks" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 55%;"><div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(14,14,13,0) 70%, rgba(14,14,13,1) 100%);"></div>
<button type="button" class="ctl" aria-label="Pause background video" style="position: absolute; right: 16px; top: 14px; background: rgba(0,0,0,0.45); color: #FFFFFF; padding: 7px 12px; font-size: 10px;">{ic('pause',12,2.2)} Pause</button></div>
<div style="position: relative; box-sizing: border-box; padding: 8px 20px 40px; display: flex; flex-direction: column; gap: 16px;">
<div class="lab" style="display: flex; align-items: center; gap: 8px; color: rgba(255,255,255,0.85); font-size: 10px;">Mobile espresso bar {SEP} Houston</div>
<h1 class="h" style="margin: 0; font-size: 44px; line-height: 1; text-wrap: balance;">{H1}</h1>
<p style="margin: 0; font-size: 16px; line-height: 1.55; color: #E9E6DE;">A full espresso bar and friendly baristas for weddings, offices and celebrations. We set up, serve and clean up.</p>
{btn('Get a quote','bw','cal','18px',12)}
{btn('See the menu','bol','arrow','17px',12)}
</div>
</div>''')
    names = ''.join(f'<span class="n" style="font-size: 19px;">{n}</span>{SEP}' for n in PRESS*4)
    h.append(f'''<div style="background: {STONE}; padding: 48px 0; display: flex; flex-direction: column; align-items: center; gap: 18px;">
<span class="lab" style="color: {MUTED}; font-size: 10px; line-height: 1.9; text-align: center; padding: 0 20px;">Serving Houston since 2021<br>As featured in [confirm]</span>
<div class="m" style="display: flex; align-items: center; gap: 14px;">{SEP.join(f'<a href="#" style="font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: {INK}; text-decoration: none;">{n}</a>' for n in PRESS)}</div>
</div>''')
    h.append(f'''<div style="padding: 40px 20px; display: flex; flex-direction: column; gap: 16px;">
{cue('01','What we do')}
<h2 class="h" style="margin: 0; font-size: 38px; line-height: 1.04;">A coffee shop that shows up.</h2>
<p style="margin: 0; font-size: 16px; line-height: 1.65; color: {MUTED};">{WWD_BODY}</p>
<div style="position: relative; height: 280px; border-radius: 8px; overflow: hidden; margin-top: 8px; background: #E9E6DE;"><img src="{u('f65')}" alt="A Fellowship barista pouring a latte at the cart" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 62% 10%;"><div class="m" style="position: absolute; left: 12px; top: 12px; display: flex; align-items: center; gap: 8px; background: rgba(255,255,255,0.95); border-radius: 999px; padding: 6px 12px 6px 6px; font-size: 11px; font-weight: 600;"><span class="tile" style="width: 26px; height: 26px; border-radius: 50%;">{ic('cup',14)}</span>Hot or iced · dairy-free milks</div></div>
<div>{btn('See the menu','bo','arrow','15px 22px',11)}</div>
</div>''')
    cards = ''
    for key, icon, label, title, body, link, alt, pos in CARDS:
        if key == 'cart_best':  # phone hero already uses cart_best
            key, pos, alt = 'cart_barista', '50% 100%', 'Barista at the Fellowship cart with espresso machine and syrups'
        cards += f'''<div class="card" style="overflow: hidden;"><div style="position: relative; height: 340px; background: #E9E6DE;"><img src="{u(key)}" alt="{alt}" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: {pos};"><div class="badge" style="left: 18px; bottom: -22px; width: 46px; height: 46px;">{ic(icon,21,1.6)}</div></div>
<div style="padding: 36px 20px 22px; display: flex; flex-direction: column; gap: 10px;"><div class="lab" style="color: {MUTED}; font-size: 10px;">{label}</div><h3 class="h" style="margin: 0; font-size: 24px; line-height: 1.12; letter-spacing: -0.03em; text-wrap: balance;">{title}</h3><p style="margin: 0; font-size: 15px; line-height: 1.55; color: {MUTED};">{body}</p><div style="border-top: 1px solid {LINE}; padding-top: 14px; margin-top: 6px;"><a href="#" class="lnk" style="font-size: 11px;">{link} {ic('arrow',14,1.8)}</a></div></div></div>
'''
    def stat(icon, label, fig, dark=False, sub=''):
        bg = f'background: {INK}; color: #FFFFFF; border-color: {INK};' if dark else ''
        t = ' background: rgba(255,255,255,0.1); color: #FFFFFF;' if dark else ''
        ring = '1px solid rgba(255,255,255,0.7)' if dark else f'1px solid {INK}'
        return f'<div class="card" style="{bg} padding: 24px; display: flex; flex-direction: column;"><span style="width: 40px; height: 40px; flex-shrink: 0; border-radius: 50%; border: {ring}; display: flex; align-items: center; justify-content: center;">{ic(icon,19,1.6)}</span><div class="h" style="font-size: 52px; line-height: 1; letter-spacing: -0.03em; margin-top: 22px;">{fig}</div><div style="font-size: 14px; line-height: 1.4; margin-top: 8px; color: {"#D8D4CA" if dark else MUTED};">{label}{sub}</div></div>'
    h.append(f'''<div style="background: {STONE}; padding: 40px 20px; display: flex; flex-direction: column; gap: 20px;">
{cards}
<div style="position: relative; border-radius: 8px; overflow: hidden; background: {INK}; color: #FFFFFF; padding: 36px 24px; margin-top: 12px; display: flex; flex-direction: column; gap: 16px;">
<img src="{u('f68')}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 55% 25%;">
<div style="position: absolute; inset: 0; background: rgba(0,0,0,0.62);"></div>
<div style="position: relative;">{cue('02','Why Fellowship',True)}</div>
<h2 class="h" style="position: relative; margin: 0; font-size: 42px; line-height: 1.04;">A real café,<br><em>on wheels.</em></h2>
<p style="position: relative; margin: 0; font-size: 15px; line-height: 1.6; color: #E9E6DE;">{DIFF_BODY}</p>
<div style="position: relative; display: flex; flex-direction: column;">{btn('Get a quote','bw','cal','16px',12)}</div>
</div>
{stat('cal','Serving Houston events since','2021')}
{stat('tag','Mobile bookings from','[$X]',True,'<br><span style="font-size: 12px; color: #A9A499;">Price: owner to confirm</span>')}
{stat('store','Our Missouri City café opened','2024')}
</div>''')
    h.append(f'''<div style="padding: 40px 20px; display: flex; flex-direction: column; gap: 20px;">
{cue('03','Kind words')}
<h2 class="h" style="margin: 0; font-size: 32px; line-height: 1.06; text-wrap: balance;">From people who've had us over.</h2>
<div style="background: {STONE}; border-radius: 8px; padding: 22px; display: flex; justify-content: space-between; align-items: center;">
<div style="display: flex; align-items: center; gap: 12px;"><span style="width: 40px; height: 40px; border-radius: 50%; background: #FFFFFF; display: flex; align-items: center; justify-content: center;">{ic('shield',19,1.6)}</span><div><div style="font-size: 14px; font-weight: 600;">[Rating source]</div><div style="display: flex; align-items: center; gap: 6px; margin-top: 4px;">{stars(12)}<span class="lab" style="font-size: 9px; color: {MUTED};">Verified</span></div><div style="font-size: 12px; color: {MUTED}; margin-top: 4px;">[N] reviews · [date]</div></div></div>
<div class="h" style="font-size: 44px; line-height: 1; letter-spacing: -0.045em;">[4.x]</div>
</div>
<div class="card" style="padding: 22px; display: flex; flex-direction: column; gap: 14px;">
<div style="display: flex; justify-content: space-between; align-items: center;"><span class="m" style="font-size: 11px; font-weight: 500; color: {MUTED};">[Rating source] review</span>{stars(13)}</div>
<div>{QUOTE(24).replace('#B5532C', INK)}</div>
<p style="margin: 0; font-size: 17px; line-height: 1.55;">[Owner-supplied review, with permission.]</p>
<div style="border-top: 1px solid {LINE}; padding-top: 14px; display: flex; align-items: center; justify-content: space-between;"><span style="display: flex; align-items: center; gap: 10px;"><span class="av" style="width: 36px; height: 36px; font-size: 13px;">[N]</span><strong style="font-size: 14px; font-weight: 600;">[Name]</strong></span><span class="pill" style="padding: 4px 10px; font-size: 11px;">Wedding</span></div>
</div>
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="display: flex; gap: 8px;"><span class="dot" style="width: 22px; border-radius: 4px; background: {INK};"></span><span class="dot"></span><span class="dot"></span></div>
<div style="display: flex; gap: 8px;"><button type="button" class="ctl" aria-label="Previous review" style="width: 44px; height: 44px; justify-content: center; border: 1px solid {INK}; background: transparent; color: {INK};">{ic('arrowl',17)}</button><button type="button" class="ctl" aria-label="Next review" style="width: 44px; height: 44px; justify-content: center; background: {INK}; color: #FFFFFF;">{ic('arrow',17)}</button></div>
</div>
</div>''')
    chks = ''.join(f'<span class="chk"><span style="color: #FFFFFF; display: flex;">{ic("check",15,2)}</span>{b}</span>' for b in BENEFITS)
    h.append(f'''<div style="position: relative; background: {INK}; color: #FFFFFF; overflow: hidden;">
<img src="{u('cup_hand')}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 60%;">
<div style="position: absolute; inset: 0; background: rgba(0,0,0,0.64);"></div>
<div style="position: relative; padding: 48px 20px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 16px;">
{cue('04','Get in touch',True)}
<h2 class="h" style="margin: 0; font-size: 42px; line-height: 1.02;">Let's put coffee on the <em>guest list.</em></h2>
<p style="margin: 0; font-size: 15px; line-height: 1.5; color: #E9E6DE; text-wrap: balance;">Share the date, headcount and location. We'll send a quote.</p>
<div style="align-self: stretch; display: flex; flex-direction: column; margin-top: 8px;">{btn('Get a quote','bw','cal','18px',12)}</div>
<div class="m" style="font-size: 11px; letter-spacing: 0.05em; color: rgba(255,255,255,0.8);">We reply within [owner to confirm]</div>
<div style="display: flex; flex-direction: column; align-items: flex-start; gap: 8px; font-size: 14px; color: #F0EEE8; margin-top: 4px;">{chks}</div>
</div>
</div>''')
    a = lambda t: f'<a href="#" style="text-decoration: none; font-size: 15px; font-weight: 500;">{t}</a>'
    h.append(f'''<div style="flex-grow: 1; position: relative; overflow: hidden; background: {STONE};">
<div style="padding: 48px 20px 0; display: flex; flex-direction: column; gap: 28px;">
<div>{logo(28)}</div>
<p style="margin: 0; font-size: 15px; line-height: 1.6; color: {MUTED};">Coffee is better shared. That's the whole idea behind the name.</p>
<div style="display: flex; gap: 10px; align-items: center;">{btn('Get a quote','bk','cal','13px 18px',11)}<a href="#" class="soc" aria-label="Instagram @fellowshipcoffee.co" style="width: 40px; height: 40px;">{ic('ig',17,1.6)}</a><a href="#" class="soc" aria-label="Facebook" style="width: 40px; height: 40px;">{ic('fb',17,1.6)}</a></div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 28px;">
<div style="display: flex; flex-direction: column; gap: 10px;"><span class="lab" style="color: #8A857B; font-size: 10px;">Services</span>{a('Weddings')}{a('Corporate')}{a('Celebrations')}</div>
<div style="display: flex; flex-direction: column; gap: 10px;"><span class="lab" style="color: #8A857B; font-size: 10px;">Resources</span>{a('Menu')}{a('FAQs')}{a('Get a quote')}</div>
<div style="display: flex; flex-direction: column; gap: 10px;"><span class="lab" style="color: #8A857B; font-size: 10px;">Company</span>{a('About')}{a('The Coffee Shop')}</div>
</div>
<div style="display: flex; flex-direction: column; gap: 10px; font-size: 15px; color: {MUTED};"><span class="lab" style="color: #8A857B; font-size: 10px;">Visit the café</span><span style="display: flex; gap: 8px;">{ic('pin',16)}3434 FM 1092 Rd #350, Missouri City, TX 77459</span><span style="display: flex; gap: 8px; align-items: center;">{ic('clock',16)}[Hours]</span></div>
<div class="card" style="padding: 20px; display: flex; flex-direction: column; gap: 14px;">
<div style="display: flex; align-items: center; gap: 12px;"><span style="width: 42px; height: 42px; flex-shrink: 0; border-radius: 50%; border: 1px solid {LINE}; display: flex; align-items: center; justify-content: center;">{ic('mail',19,1.6)}</span><div class="h" style="font-size: 18px; line-height: 1.25; letter-spacing: -0.02em;">Coffee news and event ideas, now and then.</div></div>
<div style="display: flex; gap: 8px;"><label style="flex-grow: 1; display: flex;"><span style="position: absolute; left: -9999px;">Email</span><input type="email" placeholder="Your email" style="width: 100%; border: 1px solid {LINE}; background: #FAFAF7; border-radius: 2px; padding: 13px 14px; font: 15px 'Inter Tight', sans-serif;"></label><button type="button" class="b bk" style="border: none; padding: 0 16px; font-size: 10px; cursor: pointer;">Sign up</button></div>
</div>
<div class="m" style="border-top: 1px solid #DAD6CB; padding-top: 16px; display: flex; justify-content: space-between; font-size: 11px; color: {MUTED};"><span>© 2026 Fellowship Coffee Co.</span><a href="#" style="color: {MUTED};">Privacy</a></div>
</div>
<div aria-hidden="true" style="margin: 28px 0 0; height: 48px; overflow: hidden; opacity: 0.08;"><img src="{u('logo_k')}" alt="" style="width: 100%; height: auto; display: block;"></div>
</div>''')
    return page('Fellowship home, phone v7', 390, '\n\n'.join(h))

if __name__ == '__main__':
    open(f'{SP}/style/project/Home-Desktop.dc.html', 'w').write(desktop())
    open(f'{SP}/style/project/Home-Phone.dc.html', 'w').write(phone())
    print('generated v7')
