"""Generates index.html, de/index.html and es/index.html from one template.

Edit the copy in LANGS, then run: python3 build.py
"""
import html
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://www.ettlinbiomechanics.com"
EMAIL = "ettlinbiomechanics@gmail.com"

LANGS = {
    "en": {
        "path": "",
        "title": "Ettlin Biomechanics | Ride Better. Move Together.",
        "description": "Claudia Ettlin helps riders and horses move in sync using practical biomechanics, improving posture, performance and partnership.",
        "contact_btn": "Contact Us",
        "eyebrow": "Balance Refined",
        "h1": "Ride Better.<br>Move Together.",
        "lead": "At Ettlin Biomechanics, we help riders and horses move in sync using practical biomechanics—improving posture, performance, and partnership.",
        "about_eyebrow": "Who we are",
        "about_h2": "About the Owner",
        "about_h3": '<span class="gold">Claudia Ettlin</span> - Expertise in Biomechanics &amp; Movement',
        "about_p": [
            "As a lifelong horse owner and passionate rider, I bring deep expertise in equine and human biomechanics. With a background in physiotherapy and certifications in equine osteopathy (DIPO) and Lazaris Nerve Release, I specialize in optimizing movement quality and well-being for both horse and rider.",
            "My approach combines precise techniques, personalized training, and knowledge-sharing—empowering horse owners to actively support their horse’s health and performance.",
            "With international experience in diverse riding styles and cultural influences, my goal is to build a foundation for a balanced, biomechanically sound, and joyful partnership between horse and rider.",
        ],
        "photo_alt": "Claudia Ettlin with her two black Labradors",
        "balance_eyebrow": "Balance &amp; Harmony",
        "balance_h2": "Ettlin Biomechanics – Balance &amp; Harmony for Horse and Rider",
        "balance_p": [
            "At Ettlin Biomechanics, we focus on the well-being and perfect balance between you and your horse. By understanding biomechanics, I help riders refine their body awareness and improve their horse’s movement, performance, and harmony.",
            "My mission is to equip riders with practical strategies and knowledge, ensuring both horse and rider move biomechanically correctly. The result? A stronger, healthier horse and a trusting, harmonious partnership.",
        ],
        "contact_h2": "Get in touch",
        "contact_sub": "To schedule an initial consultation and receive a personalized quote.",
        "f_first": "First name", "f_last": "Last name", "f_email": "Email", "f_phone": "Phone",
        "f_msg": "Write a message", "f_submit": "Submit",
        "f_note": "This opens your email app with your message ready to send. Or write to us directly at",
        "subject": "Website enquiry from",
        "quick": "Quick links",
        "links": ["Home", "About Me", "Ettlin Biomechanics", "Contact Us"],
        "contact_info": "Contact Info",
        "skip": "Skip to main content",
        "lang_label": "Language",
    },
    "de": {
        "path": "de/",
        "title": "Ettlin Biomechanics | Reiten mit Harmonie",
        "description": "Claudia Ettlin hilft Reitern und Pferden durch praktische Biomechanik, sich harmonisch zu bewegen: für bessere Haltung, Leistung und Verbindung.",
        "contact_btn": "Kontakt",
        "eyebrow": "Reiten mit Harmonie",
        "h1": "Optimale Bewegung für Pferd und Reiter",
        "lead": "Bei Ettlin Biomechanics helfen wir Reitern und Pferden durch praktische Biomechanik, sich harmonisch zu bewegen. Verbessern Sie Haltung, Leistung und Verbindung – für eine ausgewogene, vertrauensvolle Partnerschaft.",
        "about_eyebrow": "Über uns",
        "about_h2": "Claudia Ettlin",
        "about_h3": '<span class="gold">Expertise</span> in Biomechanik &amp; Bewegung',
        "about_p": [
            "Als leidenschaftliche Reiterin und erfahrene Pferdebesitzerin bringe ich tiefgehendes Expertenwissen in der Biomechanik von Pferd und Mensch mit. Mit einem Hintergrund in Physiotherapie und Zertifizierungen in Pferdeosteopathie (DIPO) sowie Lazaris Nerve Release spezialisiere ich mich auf die Optimierung von Bewegungsqualität und Wohlbefinden für Pferd und Reiter.",
            "Mein Ansatz kombiniert präzise Techniken, individuelles Training und Wissensvermittlung – so unterstütze ich Pferdebesitzer dabei, aktiv zur Gesundheit und Leistungsfähigkeit ihres Pferdes beizutragen.",
            "Durch meine internationale Erfahrung mit verschiedenen Reitweisen und kulturellen Einflüssen ist es mein Ziel, eine solide Grundlage für eine biomechanisch gesunde, ausgeglichene und freudvolle Partnerschaft zwischen Pferd und Reiter zu schaffen.",
        ],
        "photo_alt": "Claudia Ettlin mit ihren zwei schwarzen Labradoren",
        "balance_eyebrow": "Balance &amp; Harmonie",
        "balance_h2": "Ettlin Biomechanics – Balance &amp; Harmonie für Pferd und Reiter",
        "balance_p": [
            "Bei Ettlin Biomechanics konzentrieren wir uns auf das Wohlbefinden und die perfekte Balance zwischen Ihnen und Ihrem Pferd. Durch mein Verständnis der Biomechanik helfe ich Reitern, ihr Körperbewusstsein zu verfeinern und die Bewegung, Leistung und Harmonie ihres Pferdes zu verbessern.",
            "Meine Mission ist es, Reiter mit praktischen Strategien und Wissen auszustatten, um sicherzustellen, dass sich Pferd und Reiter biomechanisch korrekt bewegen. Das Ergebnis? Ein stärkeres, gesünderes Pferd und eine vertrauensvolle, harmonische Partnerschaft.",
        ],
        "contact_h2": "Kontaktieren Sie uns",
        "contact_sub": "Vereinbaren Sie einen ersten Beratungstermin und erhalten Sie ein individuelles Angebot.",
        "f_first": "Vorname", "f_last": "Nachname", "f_email": "E-Mail", "f_phone": "Telefon",
        "f_msg": "Nachricht schreiben", "f_submit": "Senden",
        "f_note": "Dadurch öffnet sich Ihr E-Mail-Programm mit Ihrer vorbereiteten Nachricht. Oder schreiben Sie uns direkt an",
        "subject": "Anfrage über die Website von",
        "quick": "Quick Links",
        "links": ["Startseite", "Claudia Ettlin", "Ettlin Biomechanics", "Kontaktieren Sie uns"],
        "contact_info": "Kontaktinformationen",
        "skip": "Zum Hauptinhalt springen",
        "lang_label": "Sprache",
    },
    "es": {
        "path": "es/",
        "title": "Ettlin Biomechanics | Monta Mejor. Muévanse Juntos.",
        "description": "Claudia Ettlin ayuda a jinetes y caballos a moverse en sincronía mediante la biomecánica aplicada, mejorando la postura, el rendimiento y la conexión mutua.",
        "contact_btn": "Contáctanos",
        "eyebrow": "Equilibrio Refinado",
        "h1": "Monta Mejor.<br>Muévanse Juntos.",
        "lead": "En Ettlin Biomechanics, ayudamos a jinetes y caballos a moverse en sincronía mediante la biomecánica aplicada, mejorando la postura, el rendimiento y la conexión mutua.",
        "about_eyebrow": "Quiénes somos",
        "about_h2": "Sobre la Fundadora",
        "about_h3": '<span class="gold">Claudia Ettlin</span> – Experta en Biomecánica y Movimiento',
        "about_p": [
            "Como propietaria de caballos de toda la vida y apasionada jinete, aporto una profunda experiencia en biomecánica equina y humana. Con formación en fisioterapia y certificaciones en osteopatía equina (DIPO) y Liberación Neural Lazaris, me especializo en optimizar la calidad del movimiento y el bienestar tanto del caballo como del jinete.",
            "Mi enfoque combina técnicas precisas, entrenamiento personalizado y compartición de conocimientos, empoderando a los propietarios de caballos para apoyar activamente la salud y el rendimiento de sus animales.",
            "Con experiencia internacional en diversos estilos de equitación e influencias culturales, mi objetivo es construir una base para una asociación equilibrada, biomecánicamente sólida y alegre entre jinete y caballo.",
        ],
        "photo_alt": "Claudia Ettlin con sus dos labradores negros",
        "balance_eyebrow": "Equilibrio y Armonía",
        "balance_h2": "Ettlin Biomechanics: Equilibrio y armonía para el caballo y el jinete",
        "balance_p": [
            "En Ettlin Biomechanics, nos centramos en el bienestar y el equilibrio perfecto entre usted y su caballo. Al comprender la biomecánica, ayudo a los jinetes a perfeccionar su conciencia corporal y a mejorar el movimiento, el rendimiento y la armonía de su caballo.",
            "Mi misión es dotar a los jinetes de estrategias y conocimientos prácticos, garantizando que tanto el caballo como el jinete se muevan biomecánicamente correctamente. ¿El resultado? Un caballo más fuerte y sano, y una relación armoniosa y de confianza.",
        ],
        "contact_h2": "Ponte en contacto con nosotros",
        "contact_sub": "Para agendar una consulta inicial y recibir una cotización personalizada.",
        "f_first": "Nombre", "f_last": "Apellido", "f_email": "Correo electrónico", "f_phone": "Teléfono",
        "f_msg": "Escribe un mensaje", "f_submit": "Enviar",
        "f_note": "Se abrirá tu aplicación de correo con el mensaje listo para enviar. O escríbenos directamente a",
        "subject": "Consulta desde la web de",
        "quick": "Enlaces rápidos",
        "links": ["Inicio", "Sobre mí", "Ettlin Biomechanics", "Contacto"],
        "contact_info": "Información de contacto",
        "skip": "Ir al contenido principal",
        "lang_label": "Idioma",
    },
}

