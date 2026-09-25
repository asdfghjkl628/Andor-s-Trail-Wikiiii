// Legend checkboxes toggle overlay types on map pages.
document.addEventListener('change', function (e) {
  var cb = e.target;
  if (!cb.matches || !cb.matches('.map-legend input[data-t]')) return;
  var wrap = cb.closest('.map-legend').nextElementSibling;
  while (wrap && !wrap.classList.contains('map-wrap')) wrap = wrap.nextElementSibling;
  if (wrap) wrap.classList.toggle('hide-' + cb.dataset.t, !cb.checked);
});
