document.addEventListener("DOMContentLoaded", () => {
  const overlay = document.querySelector(".xmas-overlay");
  if (!overlay) return;

  function spawn(size, count) {
    for (let i = 0; i < count; i++) {
      const el = document.createElement("div");
      el.className = `snowflake ${size}`;
      el.style.left = Math.random() * 100 + "%";
      el.style.animationDelay = Math.random() * 5 + "s";
      overlay.appendChild(el);
    }
  }

  spawn("large", 4);
  spawn("medium", 7);
  spawn("small", 12);
});
