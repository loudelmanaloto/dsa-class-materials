(function () {
  var root = document.documentElement;
  var button = document.getElementById("theme-toggle");
  var label = button.querySelector(".label");

  function current() {
    return root.getAttribute("data-theme") === "dark" ? "dark" : "light";
  }

  function render() {
    // The label names the mode you will switch TO.
    label.textContent = current() === "dark" ? "Light mode" : "Dark mode";
  }

  button.addEventListener("click", function () {
    var next = current() === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try { localStorage.setItem("theme", next); } catch (e) {}
    render();
  });

  // Follow the system setting until the visitor picks a theme themselves.
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function (e) {
    var saved = null;
    try { saved = localStorage.getItem("theme"); } catch (err) {}
    if (!saved) {
      root.setAttribute("data-theme", e.matches ? "dark" : "light");
      render();
    }
  });

  render();
})();
