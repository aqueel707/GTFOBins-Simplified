/* assets/js/app.js — GTFOBins-Simplified */
(function () {
  "use strict";

  /* ── Index: search + capability filter ──────────────── */
  const searchInput = document.getElementById("search-input");
  const capButtons  = document.querySelectorAll(".cap-filter-btn[data-cap]");
  const clearBtn    = document.getElementById("clear-filter");
  const rows        = document.querySelectorAll(".binary-row");
  const countEl     = document.getElementById("visible-count");

  if (!searchInput) return; // not on index page

  let activeCap = null;

  function filterRows() {
    const q = searchInput.value.trim().toLowerCase();
    let visible = 0;

    rows.forEach(function (row) {
      const name = (row.dataset.name  || "").toLowerCase();
      const caps = (row.dataset.caps  || "").toLowerCase();
      const tags = (row.dataset.tags  || "").toLowerCase();

      const matchesSearch = !q || name.includes(q) || caps.includes(q) || tags.includes(q);
      const matchesCap    = !activeCap || caps.split(" ").includes(activeCap);

      if (matchesSearch && matchesCap) {
        row.classList.remove("hidden");
        visible++;
      } else {
        row.classList.add("hidden");
      }
    });

    if (countEl) countEl.textContent = visible;
  }

  searchInput.addEventListener("input", filterRows);

  capButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      if (activeCap === btn.dataset.cap) {
        // deselect
        activeCap = null;
        capButtons.forEach(function (b) { b.classList.remove("active"); });
      } else {
        activeCap = btn.dataset.cap;
        capButtons.forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
      }
      filterRows();
    });
  });

  if (clearBtn) {
    clearBtn.addEventListener("click", function () {
      activeCap = null;
      capButtons.forEach(function (b) { b.classList.remove("active"); });
      searchInput.value = "";
      filterRows();
    });
  }

  /* ── Binary page: copy command on click ─────────────── */
  document.querySelectorAll(".command-block").forEach(function (block) {
    block.setAttribute("title", "Click to copy");
    block.style.cursor = "pointer";

    block.addEventListener("click", function () {
      const text = block.textContent || "";
      navigator.clipboard.writeText(text.trim()).then(function () {
        const prev = block.style.outline;
        block.style.outline = "2px solid var(--red)";
        setTimeout(function () { block.style.outline = prev; }, 600);
      }).catch(function () {
        /* fallback: select text */
        const sel = window.getSelection();
        const range = document.createRange();
        range.selectNodeContents(block);
        sel.removeAllRanges();
        sel.addRange(range);
      });
    });
  });

  /* ── Keyboard shortcut: / to focus search ───────────── */
  document.addEventListener("keydown", function (e) {
    if (e.key === "/" && document.activeElement !== searchInput && searchInput) {
      e.preventDefault();
      searchInput.focus();
    }
    if (e.key === "Escape" && searchInput) {
      searchInput.value = "";
      activeCap = null;
      capButtons.forEach(function (b) { b.classList.remove("active"); });
      filterRows();
      searchInput.blur();
    }
  });

})();
