window.onload = function() {
    // Код, зависящий от GSAP
    gsap.registerPlugin(ScrollTrigger, ScrollSmoother);
    // Другие действия
    if (ScrollTrigger.itTouch !==1) {
    ScrollSmoother.create ({
    wrapper: '.wrapper',
    content: '.content1',
    smooth: 1.5,
    effects: true
})
}
};

// app.js


