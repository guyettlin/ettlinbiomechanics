const header = document.querySelector(".site-header");
const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 40);
onScroll();
window.addEventListener("scroll", onScroll, { passive: true });
window.addEventListener("load", onScroll);

document.querySelectorAll("details.lang").forEach((d) => {
  document.addEventListener("click", (e) => { if (!d.contains(e.target)) d.open = false; });
});

// The site is static, so the form composes an email in the visitor's mail app.
const form = document.getElementById("contact-form");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  let ok = true;
  form.querySelectorAll("[required]").forEach((el) => {
    const valid = el.value.trim() && el.checkValidity();
    el.classList.toggle("invalid", !valid);
    if (!valid && ok) { el.focus(); ok = false; }
  });
  if (!ok) return;
  const v = (n) => form.elements[n].value.trim();
  const name = [v("first"), v("last")].filter(Boolean).join(" ");
  const lines = [v("message"), "", name, v("email"), v("phone")].filter((l, i) => i < 2 || l);
  const href = `mailto:${form.dataset.email}?subject=${encodeURIComponent(`${form.dataset.subject} ${name}`)}&body=${encodeURIComponent(lines.join("\n"))}`;
  window.location.href = href;
});