ARROW = '<svg class="arrow" viewBox="0 0 200 200" aria-hidden="true"><path d="M30.718 20l138.564 80-138.564 80 53.417-80.027L30.718 20z"/></svg>'
MAIL = '<svg viewBox="20 35 160 130" aria-hidden="true"><path d="M160.062 165H39.936C28.942 165 20 156.055 20 145.058V54.943C20.001 43.946 28.943 35 39.936 35h120.125c10.994 0 19.938 8.946 19.938 19.943v90.116c0 10.996-8.944 19.941-19.937 19.941zM39.936 44.845c-5.565 0-10.093 4.53-10.093 10.098v90.116c0 5.568 4.528 10.097 10.093 10.097h120.125c5.567 0 10.095-4.529 10.095-10.097V54.943c0-5.568-4.528-10.098-10.095-10.098H39.936z"/><path d="M100 112.433a4.914 4.914 0 0 1-2.822-.89L22.1 58.975a4.922 4.922 0 0 1 5.643-8.065L100 101.502l72.257-50.591a4.922 4.922 0 0 1 5.643 8.065l-75.078 52.567a4.914 4.914 0 0 1-2.822.89z"/></svg>'


def horse_svg(cls):
    svg = (ROOT / "assets/img/horse.svg").read_text()
    return svg.replace("<svg ", f'<svg class="{cls}" aria-hidden="true" ', 1)


