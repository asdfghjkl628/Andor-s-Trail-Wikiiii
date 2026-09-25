// Legend checkboxes toggle overlay types on map pages.
document.addEventListener('change', function (e) {
  var cb = e.target;
  if (!cb.matches || !cb.matches('.map-legend input[data-t]')) return;
  var wrap = cb.closest('.map-legend').nextElementSibling;
  while (wrap && !wrap.classList.contains('map-wrap')) wrap = wrap.nextElementSibling;
  if (wrap) wrap.classList.toggle('hide-' + cb.dataset.t, !cb.checked);
});

// Clicking a yellow container box opens a popup listing its contents (links go to item pages).
document.addEventListener('click', function (e) {
  var old = document.querySelector('.map-pop');
  var box = e.target.closest && e.target.closest('[data-container]');
  if (old && (!old.contains(e.target) || e.target.classList.contains('x'))) old.remove();
  if (!box) return;
  e.preventDefault();
  var src = document.getElementById(box.dataset.container);
  var wrap = box.closest('.map-wrap');
  if (!src || !wrap) return;
  var pop = document.createElement('div');
  pop.className = 'map-pop';
  pop.innerHTML = '<span class="x" title="Close">×</span>' + src.innerHTML;
  wrap.appendChild(pop);
  var bx = box.offsetLeft, by = box.offsetTop + box.offsetHeight + 4;
  if (bx + pop.offsetWidth > wrap.clientWidth) bx = Math.max(0, wrap.clientWidth - pop.offsetWidth);
  if (by + pop.offsetHeight > wrap.clientHeight) by = Math.max(0, box.offsetTop - pop.offsetHeight - 4);
  pop.style.left = bx + 'px'; pop.style.top = by + 'px';
});
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') { var p = document.querySelector('.map-pop'); if (p) p.remove(); }
});
