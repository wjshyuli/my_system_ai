document.addEventListener("DOMContentLoaded", function () {

    const summary = document.querySelector(".summary");

    if (!summary) return;

    let pauseUntil = 0;

    function pauseAutoScroll() {
        pauseUntil = Date.now() + 5000; // 暂停5秒
    }

    // 鼠标操作
    summary.addEventListener("mousedown", pauseAutoScroll);
    summary.addEventListener("wheel", pauseAutoScroll);

    // 触摸屏
    summary.addEventListener("touchstart", pauseAutoScroll);
    summary.addEventListener("touchmove", pauseAutoScroll);

    setInterval(() => {

        if (Date.now() < pauseUntil) {
            return;
        }

        summary.scrollLeft += 1;

        if (
            summary.scrollLeft >=
            summary.scrollWidth - summary.clientWidth
        ) {
            summary.scrollLeft = 0;
        }

    }, 30);

});