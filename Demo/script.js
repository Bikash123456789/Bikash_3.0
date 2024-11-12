// GSAP Animation for smooth page scroll
gsap.from("#navbar", {
    opacity: 0,
    y: -50,
    duration: 1,
  });
  
  gsap.from("#about .content", {
    opacity: 0,
    y: 50,
    duration: 1,
    delay: 0.5,
  });
  
  gsap.from("#skills .content", {
    opacity: 0,
    x: -100,
    duration: 1,
    delay: 1,
  });
  
  gsap.from("#projects .content", {
    opacity: 0,
    x: 100,
    duration: 1,
    delay: 1.5,
  });
  
  gsap.from("#contact .content", {
    opacity: 0,
    y: 50,
    duration: 1,
    delay: 2,
  });
  
  // Fancy Logo Animation on Load
  window.onload = function () {
    gsap.from(".logo img", {
      scale: 0,
      duration: 1,
      ease: "back.out(1.7)",
    });
  };
  