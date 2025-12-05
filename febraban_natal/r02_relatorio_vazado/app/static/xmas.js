document.addEventListener("DOMContentLoaded", () => {
  const overlay = document.querySelector(".xmas-overlay");
  if (!overlay) return;

  function spawn(size, count) {
    for (let i = 0; i < count; i++) {
      const flake = document.createElement("div");
      flake.className = `snowflake ${size}`;
      flake.style.left = Math.random() * 100 + "%";
      flake.style.animationDelay = (Math.random() * 5) + "s";
      overlay.appendChild(flake);
    }
  }

  spawn("large", 4);
  spawn("medium", 7);
  spawn("small", 12);
});
