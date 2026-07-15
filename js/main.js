(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    var toggle = document.querySelector('.nav-toggle');
    var nav = document.querySelector('.primary-nav');
    var dropdownTriggers = document.querySelectorAll('.nav-item.has-dropdown > a');
    var dropdownItems = document.querySelectorAll('.nav-item.has-dropdown');

    if (toggle && nav) {
      toggle.addEventListener('click', function (e) {
        e.preventDefault();
        var isOpen = nav.classList.toggle('is-open');
        toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      });
    }

    dropdownTriggers.forEach(function (trigger) {
      trigger.setAttribute('aria-haspopup', 'true');
      trigger.setAttribute('aria-expanded', 'false');

      trigger.addEventListener('click', function (e) {
        var isMobile = window.matchMedia('(max-width: 860px)').matches;
        if (!isMobile) return;

        e.preventDefault();
        var item = trigger.closest('.nav-item');
        var willOpen = !item.classList.contains('is-open');

        dropdownItems.forEach(function (i) {
          if (i !== item) {
            i.classList.remove('is-open');
            var t = i.querySelector('a');
            if (t) t.setAttribute('aria-expanded', 'false');
          }
        });

        item.classList.toggle('is-open', willOpen);
        trigger.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
      });
    });

    document.addEventListener('click', function (e) {
      if (!e.target.closest('.nav-item.has-dropdown')) {
        dropdownItems.forEach(function (item) {
          item.classList.remove('is-open');
          var trigger = item.querySelector('a');
          if (trigger) trigger.setAttribute('aria-expanded', 'false');
        });
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        dropdownItems.forEach(function (item) { item.classList.remove('is-open'); });
        if (nav && nav.classList.contains('is-open')) {
          nav.classList.remove('is-open');
          if (toggle) toggle.setAttribute('aria-expanded', 'false');
        }
      }
    });
  });
})();
