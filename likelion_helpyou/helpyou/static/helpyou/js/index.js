    const links = document.querySelectorAll('.click');
    links.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault(); // 이벤트 막기
        });
    });