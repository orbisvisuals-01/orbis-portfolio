const portfolioCards = document.querySelectorAll(".project-card");

if (window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
  window.addEventListener("mousemove", (event) => {
    portfolioCards.forEach((card) => {
      const rect = card.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      const isInside = x >= 0 && x <= rect.width && y >= 0 && y <= rect.height;

      if (!isInside) {
        card.style.setProperty("--tilt-x", "0deg");
        card.style.setProperty("--tilt-y", "0deg");
        return;
      }

      const xPercent = (x / rect.width) * 100;
      const yPercent = (y / rect.height) * 100;
      const rotateY = ((x / rect.width) - 0.5) * 5;
      const rotateX = ((0.5 - (y / rect.height)) * 5);

      card.style.setProperty("--mouse-x", `${xPercent}%`);
      card.style.setProperty("--mouse-y", `${yPercent}%`);
      card.style.setProperty("--tilt-x", `${rotateX.toFixed(2)}deg`);
      card.style.setProperty("--tilt-y", `${rotateY.toFixed(2)}deg`);
    });
  });

  portfolioCards.forEach((card) => {
    card.addEventListener("mouseleave", () => {
      card.style.setProperty("--tilt-x", "0deg");
      card.style.setProperty("--tilt-y", "0deg");
    });
  });
}

document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", (event) => {
    const id = anchor.getAttribute("href");
    if (id === "#") return;

    const target = document.querySelector(id);
    if (!target) return;

    event.preventDefault();
    target.scrollIntoView({ behavior: "smooth", block: "start" });
  });
});
