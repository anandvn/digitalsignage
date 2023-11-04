document.addEventListener('DOMContentLoaded', function () {
  const content = document.querySelector('.menu');
  const itemsPerPage = 6;
  let currentPage = 0;
  const items = Array.from(content.getElementsByTagName('tr')).slice(1);
  const totalPages = Math.floor(items.length / itemsPerPage);

function showPage(page) {
  const startIndex = page * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  items.forEach((item, index) => {
    item.classList.toggle('hidden', index < startIndex || index >= endIndex);
  });
}

function run() {
    showPage(currentPage);
    currentPage = currentPage + 1;
    if (currentPage > totalPages-1) {
        currentPage = 0;
    }
}

setInterval(run, 10000);
});