def lang_switch(code, t, prefix):
    current = ' aria-current="true"'
    opts = "".join(
        f'<a href="{(prefix + LANGS[c]["path"]) or "./"}" hreflang="{c}" lang="{c}"'
        f'{current if c == code else ""}>{c.upper()}</a>'
        for c in LANGS
    )
    return (
        f'<details class="lang"><summary aria-label="{t["lang_label"]}">{code.upper()}'
        f'<svg viewBox="0 0 12 6" aria-hidden="true"><path d="M1 .5l5 5 5-5" fill="none" stroke="currentColor"/></svg>'
        f"</summary><div>{opts}</div></details>"
    )


def page(code):
    t = LANGS[code]
    prefix = "../" if t["path"] else ""
    a = f"{prefix}assets"
    alternates = "\n".join(
        f'  <link rel="alternate" hreflang="{c}" href="{SITE}/{LANGS[c]["path"]}">' for c in LANGS
    ) + f'\n  <link rel="alternate" hreflang="x-default" href="{SITE}/">'
    about_p = "\n".join(f"        <p>{p}</p>" for p in t["about_p"])
    balance_p = "\n".join(f"      <p>{p}</p>" for p in t["balance_p"])
    links = t["links"]
    horse = horse_svg("eyebrow-horse")
    return f"""<!doctype html>
<html lang="{code}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{t["title"]}</title>
  <meta name="description" content="{html.escape(t["description"])}">
  <link rel="canonical" href="{SITE}/{t["path"]}">
{alternates}
  <meta property="og:type" content="website">
  <meta property="og:title" content="{html.escape(t["title"])}">
  <meta property="og:description" content="{html.escape(t["description"])}">
  <meta property="og:url" content="{SITE}/{t["path"]}">
  <meta property="og:image" content="{SITE}/assets/img/hero.jpg">
  <link rel="icon" href="{a}/img/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="{a}/img/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&family=Rufina:wght@700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{a}/styles.css">
</head>
<body>
  <a class="skip" href="#main">{t["skip"]}</a>
  <header class="site-header" id="top">
    <div class="wrap header-inner">
      <a class="logo" href="#top"><img src="{a}/img/logo.png" alt="Ettlin Biomechanics" width="98" height="111"></a>
      <div class="header-actions">
        {lang_switch(code, t, prefix)}
        <a class="btn" href="#contact">{t["contact_btn"]} {ARROW}</a>
      </div>
    </div>
  </header>

  <main id="main">
    <section class="hero">
      <div class="wrap hero-inner">
        <p class="eyebrow-light">{horse}{t["eyebrow"]}</p>
        <h1>{t["h1"]}</h1>
        <p class="lead">{t["lead"]}</p>
        <a class="btn" href="#contact">{t["contact_btn"]} {ARROW}</a>
      </div>
    </section>

    <section class="about" id="about">
      <div class="wrap">
        <div class="section-head">
          {horse_svg("head-horse")}
          <p class="eyebrow">{t["about_eyebrow"]}</p>
          <h2>{t["about_h2"]}</h2>
        </div>
        <div class="about-grid">
          <div class="about-text">
            <h3>{t["about_h3"]}</h3>
{about_p}
          </div>
          <figure class="about-photo">
            <img src="{a}/img/claudia-dogs.jpg" alt="{t["photo_alt"]}" width="1200" height="800" loading="lazy">
          </figure>
        </div>
      </div>
    </section>

    <section class="balance" id="balance">
      <div class="wrap narrow">
        <p class="eyebrow">{t["balance_eyebrow"]}</p>
        <h2>{t["balance_h2"]}</h2>
{balance_p}
      </div>
    </section>

    <section class="contact" id="contact">
      <div class="wrap">
        <form class="contact-card" id="contact-form" data-email="{EMAIL}" data-subject="{html.escape(t["subject"])}" novalidate>
          <h2>{t["contact_h2"]}</h2>
          <p class="contact-sub">{t["contact_sub"]}</p>
          <div class="fields">
            <label>{t["f_first"]} *<input name="first" autocomplete="given-name" required></label>
            <label>{t["f_last"]}<input name="last" autocomplete="family-name"></label>
            <label>{t["f_email"]} *<input name="email" type="email" autocomplete="email" required></label>
            <label>{t["f_phone"]}<input name="phone" type="tel" autocomplete="tel"></label>
            <label class="full">{t["f_msg"]}<textarea name="message" rows="4"></textarea></label>
          </div>
          <button class="btn-submit" type="submit">{t["f_submit"]}</button>
          <p class="form-note">{t["f_note"]} <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
        </form>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="wrap footer-grid">
      <a class="footer-logo" href="#top"><img src="{a}/img/logo.png" alt="Ettlin Biomechanics" width="149" height="170" loading="lazy"></a>
      <nav aria-label="{t["quick"]}">
        <h4>{t["quick"]}</h4>
        <a href="#top">{links[0]}</a>
        <a href="#about">{links[1]}</a>
        <a href="#balance">{links[2]}</a>
        <a href="#contact">{links[3]}</a>
      </nav>
      <div>
        <h4>{t["contact_info"]}</h4>
        <a class="mail" href="mailto:{EMAIL}">{MAIL}{EMAIL}</a>
        {lang_switch(code, t, prefix).replace('class="lang"', 'class="lang lang-up"')}
      </div>
    </div>
  </footer>
  <script src="{a}/site.js" defer></script>
</body>
</html>
"""


for code, t in LANGS.items():
    out = ROOT / t["path"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(code))
    print("wrote", out.relative_to(ROOT))
