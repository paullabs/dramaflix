(function () {
  // Quebra as páginas de texto corrido (.flowgroup) sem cortar falas, e numera tudo.
  function fits(c) { return c.scrollHeight <= c.clientHeight + 1; }
  function paginate() {
    document.querySelectorAll('.flowgroup').forEach(function (group) {
      var page = group.querySelector('.page');
      var content = page.querySelector('.content');
      var guard = 0;
      while (!fits(content) && guard++ < 80) {
        var np = page.cloneNode(true);
        var nc = np.querySelector('.content');
        nc.innerHTML = '';
        while (!fits(content) && content.children.length > 1) {
          nc.insertBefore(content.lastElementChild, nc.firstChild);
        }
        while (content.children.length > 1 && content.lastElementChild.classList.contains('keepnext')) {
          nc.insertBefore(content.lastElementChild, nc.firstChild);
        }
        var k = document.createElement('div');
        k.className = 'cont';
        k.textContent = 'continuação';
        nc.insertBefore(k, nc.firstChild);
        page.parentNode.insertBefore(np, page.nextSibling);
        page = np;
        content = nc;
      }
    });
    var pages = document.querySelectorAll('.page');
    pages.forEach(function (p, i) {
      var n = p.querySelector('.pnum');
      if (n) n.textContent = (i + 1) + ' / ' + pages.length;
    });
    document.body.setAttribute('data-paginado', pages.length);
  }
  if (document.readyState === 'complete') paginate(); else window.addEventListener('load', paginate);
})();
